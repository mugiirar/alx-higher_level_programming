#!/usr/bin/node
const request = require('request');
const process = require('process');
const args = process.argv.slice(2);
const url = args[0];

request(url, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
