#!/usr/bin/node
const eDict = require('./101-data.js').dict;
let nDict = {};

for (let key in eDict) {
  if (nDict[eDict[key]] === undefined) {
    nDict[eDict[key]] = [key];
  } else {
    nDict[eDict[key]].push(key);
  }
}
console.log(nDict);
