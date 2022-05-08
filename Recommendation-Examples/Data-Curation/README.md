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

**Querying the Graph DB**

```
//find the supplier and category for a specific product
MATCH (s:Supplier)-[r1:SUPPLIES]->(p:Product {productName: 'Chocolade'})-[r2:PART_OF]->(c:Category)
RETURN s, r1, p, r2, c;
```
<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/neo4j_example.png" alt="Graph-Model" width = "500"/>
