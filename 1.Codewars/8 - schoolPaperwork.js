// KATA LINK - https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd/solutions/javascript
// Date - 14/11/22
//
// This could of been handled more eleganly, i could of used a turney operator to do the whole thing in one line. I also
// didn't need the Math module

function paperwork(n, m) {
    if (Math.sign(n) < 0 || Math.sign(m) < 0) {
        return 0;
    }
    return n * m;
}

console.log(paperwork(5, 5));