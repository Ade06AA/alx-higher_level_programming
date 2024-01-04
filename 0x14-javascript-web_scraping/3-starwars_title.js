#!/usr/bin/env node

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
const request = require('request');

request(url, (err, responce, body) => {
  if (err) {
    console.error(`${err}`);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
