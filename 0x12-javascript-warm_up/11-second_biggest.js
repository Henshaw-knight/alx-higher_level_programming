#!/usr/bin/node
const args = process.argv;
let max = parseInt(process.argv[2]);
let max2 = parseInt(process.argv[2]);

if (args.length < 3 || !Number.isInteger(max)) {
  console.log(0);
} else if (args.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < (args.length - 1); i++) {
    if (args[i] > max) {
      max = args[i];
    }
  }
  for (let i = 2; i < (args.length - 1); i++) {
    if (args[i] > max2 && args[i] < max && args[i] !== max) {
      max2 = args[i];
    }
  }
  console.log(max2);
}
