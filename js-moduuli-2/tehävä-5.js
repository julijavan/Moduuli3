const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let numbers = [];

function askNumber() {
    rl.question("Anna numero: ", (input) => {
        let num = parseFloat(input);

        if (numbers.includes(num)) {
            console.log(`Numero ${num} on syötetty jo. Lopetan kyselyn.`);
            numbers.sort((a, b) => a - b);
            console.log("Numerosi:");
            console.log(numbers);
            rl.close();
        } else {
            numbers.push(num);
            askNumber();
        }
    });
}

askNumber();