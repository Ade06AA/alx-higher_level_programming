#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

// this request object is a non blocking process 
// that is while geting the request the code can continue running
// and when it finish geting the request it can call the function passed to it as the second argument
request(url, (err, responce, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${responce.statusCode}`);
  }
  // console.log(`body: ${body}`);
});
