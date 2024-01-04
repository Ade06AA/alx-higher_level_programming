#!/usr/bin/env node

const fs = require('node:fs');
const name = process.argv[2];
const content = process.argv[3];
fs.writeFile(name, content,
  err => {
    if (err) console.error(err);
  });
