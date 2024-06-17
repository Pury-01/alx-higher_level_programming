#!/usr/bin/node

// prints the first argument passed to it

// accessing comand line arguments
const args = process.argv;

const arg1 = args[2];

// check if any argument is passed
if (!arg1) {
  console.log('No argument');
} else {
  console.log(arg1);
}
