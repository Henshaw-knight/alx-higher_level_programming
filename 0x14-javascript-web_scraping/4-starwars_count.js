#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
// 'https://swapi-api.alx-tools.com/api/films/';
const id = '18';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonData = JSON.parse(body);
    let count = 0;
    for (const result of jsonData.results) {
      for (const character of result.characters) {
        const strArray = character.split('/');
        if (strArray[strArray.length - 2] === id) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
