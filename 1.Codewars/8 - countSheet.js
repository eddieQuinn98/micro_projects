// KATA-LINK: https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/solutions/javascript
// DATE: 24/10/22
//
// I think i could of used a switch case here instead, will update in future

function countSheep (num) {
    let return_str = "";
    for (let i=0; i< num; i++){
      return_str += i+1 + " sheep...";
    }
    return return_str;
  }

console.log(countSheep(3));