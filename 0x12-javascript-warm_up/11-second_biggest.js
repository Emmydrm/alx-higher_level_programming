#!/usr/bin/node

if (process.argv.length === 2) {
	console.log(0);
} else if (process.argv.length === 3) {
	console.log(0);
} else {
	const args = process.argv.slice(2);
	args.sort(function (a, b) { return b - a; });
	console.log(args[1]);
}
