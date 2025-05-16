'use strict';


const nums = [];


let rep = 0

while (rep<5){
  const num = parseInt(prompt("Please enter a number"))
  nums.push(num)
  rep ++
}

for (let i = 4; i >= 0; i--) {
        console.log(`number ${i+1}: ${nums[i]}`);
}