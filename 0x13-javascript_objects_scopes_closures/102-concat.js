#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

function concatFiles (file1, file2, outputFile) {
  const content1 = fs.readFileSync(file1, 'utf8');
  const content2 = fs.readFileSync(file2, 'utf8');
  const concatenatedContent = content1 + content2;

  fs.writeFileSync(outputFile, concatenatedContent, 'utf8');
}

concatFiles(args[2], args[3], args[4]);
