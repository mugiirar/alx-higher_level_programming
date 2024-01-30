#!/usr/bin/node
const request = require('request');
const filmUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(filmUrl, function (error, response, body) {
  if (!error) {
    const characterUrls = JSON.parse(body).characters;
    printCharacters(characterUrls, 0);
  }
});

function printCharacters (characterUrls, currentIndex) {
  request(characterUrls[currentIndex], function (error, response, body) {
    if (!error) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);

      if (currentIndex + 1 < characterUrls.length) {
        printCharacters(characterUrls, currentIndex + 1);
      }
    }
  });
}
