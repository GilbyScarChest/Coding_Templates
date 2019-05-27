//// 1) variables, data types, if/else statements ////
let example1 = "a";
var example2 = "1";
let x = 1;
var y = 10;
const z = 2; // a constant cannot be changed later.

example2 === "1"; // === means value AND data type are equal.
example2 !== 1;  // !== means value AND data type are Not equal.

if (example1 == "a") {
	console.log("example1 is a!")
} else if (example1 == "b") {
	console.log("example1 is b!")
} else {
	console.log("example1 is something else")
};

// AND and OR.
if (x === 1 && y === 10){
	console.log('both of these values are true')
};

if (x === 1 || y === 10){
	console.log('one of these values is true')
};

// Combine strings and variables
console.log(`example1 is ${example1}, and example2 is ${example2}.`)




//// 2) loops ////
// For loops
for (i = 0; i < 10; i++) {
	console.log(i);
}

for (i = 0; i < myArray.length; i++) {
	console.log(i);
}

for (stuff in myArray) {
	console.log(myArray[stuff]); //almost like python
}

// While loops
while (i < 10) {
  text += "The number is " + i;
  i++;
}

// Map/forEach
var princesses = [
  { name: "Rapunzel", age: 18 },
  { name: "Mulan", age: 16 },
  { name: "Anna", age: 18 },
  { name: "Moana", age: 16 }
];

princesses.map(princess => princess.name);
princesses.forEach(princess => princess.name);

princesses.map(function(princess){
  return princess.name;
};
princesses.forEach(function(princess){
  return princess.name;
};

var theStagesOfJS = ["confidence", "sadness", "confusion", "realization", "debugging", "satisfaction"];

var mapArrayWithIndex = theStagesOfJS.map(function(item, index){
  return `${item} ${index}`;
});

// Map/Filter
princesses.map(princess => princess.name).filter(name => name.length < 5);




//// 3) arrays ////
let myFirstArray = ['a', 'b', 'c', 5];

// console.log(myFirstArray)
// console.dir(myFirstArray)

// get by element
var firstElement = myFirstArray[0]
var secondElement = myFirstArray[1]

console.log(`${firstElement}, ${secondElement}`)

myFirstArray.push('Tyler') // push to the back of array.

console.log(myFirstArray.slice(1)) // give me element [1] till the end.
console.log(myFirstArray.slice(1,4)) // give me element [1]:[4].
console.log(myFirstArray.slice(-2)) // give me 2 from the end.

var arrayAsString = myFirstArray.join(';') // join items in list by ";" into one string.
var backToArray = myFirstArray.split(';') // split string into list on ";"

console.log(arrayAsString[0]) // first letter of string




//// 4) functions ////
// Simple log statement
function printHello() {
  console.log("Hello there!");
}

// Takes two numbers and adds them
function addition(a, b) {
  return a + b;
}

// Run the code in the `printHello` function
printHello();

// Log results of addition function
console.log(addition(44, 50));

// This function accepts a parameter and iterates through an array
function listLoop(userList) {
  for (var i = 0; i < userList.length; i++) {
    console.log(userList[i]);
  }
}

var friends = ["Sarah", "Greg", "Cindy", "Jeff"];
listLoop(friends);

// Functions can call other functions
function doubleAddition(c, d) {
  var total = addition(c, d) * 2;

  return total;
}

// Log results of doubleAddition function
console.log(doubleAddition(3, 4));


// Javascript built in functions
var longDecimal = 112.34534454;
var roundedDecimal = Math.floor(longDecimal);
console.log(roundedDecimal);