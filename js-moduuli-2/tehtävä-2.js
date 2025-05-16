'use strict';

const names = [];
const num_of_par = parseInt(prompt("How many participants will there be?"))

for (let i=1; i <= num_of_par; i++) {
  let name = prompt("Please enter the name of participant no." + i)
  names.push(name)
}

const html_list = document.querySelector('#Listofpeople');

names.sort()

for (let i = 0; i < num_of_par; i++) {
  html_list.innerHTML += `<li> ${names[i]}</li>`;
}