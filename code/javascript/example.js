// npm install --save neo4j-driver
// node example.js
const neo4j = require('neo4j-driver');
const driver = neo4j.driver('neo4j://<HOST>:<BOLTPORT>',
                  neo4j.auth.basic('<USERNAME>', '<PASSWORD>'), 
                  {/* encrypted: 'ENCRYPTION_OFF' */});

const query =
  `
  MATCH (i:IP {ip:$ipAddress})-[r:FROM_IP]-(p:Purchase)
  RETURN p.amount as amount
  `;

const params = {"ipAddress": "168.166.144.243"};

const session = driver.session({database:"neo4j"});

session.run(query, params)
  .then((result) => {
    result.records.forEach((record) => {
        console.log(record.get('amount'));
    });
    session.close();
    driver.close();
  })
  .catch((error) => {
    console.error(error);
  });
