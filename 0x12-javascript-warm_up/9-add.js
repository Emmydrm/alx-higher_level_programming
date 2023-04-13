#!/usr/bin/node

function add (a, b) {
	console.log(a + b);
}
if (isNaN(process.argv[2])) {
	console.log('NaN');
} else if (isNaN(process.argv[3])) {
	console.log('NaN');
} else {
	add(parseInt(process.argv[2]), parseInt(process.argv[3]));
}
