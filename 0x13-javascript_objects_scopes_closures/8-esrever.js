#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];

  for (let x = list.length - 1; x >= 0; x--) {
    reversedList[list.length - x - 1] = list[x];
  }

  return reversedList;
};
