#!/usr/bin/node

// process.argv
const { argv } = require('process');


argv.forEach((val, index) => {
	console.log(`${index}: ${val}`);
});

let len = 0;
argv.forEach((val, index) => {
	len++;
});

if (len > 2) {
	if (len == 3) {
		console.log('Argument found');
	}
	else if (len > 3) {
		console.log('Arguments found');
	}
else {
	console.log('No Argument');
}
}

