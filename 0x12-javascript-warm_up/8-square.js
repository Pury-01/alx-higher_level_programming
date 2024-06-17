#!/usr/bin/node

// prints a square

const args = process.argv;

const size = parseInt(args[2]);
let i = 0;
let j = 0;
let row = ''; // an empty string for the row

// check if first argument converted to integer
if (isNaN(size)) {
  console.log('Missing size');
}

// print a square
while (i < size) {
  while (j < size) {
    row += 'X'; // print 'X' character without newline
    j++;
  }
  console.log(row); // move to next line after completing row
  i++;
}
