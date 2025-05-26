const tareasPendientes = ["Crear tareas", "Hacer ejemplo"]
const tareasCompletadas = []
const textoMenu = `
            ¿Qué quieres hacer?
            ===============================
            1. Crear nueva tarea (Escribe 1)
            2. Mostrar todas las tareas (Escribe 2)
            3. Marcar tarea como completada (Escribe 3)
            4. Contar tareas pendientes (Escribe 4)
            5. Salir de la applicación (Escribe 5)
            `

function main() {
    let funcionando = true

    while (funcionando) {
        const userInput = prompt(textoMenu)

        switch (userInput) {
            case "1":
                crearTarea()
                break
            case "2":
                mostrarTareas()
                break
            case "3":
                marcarTareaCompleta()
                break
            case "4":
                contarTareasPendientes()
                break
            case "5":
                funcionando = false
                break
            default:
                alert("Esa opción no es válida")
                break
        }
    }
    return 0;
}

// Crear nueva tarea
function crearTarea() {
    const tarea = prompt("Escribe el nombre de la tarea: ")
    if (tarea) {
        tareasPendientes.push(tarea)
    }
}

// Mostrar todas las tareas
function mostrarTareas() {
    alert(`
        TAREAS PENDIENTES
        =================
        ${tareasPendientes.join("\n        ")}

        TAREAS COMPLETAS
        ================
        ${tareasCompletadas.join("\n        ")}
        `)
}

// Marcar tarea como completada
function marcarTareaCompleta() {
    let listaFormateada = ""
    tareasPendientes.forEach((tarea, indice) => {
        listaFormateada += indice + " - " + tarea
    })
    const tareaCompleta = prompt(`
        ¿Qué tarea quieres quitar¿
        ${listaFormateada}
        `)
}

// Contar tareas pendientes
function contarTareasPendientes() {
    alert("El número de tareas pendientes es " + tareasPendientes.length)
}


main()