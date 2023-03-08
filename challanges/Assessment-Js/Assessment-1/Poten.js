let giraffen = Number(prompt("Hoeveel Giraffen zijn er geteld? "))
let struisvogel = Number(prompt("Hoeveel Struisvogels zijn er geteld? "))
let zebra = Number(prompt("Hoeveel Zebras zijn er geteld? "))

function potenbereken(a, b, c){
    a = a * 4
    b = b * 2
    c = c * 4
    return a + b + c;
}
console.log(potenbereken(giraffen, struisvogel, zebra))