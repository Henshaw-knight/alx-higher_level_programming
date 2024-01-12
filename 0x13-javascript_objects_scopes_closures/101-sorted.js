#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};

for (const key in dict) {
  const keyValue = String(dict[key]);

  if (!(keyValue in newDict)) {
    newDict[keyValue] = [String(key)];
  } else {
    const value = newDict[keyValue];
    value.push(String(key));
    newDict[keyValue] = value;
  }
}

console.log(newDict);
