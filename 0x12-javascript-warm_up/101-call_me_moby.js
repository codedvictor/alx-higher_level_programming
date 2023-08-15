#!/usr/bin/node

const callMeMoby = function (x, theFunction) {
  for (let j = 0; j < x; j++) {
    theFunction();
  }
};

exports.callMeMoby = callMeMoby;
