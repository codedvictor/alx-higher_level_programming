#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node get-status-code.js <URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

//  send a GET request and display the movie count
request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const starData = JSON.parse(body).results;
    const wedgeMovies = starData.filter((film) => {
      const characters = film.characters.map((characterUrl) =>
        characterUrl.split('/').slice(-2, -1).pop()
      );
      return characters.includes('18');
    });
    console.log(`${wedgeMovies.length}`);
  }
});
