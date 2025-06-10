function suma(a, b) {
    return a + b
}

function resta(a, b) {
    return a - b
}

function multiplicacion(a, b) {
    return a * b
}

function mostrarResultado() {
    const x = 5
    const y = 7
    const operacion = "suma"

    switch(operacion) {
        case "suma":
            suma(x, y)
            break
        case "resta":
            resta(x, y)
            break
        case "multiplicación":
            multiplicacion(x, y)
            break
    }
}

console.log(mostrarResultado())