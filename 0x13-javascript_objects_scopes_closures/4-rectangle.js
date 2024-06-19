#!/usr/bin/node

/**
 * class Rectangle that defines a rectangle
 *
 * creates an empty object if w or h is <= 0
 * create instance method print() that prints rectangle
 * using X character
 *
 * create instance method rotate() that exchanges the width
 * and height of rectangle
 * create instance method double() that multiples the width
 * and height of the rectangle
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
