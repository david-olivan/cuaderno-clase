// ESTRUCTURA DE TAREAS
// {
//  nombre, prioridad, estado
// }

let numeroTareas = 0


function renderApp() {
    const tablaTareas = document.getElementById("tablaTareas")
    tablaTareas.innerHTML = ""
    const prioridades = ["Normal", "Importante", "SuperUrgente"]
    const estados = {
        "pendiente": "Pendiente",
        "progreso": "En progreso",
        "completa": "Tarea completada"
    }

    const idsParaListeners = []

    cargarTareas().forEach((tarea, index) => {
        const idBorrar = "tarea" + index
        idsParaListeners.push(idBorrar)

        tablaTareas.innerHTML += `
                <tr>
                    <td>${tarea.nombre}</td>
                    <td>${prioridades[tarea.prioridad - 1]}</td>
                    <td>${estados[tarea.estado]}</td>
                    <td><span id=${idBorrar} class='btnBorrar'>&#9760;</span></td>
                </tr>
        `
    })

    idsParaListeners.forEach(idParaListener => {
        document.getElementById(idParaListener).addEventListener("click", (event) => {
            const index = Number(event.target.id.replace("tarea", ""))
            console.log("Eliminando la tarea: " + index)
            eliminarTarea(index)
        })
    })
}

/**
 * Hace una llamada a añadirTareas y resetea el valor del input
 */
function crearTarea() {
    const userInput = document.getElementById("nombreTarea")
    añadirTarea(userInput.value)
    userInput.value = ""

    renderApp()
}

/**
 * La función crea un objeto con las propiedades de tarea (nombre, prioridad, estado) y lo guarda en localStorage
 * @param {string} nombre El nombre de la tarea
 * @param {number} prioridad La prioridad de la tarea
 * @param {string} estado El estado de la tarea
 * @returns 
 */
function añadirTarea(nombre, prioridad=1, estado="pendiente") {
    if (nombre.length < 3 || nombre.length > 63) {
        console.warn("El nombre de la tarea debe tener entre 3 y 63 caracteres")
        return
    }

    if (![1, 2 ,3].includes(prioridad)) {
        console.warn("Prioridad no es válida")
        return
    }

    if (!["pendiente", "progreso", "completa"].includes(estado)) {
        console.warn("El estado debe ser 'pendiente', 'progreso' o 'completa'")
        return
    }

    const tareas = cargarTareas()
    tareas.push({nombre, prioridad, estado})

    guardarTareas(tareas)
}


/**
 * Elimina una tarea en base a un índice
 * @param {number} idTarea El índice de la lista de tareas
 * @returns 
 */
function eliminarTarea(idTarea) {
    if (typeof idTarea !== "number" || idTarea < 0) {
        console.warn("El id no es válido --- idTareas: " + typeof idTarea)
        return
    }

    const tareas = cargarTareas()

    if (tareas[idTarea]) {        
        tareas.splice(idTarea, 1)
        guardarTareas(tareas)    
        renderApp()
    }
}

renderApp()


// LISTENERS PARA FADE-IN-OUT DE LA TABLA DE TAREAS
// document.getElementById("formTareas").addEventListener("mouseenter", (e) => {
//     document.getElementById("laTabla").classList.add("oculto")
// })

// document.getElementById("formTareas").addEventListener("mouseleave", (e) => {
//     document.getElementById("laTabla").classList.remove("oculto")
// })

document.getElementById("ejemploPrevent").addEventListener("click", e => {
//    e.preventDefault()
    e.target.textContent += "Porfi no te vayas"

    if (e.target.textContent.length >= 100) {

    }
})