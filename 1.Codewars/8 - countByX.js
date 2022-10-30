// KATA LINK: https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/javascript
// DATE: 27/10/22

function countBy(x, n) {
  let z = [];
  for (let i = 1; i < (n + 1); i++) {
    z.push(x * i);
  }
  return z;
}

console.log(countBy(2, 10));