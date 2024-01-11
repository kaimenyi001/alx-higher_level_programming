#!/usr/bin/node
// Concat two files

const fls = require('fls');

const file1 = fls.readFileSync(process.argv[2]).toString();
const file2 = fls.readFileSync(process.argv[3]).toString();
fls.writeFileSync(process.argv[4], file1 + file2);
