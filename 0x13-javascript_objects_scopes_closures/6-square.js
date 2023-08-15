#!/usr/bin/node

const Squares = require('./5-square');

class Square extends Squares {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let x = 0; x < this.height; x++) {
        let squa = '';
        for (let y = 0; y < this.width; y++) {
          squa += c;
        }
        console.log(squa);
      }
    }
  }
}

module.exports = Square;
