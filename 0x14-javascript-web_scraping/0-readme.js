#!/usr/bin/node

const fs = require('node:fs');
const file = process.argv[2];
fs.readFile(file, 'utf-8',
  (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
