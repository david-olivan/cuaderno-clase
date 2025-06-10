function ejemploCallback(data) {
    console.log(data)
}

function ejemploCallback2(data) {
    console.log("Hola " + data)
}

function ejemploLlamador(texto, callback) {
    callback(texto)
}



ejemploLlamador("David", ejemploCallback)
ejemploLlamador("David", ejemploCallback2)
ejemploLlamador("David", (data) => console.log(data + ": Esto no ha funcionado"))