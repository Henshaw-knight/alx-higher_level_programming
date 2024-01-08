#!/usr/bin/node
const firstArg = parseInt(process.argv[2]);

if (Number.isInteger(firstArg)) {
  let i = 1;
  while (i <= firstArg) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
