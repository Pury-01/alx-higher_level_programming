#!/usr/bin/node

/**
 * class Rectangle that defines a rectangle
 *
 * create an empty object if w or h <= 0
 * create instance method print() to print rectangle
 * using X character
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;

    if (this.width && this.height) {
      for (i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}

module.exports = Rectangle;
