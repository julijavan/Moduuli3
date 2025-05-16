'use strict';

let nub = 1
let num_lst = []


while (nub !== 0) {
  nub = parseInt(prompt("Please enter numbers, or enter a 0 to quit."))
  num_lst.push(nub)
}

num_lst.sort((b,a) => b-a);
num_lst.reverse()

for (let i = 0; i <num_lst.length; i++ ) {
  console.log(num_lst[i])
}