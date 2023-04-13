#!/usr/bin/node

const args = process.argv;

if (process.argv[2] == null) {
	console.log('No argument');
} else {
	console.log(process.argv[2]);
}
