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
    const dataTask = JSON.parse(body);
    const userCompletedTask = {};

    dataTask.forEach((task) => {
      if (task.completed) {
        if (!userCompletedTask[task.userId]) {
          userCompletedTask[task.userId] = 1;
        } else {
          userCompletedTask[task.userId]++;
        }
      }
    });

    Object.keys(userCompletedTask).forEach((userId) => {
      console.log(`'${userId}': ${userCompletedTask[userId]},`);
    });
  }
});
