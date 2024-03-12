# pip3 install neo4j
# python3 example.py

from neo4j import GraphDatabase, basic_auth

cypher_query = '''
MATCH (i:IP {ip:$ipAddress})-[r:FROM_IP]-(p:Purchase)
RETURN p.amount as amount
'''

with GraphDatabase.driver(
    "neo4j://<HOST>:<BOLTPORT>",
    auth=("<USERNAME>", "<PASSWORD>")
) as driver:
    result = driver.execute_query(
        cypher_query,
        ipAddress="168.166.144.243",
        database_="neo4j")
    for record in result.records:
        print(record['amount'])
