#!/usr/bin/node

// prints the addition of 2 integers

function add (a, b) {
  return a + b;
}

const args = process.argv; // acessing cmd args

const a = parseInt(args[2]);
const b = parseInt(args[3]);

console.log(add(a, b));
