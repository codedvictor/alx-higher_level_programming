#!/usr/bin/node

const eList = require('./100-data').list;

const nList = eList.map((x, index) => x * index);

console.log(eList);
console.log(nList);
