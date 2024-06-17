#!/usr/bin/node

// prints x times "C is fun"

const args = process.argv;

// convert first argument to integer
const x = parseInt(args[2]);
let i = 0;

// check if arg1 converted to an integer
if (isNaN(x)) {
  console.log('Missing number of occurences');
}

// print x times
while (i < x) {
  console.log('C is fun');
  i++;
}
