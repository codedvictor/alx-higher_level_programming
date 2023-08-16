#!/usr/bin/node

const efs = require('fs');

const fileA = efs.readFileSync(process.argv[2]).toString();
const fileB = efs.readFileSync(process.argv[3]).toString();

efs.writeFileSync(process.argv[4], fileA + fileB);
