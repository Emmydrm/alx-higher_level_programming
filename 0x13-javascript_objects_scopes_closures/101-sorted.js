#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const key in dict) {
	function array (value) {
		const list = [];
		for (const item in dict) {
			if (dict[item] === value) {
				list.push(item);
			}
		}
		return list;
	}
	const value = dict[key];
	newDict[value.toString()] = array(value);
}
console.log(newDict);
