#!/usr/bin/node

const value = parseInt(process.argv[2]);

if (Number.isNaN(value)){
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < value; x++){
    console.log('C is fun');
  }
}
