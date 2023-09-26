#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 3) {
  console.error('Usage: node read-file.js <file_path>');
  process.exit(1);
}

const file_Path = process.argv[2];

// Read and print the content of the file in utf-8 encoding
fs.readFile(file_Path, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});

