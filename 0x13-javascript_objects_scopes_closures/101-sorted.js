#!/usr/bin/node

const eDict = require('./101-data').dict;
const nDict = {};

Object.keys(eDict).map (function (key) {
  if (nDict[eDict[key]] === undefined) {
    nDict[eDict[key]] = [];
  }
  nDict[eDict[key]].push(key);
});

console.log(nDict);
