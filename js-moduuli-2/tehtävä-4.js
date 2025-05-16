const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let numbers = [];

function askNumber() {
    rl.question("Syötä numero! 0 päättää kyselyn: ", (input) => {
        let num = parseFloat(input);

        if (num === 0) {
            numbers.sort((a, b) => b - a); // Sort descending
            console.log("Numerosi suurimmasta pienimpään:");
            console.log(numbers);
            rl.close();
        } else {
            numbers.push(num);
            askNumber(); // Keep asking
        }
    });
}

askNumber();