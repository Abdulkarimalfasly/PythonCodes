function giveMeSomething(a) {
    // Start by creating the string "something"
    let result = "something";

    // Now add a space between "something" and the argument passed (a)
    result += " " + a;

    // Finally, return the result
    return result;
}

// Test the function with some examples:
console.log(giveMeSomething("is better than nothing"));  // Output: "something is better than nothing"
console.log(giveMeSomething("Bob Jane"));  // Output: "something Bob Jane"
console.log(giveMeSomething("something"));  // Output: "something something"
