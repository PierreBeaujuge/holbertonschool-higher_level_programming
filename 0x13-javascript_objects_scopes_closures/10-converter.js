#!/usr/bin/node

exports.converter = function (base) {
  const func = function (val) { return val.toString(base); };
  return func;
};
