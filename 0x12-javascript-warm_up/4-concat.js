#!/usr/bin/node
var myArgs = process.argv.slice(2);

if (myArgs[0] === undefined && myArgs[1] === undefined) {
    console.log('undefined is undefined');
} else {
    console.log(myArgs[0], "is", myArgs[1]);
}
