#!/usr/bin/node

// searches the second biggest integer in arguments list

const args = process.argv;
let num;
let secMax = 0;
let max = 0;

if (args <= 3) {
  console.log(0); // print 0 if 0 or 1 argument given
} else {
  const nums = args.map(Number); // convert elements to integers

  // compare numbers in list to find second largest
  for (num of nums) {
    if (num > max) {
      secMax = max;
      max = num;
    } else if (num > secMax && num !== max) {
      secMax = num;
    }
  }
  console.log(secMax);
}
