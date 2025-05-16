'use strict';

let nums = []


while (true){
   const num = parseInt(prompt("Please enter numbers, or enter a number you have already submitted to quit."))

   if (nums.includes(num)) break; {
      nums.push(num)
  }
}

alert("You have already submitted that number, please check the console to see the numbers you entered.")
nums.sort((a,b) => a-b)

for (let i = 0; i < nums.length; i++) {
  console.log(nums[i])
}