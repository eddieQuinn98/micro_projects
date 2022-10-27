// This is my first attempt at a fizzbuzz in JS, i would of prefered to use a dict to map vals to outputs but i don't know how to do that yet

function fizzbuzz(range) {

    for (let i = 1; i < range; i++) {
        let pstr = "";
        if (i % 3 === 0) {
            pstr += "fizz";
        }
        if (i % 5 === 0) {
            pstr += "buzz";
        }
        console.log(pstr === "" ? i : pstr);
    }
}

fizzbuzz(300);