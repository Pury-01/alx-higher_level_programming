#!/usr/bin/node

// computes and prints a factorial

// function to compute factorial
function factorial (n) {
  let i = 1;
  let myNumber = 1;

  while (i <= n) {
    myNumber *= i;
    i++;
  }
  return myNumber;
}

const args = process.argv;

const arg1 = parseInt(args[2]);

if (isNaN(arg1)) {
  console.log(1);
} else {
  console.log(factorial(arg1));
}
