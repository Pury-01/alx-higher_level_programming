#!/usr/bin/node

/**
 * class square that defines a square
 * it inherits from class Rectangle
 */

const Rectangle = require('./4-rectangle');

class square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = square;
