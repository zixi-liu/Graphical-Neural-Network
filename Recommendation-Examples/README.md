# Personalized Product Recommendations


[Cypher Cheatsheet](https://neo4j.com/docs/cypher-refcard/current/?ref=browser-guide)

**Example of Neo4j Movie Recommendations**

```
CALL db.schema.visualization()
```

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/recommendation-movie.png" alt="recommendation"/>

### Content-Based Filtering

Recommend items that are similar to those that a user is viewing, rated highly or purchased previously.

### Collaborative Filtering

Use the preferences, ratings and actions of other users in the network to find items to recommend.

### Neo4j Graph Data Science (GDS) 

The Neo4j Graph Data Science (GDS) library provides extensive analytical capabilities centered around graph algorithms. The library includes algorithms for community detection, centrality, node similarity, path finding, and link prediction, as well as graph catalog procedures designed to support data science workflows and machine learning tasks over your graphs. 

Neo4j Graph Data Science library supports the random walk algorithm, which makes it very easy for us to implement the node2vec algorithm. 


[Graph Embeddings](https://towardsdatascience.com/node-embeddings-node2vec-with-neo4j-5152d3472d8e)

## Northwind Recommendation Engine 

### Developing a Graph Model

Northwind sells food products in a few categories provided by suppliers. Let's start by loading the product catalog tables.

- Translate the relational data model to a graph data model:
  - A row is a node.
  - A table name is a label name.
  - A join or foreign key is a relationship.
 
**Graph Data Model**

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/northwind_graph.png" alt="Graph-Model" width = "600"/>
 
- Use Cypher’s LOAD CSV command to transform the contents of the CSV file into a graph structure.

**Load Orders**
```
LOAD CSV WITH HEADERS FROM "http://data.neo4j.com/northwind/orders.csv" AS row
CREATE (n:Order)
SET n = row
```

**Load products**
```
LOAD CSV WITH HEADERS FROM "http://data.neo4j.com/northwind/products.csv" AS row
CREATE (n:Product)
SET n = row,
n.unitPrice = toFloat(row.unitPrice),
n.unitsInStock = toInteger(row.unitsInStock), n.unitsOnOrder = toInteger(row.unitsOnOrder),
n.reorderLevel = toInteger(row.reorderLevel), n.discontinued = (row.discontinued <> "0")
```

**Load categories**
```
LOAD CSV WITH HEADERS FROM "http://data.neo4j.com/northwind/categories.csv" AS row
CREATE (n:Category)
SET n = row
```

**Load suppliers**
```
LOAD CSV WITH HEADERS FROM "http://data.neo4j.com/northwind/suppliers.csv" AS row
CREATE (n:Supplier)
SET n = row
```

**Creating the indexes for the data in the graph**

```
CREATE INDEX product_id FOR (p:Product) ON (p.productID);
CREATE INDEX product_name FOR (p:Product) ON (p.productName);
CREATE INDEX supplier_id FOR (s:Supplier) ON (s.supplierID);
CREATE INDEX category_id FOR (c:Category) ON (c.categoryID);
CREATE INDEX order_id FOR (o:Order) ON (o.orderID);
CREATE CONSTRAINT order_id ON (o:Order) ASSERT o.orderID IS UNIQUE;
CALL db.awaitIndexes();
```

**Creating relationships between products and suppliers and between products and categories**

```
MATCH (p:Product),(s:Supplier)
WHERE p.supplierID = s.supplierID
CREATE (s)-[:SUPPLIES]->(p)
```

```
MATCH (p:Product),(c:Category)
WHERE p.categoryID = c.categoryID
CREATE (p)-[:PART_OF]->(c)
```

```
MATCH (n:Customer),(o:Order)
WHERE n.customerID = o.customerID
CREATE (n)-[:PURCHASED]->(o)
```

```
LOAD CSV WITH HEADERS FROM "http://data.neo4j.com/northwind/order-details.csv" AS row
MATCH (p:Product), (o:Order)
WHERE p.productID = row.productID AND o.orderID = row.orderID
CREATE (o)-[details:PRODUCTS]->(p)
SET details = row,
details.quantity = toInteger(row.quantity)
```

**Querying the Graph DB**

```
//find the supplier and category for a specific product
MATCH (s:Supplier)-[r1:SUPPLIES]->(p:Product {productName: 'Chocolade'})-[r2:PART_OF]->(c:Category)
RETURN s, r1, p, r2, c;
```
<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/neo4j_example.png" alt="Graph-Model" width = "400"/>


### Find Popular Products

```
MATCH (cust:Customer)-[:PURCHASED]->(:Order)-[o:ORDERS]->(p:Product)
RETURN cust.companyName, p.productName, COUNT(o) as orders
ORDER BY orders DESC
LIMIT 5
```

### Content Based Recommendations

Based on previous purchases, we can recommend customers anything that they haven’t already bought. For every product the customer has purchased, let’s see what other customers have also purchased.

```
MATCH (c:Customer)-[:PURCHASED]->(:Order)-[o:ORDERS]->(p:Product)<-[:PRODUCTS]-(o2:Order)-[:PRODUCTS]->(p2:Product)-[:PART_OF]->(:Category)<-[:PART_OF]-(p)
WHERE c.customerID = 'ANTON' and NOT( (c)-[:PURCHASED]->(:Order)-[:PRODUCT]->(p2) )
return c.companyName, p.productName as has_purchased, p2.productName as has_also_purchased, count(DISTINCT o2) as occurrences
order by occurrences desc
limit 5
```

| c.companyName	| has_purchased	| has_also_purchased	| occurrences |
| :---: | :---: | :---: | :---: | 
| "Antonio Moreno Taquería"	| "Raclette Courdavault"	| "Flotemysost"	 | 20 |
| "Antonio Moreno Taquería"	| "Geitost"	| "Mozzarella di Giovanni"	| 15 |
| "Antonio Moreno Taquería"	| "Chang"	| "Outback Lager"	| 15 |
| "Antonio Moreno Taquería"	| "Queso Cabrales" | "Mozzarella di Giovanni"	| 15 |
| "Antonio Moreno Taquería"	| "Geitost"	| "Camembert Pierrot"	| 15 |


### Collaborative Filtering

Recommend content based on the feedback from other Customers. To do this, we can use the k-NN (k-nearest neighbors) Algorithm. k-NN works by grouping items into classifications based on their similarity to each other.

```
MATCH (c:Customer)-[:PURCHASED]->(o:Order)-[:PRODUCTS]->(p:Product)
WITH c, count(p) as total
MATCH (c)-[:PURCHASED]->(o:Order)-[:PRODUCTS]->(p:Product)
WITH c, total,p, count(o)*1.0 as orders
MERGE (c)-[rated:RATED]->(p)
ON CREATE SET rated.rating = orders/total
ON MATCH SET rated.rating = orders/total
WITH c.companyName as company, p.productName as product, orders, total, rated.rating as rating
ORDER BY rating DESC
RETURN company, product, orders, total, rating LIMIT 10
```

```
// See Customer's Similar Ratings to Others
MATCH (c1:Customer {customerID:'ANTON'})-[r1:RATED]->(p:Product)<-[r2:RATED]-(c2:Customer)
RETURN c1.customerID, c2.customerID, p.productName, r1.rating, r2.rating,
CASE WHEN r1.rating-r2.rating < 0 THEN -(r1.rating-r2.rating) ELSE r1.rating-r2.rating END as difference
ORDER BY difference ASC
LIMIT 15
```

Create a similarity score between two Customers using Cosine Similarity.

```
MATCH (c1:Customer)-[r1:RATED]->(p:Product)<-[r2:RATED]-(c2:Customer)
WITH
	SUM(r1.rating*r2.rating) as dot_product,
	SQRT( REDUCE(x=0.0, a IN COLLECT(r1.rating) | x + a^2) ) as r1_length,
	SQRT( REDUCE(y=0.0, b IN COLLECT(r2.rating) | y + b^2) ) as r2_length,
	c1,c2
MERGE (c1)-[s:SIMILARITY]-(c2)
SET s.similarity = dot_product / (r1_length * r2_length)
```
```
WITH 1 as neighbours
MATCH (me:Customer)-[:SIMILARITY]->(c:Customer)-[r:RATED]->(p:Product)
WHERE me.customerID = 'ANTON' and NOT ( (me)-[:RATED|PRODUCT|ORDER*1..2]->(p:Product) )
WITH p, COLLECT(r.rating)[0..neighbours] as ratings, collect(c.companyName)[0..neighbours] as customers
WITH p, customers, REDUCE(s=0,i in ratings | s+i) / LENGTH(ratings)  as recommendation
ORDER BY recommendation DESC
RETURN p.productName, customers, recommendation LIMIT 10
```

| p.productName |	customers	| recommendation
| :---: | :---: | :---: | 
| "Mishi Kobe Niku"	| ["Consolidated Holdings"]	| 0.07142857142857142
| "Inlagd Sill"	| ["La maison d'Asie"]	| 0.04838709677419355
| "Tunnbröd"	| ["Island Trading"]	| 0.043478260869565216
