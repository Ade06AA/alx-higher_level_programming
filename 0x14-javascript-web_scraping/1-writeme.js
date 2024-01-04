#!/usr/bin/node

const fs = require('node:fs');
const name = process.argv[2];
const content = process.argv[3];
fs.writeFile(name, content, 'utf-8',
  err => {
    if (err) {
      console.log(err);
    }
  });
