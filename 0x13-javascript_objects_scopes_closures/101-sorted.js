#!/usr/bin/node

const dict = require('./101-data').dict;
const items = [];
for (const [key, value] of Object.entries(dict)) {
  items.push([value, key]);
}
const sortedItems = items.sort();
const newDict = {};
let values = [];
for (let i = 1; i < sortedItems.length; i++) {
  if (sortedItems[i][0] === sortedItems[i - 1][0]) {
    values.push(sortedItems[i - 1][1]);
    if (sortedItems[i + 1] === undefined) {
      values.push(sortedItems[i][1]);
      newDict[sortedItems[i][0]] = values;
    }
  } else {
    values.push(sortedItems[i - 1][1]);
    newDict[sortedItems[i - 1][0]] = values;
    values = [];
    if (sortedItems[i + 1] === undefined) {
      values.push(sortedItems[i][1]);
      newDict[sortedItems[i][0]] = values;
    }
  }
}
console.log(newDict);
