#!/usr/bin/node
let num = 0;
module.exports.logMe = function (item) {
	console.log(num + ': ' + item);
	num++;
};
