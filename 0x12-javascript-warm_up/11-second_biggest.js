#!/usr/bin/node

let big = 0;
const listNum = [];
let x;

for (x = 2; x < process.argv.length; x++) {
  if (!Number.isNaN(parseInt(process.argv[x]))) {
    listNum[x - 2] = parseInt(process.argv[x]);
  }
}

if (listNum.length > 1) {
  big = Math.max.apply(null, listNum);
  x = listNum.indexOf(big);
  listNum[x] = -Infinity;
  big = Math.max.apply(null, listNum);
}

console.log(big);
