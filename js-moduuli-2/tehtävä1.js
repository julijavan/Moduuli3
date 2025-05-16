const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let numbers = [];
let count = 0;

function kysyNumero() {
    rl.question(`Annappas numero bro ${count + 1}: `, (input) => {
        numbers.push(parseFloat(input));
        count++;

        if (count < 5) {
            kysyNumero();
        } else {
            console.log("Numerosi in reverse:");
            for (let i = numbers.length - 1; i >= 0; i--) {
                console.log(numbers[i]);
            }
            rl.close();
        }
    });
}

kysyNumero();