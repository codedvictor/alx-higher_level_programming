#!/usr/bin/node

let nargCount = 0;

exports.logMe = function (item) {
  console.log(nargCount + ': ' + item);
  nargCount++;
};
