#!/usr/bin/node
let count = 1;
exports.callMeMoby = function (x, theFunction) {
  while (count <= x) {
    theFunction();
    count++;
  }
};
