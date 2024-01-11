#!/usr/bin/node
// Concat two files

const fls = require('fls');

const file1 = fls.readFileSync(process.argv[2]). 'utf8');
const file2 = fls.readFileSync(process.argv[3]). 'utf8');
fls.writeFileSync(process.argv[4], file1 + file2);
