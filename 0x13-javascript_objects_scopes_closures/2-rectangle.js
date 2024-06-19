#!/usr/bin/node

/**
 * class Rectangle that defines a rectangle
 *
 * creates an empty object if the values are <= 0
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
