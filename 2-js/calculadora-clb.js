function calcular(numX, numY, operacion) {
    return operacion(numX, numY)
}

function mostrarResultado() {
    const x = 5
    const y = 7
    const operacion = "suma"

    switch(operacion) {
        case "suma":
            calcular(x, y, (a, b) => a + b)
            break
        case "resta":
            calcular(x, y, (a, b) => a - b)
            break
        case "multiplicación":
            calcular(x, y, (a, b) => a * b)
            break
    }
}
