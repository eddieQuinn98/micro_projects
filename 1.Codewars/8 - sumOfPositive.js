// KATA Link: https://www.codewars.com/kata/5715eaedb436cf5606000381/solutions/javascript
// Date: 26/10/22

function positiveSum(arr) {
  let sum = 0;
  for(let x of arr){
    if (Math.sign(x) == -1) {
        continue;
    }
    sum = sum + x;
  }
  return sum;
}

console.log(positiveSum([1,2,3,4,5]));