#!/usr/bin/node
const FirstSquare = require('./5-square');

class Square extends FirstSquare {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      if (c === undefined) {
        console.log('X'.repeat(this.width));
      } else {
        console.log(`${c}`.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
