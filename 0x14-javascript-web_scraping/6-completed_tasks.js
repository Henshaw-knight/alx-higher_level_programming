#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
// 'https://jsonplaceholder.typicode.com/todos';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonData = JSON.parse(body);
    const result = {};
    for (let i = 0; i < jsonData.length; i++) {
      if (jsonData[i].completed === true) {
        const formattedID = (jsonData[i].userId).toString();
        if (formattedID in result) {
          result[formattedID] = result[formattedID] + 1;
        } else {
          result[formattedID] = 1;
        }
      }
    }
    console.log(result);
  }
});
