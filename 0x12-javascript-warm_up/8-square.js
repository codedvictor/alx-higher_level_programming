#!/usr/bin/node

const value = parseInt(process.argv[2]);
let size;

if (Number.isNaN(value)){
  console.log('Missing size');
} else {
  for (let x = 0; x < value; x++){
    size = '';
    for (let y = 0; y < value; y++){
      size += 'X';
    }
    console.log(size);
  }
}
