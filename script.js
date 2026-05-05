console.log("Hello World")


let number= 10
console.log(number)


// We cannot change the value of the constant 
const courseTeacher= "Keymar";
console.log(courseTeacher);
//


//In this case an array is assigned to const grades 
//We cannot change the GRADES ITSELF 
//But we can manipulate the array

const grades= [80, 90, 100];
grades.push(60);
console.log(grades)

//

//3. BLOCK SCOPE

a=5

if(a==5){
    let message= "You guessed the number right";
    console.log(message);
}

//

function showUser(){
    const username="Mina";
    console.log(`${username} is logged in`);
}

showUser()

// WARNING
//console.log(user); -> Will not work because USERNAME is in the function's scope and not accessible

//4. LET OR CONST

let page=1; //page can change
const maxItems= 20;//maxITEMS could not change cause is the max ammount that we will be able to add
const categories=["movies", "books"];// IT IS A CONTS BECAUSE.... 

//THIS IS A RETURN FUNCTION
function add(a,b){
    return a+b;
}

//**MINI EXERCISE */

const Name= "Jane"
const lastName= "Doe"


//1. WRITE A RETURN FUNCTION THAT ADDS A NAME AND LASTNAME AND RETURNS IT TO FULLNAME
function createName(Name,lastName){
    return (`${Name} ${lastName}`);

}

//Define the function fullName
const fullName= createName(Name, lastName)

//2. WRITE A FUNCTION THAT GREETS  the user calling their FULLname

function greeting(fullName){
    console.log(`Hello ${fullName}`);
}

greeting(fullName);



// END OF THE EXERCISE


//ADD SOLUTION 2

///


// ONE RESPONSABILITY PER FUNCTION//
function calculateTotal(price, quantity){
    return price * quantity;
}

function formatPrice(amount){
    return "$" + amount.toFixed(2);
}

const totalPrice=calculateTotal(20,4)
console.log(totalPrice);
console.log(formatPrice(totalPrice)) 

//

// LOOPS

//FIND FUNCTION -->Finds the first ocurrence that passes the condition//


const prices= [10, 20, 30, 40];
const firstBigPrice= prices.find(function(price){
    return price > 25;
});

//MAP FUNCTION  --> Transforms each element of the array and stores it in a new array



//OBJECTS 

const products = {
    name: "Keyboard",
    price: 49.98,
    inStock:true,
    describe:function(){
        
    }

}
