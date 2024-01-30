#!/usr/bin/node

const request = require('request');
const process = require('process');

const filmId = process.argv[2];

request.get('https://swapi-api.hbtn.io/api/films/' + filmId + '/', function (error, response, responseBody) {
  if (error) {
    console.log(error);
  } else {
    const filmData = JSON.parse(responseBody);
    
    for (const characterUrl of filmData.characters) {
      request.get(characterUrl, function (error, res, characterBody) {
        const characterData = JSON.parse(characterBody);
        if (error) {
          console.log(error);
        } else {
          console.log(characterData.name);
        }
      });
    }
  }
});
