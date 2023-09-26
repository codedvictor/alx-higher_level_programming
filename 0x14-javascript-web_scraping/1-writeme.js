#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: node read-file.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];
const contentWrite = process.argv[3];

//  write and print the content of the file in utf-8 encoding
fs.writeFile(filePath, contentWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
