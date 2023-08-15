#!/usr/bin/node

const myObj = {
  type: 'object',
  value: 12
};
console.log(myObj);

myObj.incr = function () {
  this.value++;
};

myObject.incr();
console.log(myObj);
myObject.incr();
console.log(myObj);
myObject.incr();
console.log(myObj);
