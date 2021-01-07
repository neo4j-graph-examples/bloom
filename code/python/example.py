# pip3 install neo4j-driver
# python3 example.py

from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
  "bolt://<HOST>:<BOLTPORT>", 
  auth=basic_auth("<USERNAME>", "<PASSWORD>"))

cypher_query = '''
MATCH (i:IP {ip:$ipAddress})-[r:FROM_IP]-(p:Purchase) 
RETURN p.amount as amount
'''

with driver.session(database="neo4j") as session:
  results = session.read_transaction(
    lambda tx: tx.run(cypher_query,
      ipAddress="168.166.144.243").data())

  for record in results:
    print(record['amount'])

driver.close()