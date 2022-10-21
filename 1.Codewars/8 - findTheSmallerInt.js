// ORIGINAL KATA: "https://www.codewars.com/kata/55a2d7ebe362935a210000b2/solutions/javascript"
// DATE: 21-10-22
//
// First time i did an iterable in JS - Code is a bit scuffed, i rly would of like to have not cone the whole sv=null, but idk how to avoid it atm


function findSmallestInt(args) {
    let sv = null;
    for (let i in args) {
        if (sv === null) {
            sv = args[i];
        }
        else if (sv > args[i]) {
            sv = args[i];
        }
    }
    return sv;
}

let p = [78, 56, 232, 12, 8];
p = findSmallestInt(p);
console.log(p);

