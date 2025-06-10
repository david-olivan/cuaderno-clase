let progreso = 0

const intervalId = setInterval(() => {
    progreso += 1
    console.log("Progreso:", "*".repeat(progreso))

    if (progreso === 10) {
        console.log("Página cargada")
        clearInterval(intervalId)
    }
}, 500)