#!/usr/bin/node

const myArray = process.argv.slice(2);
const request = require('request');

request(myArray[0], function (error, response, body) {
  if (error) console.error('error:', error); // Print the error if one occurred
  const results = JSON.parse(body).results;
  let count = 0;
  results.forEach(dict => { if (dict.characters.includes('https://swapi.co/api/people/18/')) { count++; } });
  console.log(count);
});
