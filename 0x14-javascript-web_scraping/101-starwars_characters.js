#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + movieID, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonData = JSON.parse(body);
    jsonData.characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
