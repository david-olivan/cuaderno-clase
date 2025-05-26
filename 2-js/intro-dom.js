
function crearMensaje(nombre) {
    return `Hola, ${nombre ? nombre : "usuario"}!!`
}

function saludar() {
    const htmlTitulo = document.getElementById("saludo")
    const htmlUserInput = document.getElementById("userInput")

    htmlTitulo.textContent = crearMensaje(htmlUserInput.value)
    htmlUserInput.value = ""
}

