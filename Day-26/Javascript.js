// ==========================================================
//              JAVASCRIPT BASICS NOTES
// ==========================================================

// ----------------------------------------------------------
// 1. What is JavaScript?
//
// JavaScript (JS) is a high-level, interpreted programming
// language used to make web pages interactive.
//
// JavaScript is used for:
// - Dynamic web pages
// - Form validation
// - Animations
// - Games
// - API calls
// - DOM Manipulation
//
// HTML -> Structure
// CSS -> Styling
// JavaScript -> Functionality

// ----------------------------------------------------------
// 2. Ways to Add JavaScript

// Inline JavaScript
// <button onclick="alert('Hello')">Click</button>

// Internal JavaScript
// <script>
//     console.log("Hello");
// </script>

// External JavaScript
// <script src="script.js"></script>

// ----------------------------------------------------------
// 3. Output Methods

console.log("Hello World");

alert("Welcome!");

document.write("Hello JavaScript");

// ----------------------------------------------------------
// 4. Variables
//
// Variables store data.
//
// JavaScript has three ways to declare variables:
//
// var
// let
// const

var city = "Delhi";
let age = 21;
const PI = 3.14;

// ----------------------------------------------------------
// 5. Difference between var, let and const

// var
// - Can be redeclared
// - Can be reassigned
// - Function scoped

// let
// - Cannot be redeclared
// - Can be reassigned
// - Block scoped

// const
// - Cannot be redeclared
// - Cannot be reassigned
// - Block scoped

// ----------------------------------------------------------
// 6. Data Types

// Primitive Data Types

let name = "Kirti";       // String
let age1 = 21;            // Number
let isStudent = true;     // Boolean
let salary = null;        // Null
let x;                    // Undefined
let id = Symbol();        // Symbol
let big = 123456789n;     // BigInt

// Non-Primitive

let person = {
    name: "Kirti",
    age: 21
};

let numbers = [10, 20, 30];

// ----------------------------------------------------------
// 7. typeof Operator

console.log(typeof "Hello");     // string
console.log(typeof 25);          // number
console.log(typeof true);        // boolean

// ----------------------------------------------------------
// 8. Operators

// Arithmetic

let a = 10;
let b = 5;

console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(a / b);
console.log(a % b);

// ----------------------------------------------------------

// Assignment

let num = 5;

num += 2;
num -= 1;
num *= 3;

// ----------------------------------------------------------

// Comparison

console.log(10 == "10");
console.log(10 === "10");
console.log(10 != 20);
console.log(10 > 5);

// == checks only value
// === checks value and datatype

// ----------------------------------------------------------

// Logical

console.log(true && false);
console.log(true || false);
console.log(!true);

// ----------------------------------------------------------

// Increment / Decrement

let x1 = 5;

x1++;
x1--;

// ----------------------------------------------------------
// 9. User Input

// let name1 = prompt("Enter your name");

// alert(name1);

// ----------------------------------------------------------
// 10. Conditional Statements

let marks = 80;

if (marks >= 90) {
    console.log("Grade A");
}
else if (marks >= 70) {
    console.log("Grade B");
}
else {
    console.log("Grade C");
}

// ----------------------------------------------------------
// 11. switch Statement

let day = 2;

switch(day){

    case 1:
        console.log("Monday");
        break;

    case 2:
        console.log("Tuesday");
        break;

    default:
        console.log("Invalid");
}

// ----------------------------------------------------------
// 12. Loops

// for loop

for(let i=1;i<=5;i++){
    console.log(i);
}

// while loop

let i=1;

while(i<=5){
    console.log(i);
    i++;
}

// do while

let j=1;

do{
    console.log(j);
    j++;
}
while(j<=5);

// ----------------------------------------------------------
// 13. Functions

function greet(){

    console.log("Hello");
}

greet();

// ----------------------------------------------------------

// Function with Parameters

function add(a,b){

    return a+b;
}

console.log(add(5,10));

// ----------------------------------------------------------
// 14. Arrow Functions

const multiply = (a,b) => {

    return a*b;
};

console.log(multiply(4,5));

// ----------------------------------------------------------
// 15. Arrays

let fruits = ["Apple","Mango","Banana"];

console.log(fruits[0]);

fruits.push("Orange");

fruits.pop();

console.log(fruits.length);

// ----------------------------------------------------------
// 16. Objects

let student = {

    name:"Kirti",

    age:21,

    course:"B.Tech"
};

console.log(student.name);

// ----------------------------------------------------------
// 17. String Methods

let str = "JavaScript";

console.log(str.length);

console.log(str.toUpperCase());

console.log(str.toLowerCase());

console.log(str.substring(0,4));

console.log(str.includes("Script"));

// ----------------------------------------------------------
// 18. Array Methods

let nums = [1,2,3];

nums.push(4);

nums.pop();

nums.shift();

nums.unshift(10);

console.log(nums);

// ----------------------------------------------------------
// 19. Template Literals

let username = "Kirti";

console.log(`Welcome ${username}`);

// ----------------------------------------------------------
// 20. DOM (Document Object Model)
//
// JavaScript uses the DOM to interact with HTML.

document.getElementById("title");

document.querySelector(".box");

document.querySelectorAll("p");

// ----------------------------------------------------------
// 21. Changing HTML Content

document.getElementById("demo").innerHTML = "Hello";

// ----------------------------------------------------------
// 22. Changing CSS

document.getElementById("demo").style.color = "red";

// ----------------------------------------------------------
// 23. Events

// Button click

// button.onclick = function(){
//      console.log("Clicked");
// }

// ----------------------------------------------------------

// addEventListener

// button.addEventListener("click", function(){
//      console.log("Clicked");
// });

// ----------------------------------------------------------
// 24. Common Events

// click
// mouseover
// mouseout
// keydown
// keyup
// submit
// change
// input

// ----------------------------------------------------------
// 25. JavaScript Comments

// Single Line Comment

/*

Multi-line Comment

*/

// ----------------------------------------------------------
// 26. Common Interview Questions

// Q1. Difference between let and var?
//
// var:
// Function scoped
// Can be redeclared
//
// let:
// Block scoped
// Cannot be redeclared

// ----------------------------------------------------------

// Q2. Difference between == and ===?
//
// ==
// Compares value only.
//
// ===
// Compares value and datatype.

// ----------------------------------------------------------

// Q3. Difference between null and undefined?
//
// null
// Intentionally empty value.
//
// undefined
// Variable declared but not assigned.

// ----------------------------------------------------------

// Q4. What is JavaScript?
//
// A scripting language used to create dynamic web pages.

// ----------------------------------------------------------

// Q5. What is DOM?
//
// DOM is the Document Object Model.
// It allows JavaScript to access and modify HTML.

// ----------------------------------------------------------

// Q6. What is an Arrow Function?
//
// A shorter syntax for writing functions.

// ----------------------------------------------------------
// 27. Quick Revision

// Variable

let age = 21;

// Function

function greet(){}

// Arrow Function

const add = (a,b) => a+b;

// Array

let arr = [1,2,3];

// Object

let obj = {
    name:"Kirti"
};

// If

if(condition){}

// Loop

for(let i=0;i<5;i++){}

// DOM

document.getElementById()

document.querySelector()

// Event

addEventListener()

// ----------------------------------------------------------
// Summary
//
// JavaScript is used to make web pages interactive.
// It supports variables, data types, operators, loops,
// functions, arrays, objects, DOM manipulation, and events.
// Together with HTML and CSS, JavaScript forms the core of
// front-end web development.