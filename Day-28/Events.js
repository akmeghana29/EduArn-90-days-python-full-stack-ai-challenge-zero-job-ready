// ==========================================================
//                 JAVASCRIPT EVENTS NOTES
// ==========================================================

// ----------------------------------------------------------
// 1. What are Events?
//
// Events are actions or occurrences that happen in the browser.
//
// JavaScript can detect these events and execute code in
// response to them.
//
// Examples:
// - Clicking a button
// - Typing in a textbox
// - Submitting a form
// - Moving the mouse
// - Pressing a key
// - Loading a webpage

// ----------------------------------------------------------
// 2. Why are Events Used?
//
// Events make web pages interactive.
//
// They allow users to:
// - Click buttons
// - Fill forms
// - Play games
// - Navigate websites
// - Trigger animations
// - Validate inputs

// ----------------------------------------------------------
// 3. Event Handling
//
// Event Handling means writing JavaScript code that executes
// when an event occurs.

// ----------------------------------------------------------
// 4. Ways to Add Events

// Method 1: Inline Event (Not Recommended)

// <button onclick="showMessage()">Click</button>

// ----------------------------------------------------------

// Method 2: Using onclick Property

let button = document.getElementById("btn");

button.onclick = function () {
    console.log("Button Clicked");
};

// ----------------------------------------------------------

// Method 3: addEventListener() (Recommended)

button.addEventListener("click", function () {
    console.log("Button Clicked");
});

// Advantages:
// - Multiple event handlers
// - Cleaner code
// - Easy to remove events

// ----------------------------------------------------------
// 5. Common Mouse Events

// click
// Fired when the element is clicked.

button.addEventListener("click", function () {
    console.log("Clicked");
});

// ----------------------------------------------------------

// dblclick
// Fired when double-clicked.

button.addEventListener("dblclick", function () {
    console.log("Double Click");
});

// ----------------------------------------------------------

// mouseover
// Fired when mouse enters the element.

button.addEventListener("mouseover", function () {
    console.log("Mouse Over");
});

// ----------------------------------------------------------

// mouseout
// Fired when mouse leaves the element.

button.addEventListener("mouseout", function () {
    console.log("Mouse Out");
});

// ----------------------------------------------------------

// mousedown
// Fired when mouse button is pressed.

button.addEventListener("mousedown", function () {
    console.log("Mouse Down");
});

// ----------------------------------------------------------

// mouseup
// Fired when mouse button is released.

button.addEventListener("mouseup", function () {
    console.log("Mouse Up");
});

// ----------------------------------------------------------
// 6. Keyboard Events

let input = document.getElementById("name");

// keydown
// Fires when a key is pressed.

input.addEventListener("keydown", function () {
    console.log("Key Pressed");
});

// ----------------------------------------------------------

// keyup
// Fires when key is released.

input.addEventListener("keyup", function () {
    console.log("Key Released");
});

// ----------------------------------------------------------

// keypress (Deprecated)
// Earlier used to detect character keys.

// ----------------------------------------------------------
// 7. Form Events

let form = document.getElementById("myForm");

// submit

form.addEventListener("submit", function (event) {

    event.preventDefault();

    console.log("Form Submitted");
});

// ----------------------------------------------------------

// change
// Triggered when value changes and loses focus.

input.addEventListener("change", function () {
    console.log("Value Changed");
});

// ----------------------------------------------------------

// input
// Triggered whenever user types.

input.addEventListener("input", function () {
    console.log(input.value);
});

// ----------------------------------------------------------

// focus
// Fired when input gains focus.

input.addEventListener("focus", function () {
    console.log("Focused");
});

// ----------------------------------------------------------

// blur
// Fired when input loses focus.

input.addEventListener("blur", function () {
    console.log("Lost Focus");
});

// ----------------------------------------------------------
// 8. Window Events

// load
// Fired after the webpage is fully loaded.

window.addEventListener("load", function () {
    console.log("Page Loaded");
});

// ----------------------------------------------------------

// resize
// Fired when browser window changes size.

window.addEventListener("resize", function () {
    console.log("Window Resized");
});

// ----------------------------------------------------------

// scroll
// Fired while scrolling.

window.addEventListener("scroll", function () {
    console.log("Scrolling");
});

// ----------------------------------------------------------
// 9. Event Object

button.addEventListener("click", function (event) {

    console.log(event);

});

// The event object contains information such as:
// - event.target
// - event.type
// - event.clientX
// - event.clientY
// - event.key

// ----------------------------------------------------------
// 10. event.target

button.addEventListener("click", function (event) {

    console.log(event.target);

});

// Returns the element that triggered the event.

// ----------------------------------------------------------
// 11. event.type

button.addEventListener("click", function (event) {

    console.log(event.type);

});

// Output:
// click

// ----------------------------------------------------------
// 12. event.preventDefault()

// Prevents the browser's default behavior.

form.addEventListener("submit", function (event) {

    event.preventDefault();

});

// Example:
// Prevent page refresh after form submission.

// ----------------------------------------------------------
// 13. event.stopPropagation()

// Stops event bubbling.

button.addEventListener("click", function (event) {

    event.stopPropagation();

});

// ----------------------------------------------------------
// 14. Event Bubbling
//
// Event travels from child element
// to parent element.
//
// Example:
//
// Button
// ↓
// Div
// ↓
// Body

// ----------------------------------------------------------
// 15. Event Delegation
//
// Instead of adding listeners to every child,
// add one listener to the parent.

let list = document.getElementById("list");

list.addEventListener("click", function (event) {

    console.log(event.target);

});

// Useful for dynamic elements.

// ----------------------------------------------------------
// 16. Removing Event Listeners

function greet() {

    console.log("Hello");
}

button.addEventListener("click", greet);

// Remove Listener

button.removeEventListener("click", greet);

// ----------------------------------------------------------
// 17. Anonymous Function Example

button.addEventListener("click", function () {

    console.log("Anonymous Function");

});

// Cannot be removed later because it has no reference.

// ----------------------------------------------------------
// 18. Arrow Function Example

button.addEventListener("click", () => {

    console.log("Arrow Function");

});

// ----------------------------------------------------------
// 19. Common Interview Questions

// Q1. What is an event?
//
// An action or occurrence detected by JavaScript.

// ----------------------------------------------------------

// Q2. What is event handling?
//
// Executing JavaScript code when an event occurs.

// ----------------------------------------------------------

// Q3. Difference between onclick and addEventListener()?
//
// onclick
// - One handler only
//
// addEventListener()
// - Multiple handlers allowed
// - More flexible
// - Recommended

// ----------------------------------------------------------

// Q4. What is event bubbling?
//
// Events propagate from child elements to parent elements.

// ----------------------------------------------------------

// Q5. What is event delegation?
//
// Attaching a single event listener to a parent
// to handle events for multiple child elements.

// ----------------------------------------------------------

// Q6. What does preventDefault() do?
//
// Stops the browser's default action.

// ----------------------------------------------------------

// Q7. What does stopPropagation() do?
//
// Stops event bubbling.

// ----------------------------------------------------------
// 20. Quick Revision

// Add Event

element.addEventListener("click", function(){});

// Mouse Events

click

dblclick

mouseover

mouseout

mousedown

mouseup

// Keyboard Events

keydown

keyup

// Form Events

submit

change

input

focus

blur

// Window Events

load

resize

scroll

// Event Object

event.target

event.type

event.preventDefault()

event.stopPropagation()

// Remove Event

removeEventListener()

// ----------------------------------------------------------
// Summary
//
// JavaScript events allow web pages to respond to user
// interactions such as clicks, typing, scrolling, and form
// submissions. Event handling is commonly implemented using
// addEventListener(), which provides a flexible and efficient
// way to build interactive web applications.