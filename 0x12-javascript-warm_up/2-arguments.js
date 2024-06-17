#!/usr/bin/node

// prints a message depending on number of args passed

const args = process.argv; // accessing cmd args

if (args.length < 3) {
  console.log('No argument');
} else if (args.length === 3) {
  console.log('Argument found');
} else { console.log('Arguments found'); }
