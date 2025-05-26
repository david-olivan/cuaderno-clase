
function suma() {
    let x = Number(prompt("X: "))
    let y = Number(prompt("Y: "))
    console.log("Suma: " + (x + y))
}

function suma_return() {
    let x = Number(prompt("X: "))
    let y = Number(prompt("Y: "))

    return x + y
}

function suma_arg_return(x, y) {
    return x + y
}
