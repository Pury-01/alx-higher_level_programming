#!/usr/bin/node

// prints three lines using an array of string and a loop

const languages = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

let i = 0;

while (i < languages.length) {
  console.log(languages[i]);
  i++;
}
