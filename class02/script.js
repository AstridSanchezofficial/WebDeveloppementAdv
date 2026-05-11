console.log("Starts");
console.log("Middle");

//WE COULD USE  setTimeout() , to run the code
//After certain amount of time 

setTimeout(()=>{
    console.log("This is appearing after 100 seconds")
}, 1000); //

console.log("This has not SetTimeout");

//CALLBACK FUNCTION -->We have to pase the function as an argument  to the doSomething function

function doSomethingLater(callback){
    console.log("Doing set up");
    console.log("Preparing");
    callback()
};

doSomethingLater(()=>{
    console.log("Nice to meet you");
});

/**
* Exercise
*/

// 1. load in DOM elements

// nameinput

// greet button
// output

// 2. add an event listener to the button
const button=document.getElementById("great_button");
const input=document.getElementById("nameInput");
const output=document.querySelector("#output");

button.addEventListener("click",()=>{
    const inputValue=input.value.trim();
    

});

// continuation function for it should be:

// 1. take the input value and trim it

// 2. (condition)
// validate that the input is not an empty string
// if it is --> update output text to :
//                  Please enter something

// 3. after 1000ms , update the output with:
//                  Hello, INPUT_VALUE
 