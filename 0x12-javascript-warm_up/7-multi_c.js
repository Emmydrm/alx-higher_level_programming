#!/usr/bin/node

const param = process.argv[2];
if (!isNaN(param)) {
	for (let i = 0; i < param; i++) {
		console.log('C is fun');
	}
} else {
	console.log('Missing number of occurrences');
}
