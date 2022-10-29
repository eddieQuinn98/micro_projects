// This is my first attempt at a fizzbuzz in JS, i would of prefered to use a dict to map vals to outputs but i don't know how to do that yet

function fizzbuzz(range, tests = { 3: "fizz", 5: "buzz" }) {
    for (let i = 1; i < range; i++) {
        let pstr = "";
        for (t in tests) {
            if (i % t === 0) {
                pstr += tests[t]
            }
        }
        console.log(pstr === "" ? i : pstr);

    }
}

fizzbuzz(300);