#!/usr/bin/node

// converts argument to integer and if it does it prints it

const args = process.argv;

// convert first argument to int
const myNumber = parseInt(args[2]);

// check if argument is a number
if (isNaN(myNumber)) {
  console.log('Not a number');
} else {
  console.log('My number:' + ' ' + (myNumber));
}
