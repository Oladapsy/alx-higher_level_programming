#!/usr/bin/node
/* script that searches the second biggest integer in the list of arguments. */
const args = process.argv;

if (args.length < 3) {
  console.log(0);
} else if (args.length === 3) {
  console.log(0);
} else {
  let highest = 0;
  for (let i = 2; i < args.length; i++) {
    if (parseInt(args[i]) > highest) {
      highest = parseInt(args[i]);
    }
  }
  console.log(highest);
}
