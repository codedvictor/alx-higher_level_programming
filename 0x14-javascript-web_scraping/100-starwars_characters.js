#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node get-status-code.js <URL>');
  process.exit(1);
}

const id = process.argv[2];
const urlPath = `https://swapi-api.alx-tools.com/api/films/${id}`;

//  send a GET request and display the status code
request.get(urlPath, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const starData = JSON.parse(body);
    console.log(`${starData.title}`);
  }
});
