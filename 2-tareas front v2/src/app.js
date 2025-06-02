// ESTRUCTURA DE TAREAS
// {
//  nombre, prioridad, estado
// }


function renderApp() {
    const tablaTareas = document.getElementById("tablaTareas")
    tablaTareas.innerHTML = ""

    cargarTareas().forEach((tarea, index) => {
        tablaTareas.innerHTML += `
                <tr>
                    <td>${index + 1}</td>
                    <td>${tarea.nombre}</td>
                    <td>Importante</td>
                    <td>En progreso</td>
                </tr>
        `
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

function formatearTareas(tareas) {
    const tareasFormateadas = []

    tareas.forEach((tarea) => {
        tareasFormateadas.push(`<li>${tarea.nombre}</li>`)
    })

    return tareasFormateadas.join("")
}


function eliminarTarea() {
    const userInput = document.getElementById("eliminarTarea")
    const idTarea = Number(userInput.value) - 1
    const tareas = cargarTareas()
    userInput.value = ""

    if (!tareas[idTarea]) {
        console.warn("Tarea no existe o el id no es válido")
        return
    }
    
    tareas.splice(idTarea, 1)

    guardarTareas(tareas)    
    renderApp()
}


renderApp()
