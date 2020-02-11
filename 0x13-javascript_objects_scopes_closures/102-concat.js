#!/usr/bin/node

const fs = require('fs');

let myArray = process.argv.slice(2);

fs.readFile(myArray[0], (err, data_to_append) => {
    if (err) throw err;
    fs.appendFile(myArray[2], data_to_append, (err) => {
	if (err) throw err;
    });
});
fs.readFile(myArray[1], (err, data_to_append) => {
    if (err) throw err;
    fs.appendFile(myArray[2], data_to_append, (err) => {
	if (err) throw err;
    });
});
