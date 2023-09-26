#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node get-status-code.js <URL>');
  process.exit(1);
}

const urlPath = process.argv[2];

//  send a GET request and display the status code
request.get(urlPath, (err, response) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
