// KATA-LINK: https://www.codewars.com/kata/57a429e253ba3381850000fb/train/javascript
// DATE: 22/10/22
//
// I think i could of used a switch case here instead, will update in future


function bmi(weight, height) {

    let bmi_ = weight / (height ** 2);

    if (bmi_ <= 18.5) {
        return "Underweight";
    }
    else if (bmi_ <= 25.0) {
        return "Normal";
    }
    else if (bmi_ <= 30.0) {
        return "Overweight";
    }
    else {
        return "Obese";
    }
}

console.log(bmi(80, 1.80));