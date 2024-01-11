#!/usr/bin/node
const reversedList = [];

exports.esrever = function (list) {
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return (reversedList);
};
