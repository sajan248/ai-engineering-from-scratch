// Lesson: Dev Environment (phase 00 / lesson 01)
// Path: phases/00-setup-and-tooling/01-dev-environment/docs/en.md
// Description: TypeScript Hello World demonstrating Node.js and TypeScript runner availability.

import process from "node:process";

function main() {
  console.log("Hello World from TypeScript / Node.js!");
  console.log(`Node.js Version: ${process.version}`);
  console.log(`Platform: ${process.platform}`);
}

main();
