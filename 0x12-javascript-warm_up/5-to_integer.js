#!/usr/bin/node
var myArgs = process.argv.slice(2);

if (isNaN(myArgs[0])) {
    console.log('Not a number');
} else {
    console.log("My number:", parseInt(myArgs[0]));
}
