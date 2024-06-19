#!/usr/bin/node

/**
 * class square that defines a square and inherits from Square
 * class
 *
 * creates an instance method charPrint(c) that prints the
 * rectangle using character c
 * if c is undefined, character X is used
 */

const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}

module.exports = Square;
