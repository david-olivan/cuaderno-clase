// TODO: implementar persistencia de tareas

// TODO: Rehacer el diseño del código para utilizar nombres más ilustrativos

// TODO: desacoplar funciones comunes


/**
 * Guarda una lista de tareas en localStorage
 * @param {string[]} lista lista de tareas para guardar
 */
function guardarTareas(lista) {
    localStorage.setItem("tareas", lista)
}


/**
 * Devuelve la lista de tareas guardadas en localStorage
 * @returns {string[]}
 */
function cargarTareas() {
    let tareas = localStorage.getItem("tareas")
    console.log(typeof tareas)
    
    if (!tareas) {
        tareas = []
        guardarTareas(tareas)
    }

    return tareas
}


function renderApp() {
    const myApp = document.getElementById("app")    

    // TODO: crear los componentes de tareas de manera programática
    myApp.innerHTML = `
        <h2>Bienvenid@ a la App</h2>

        <h3>Tareas pendientes</h3>
        <ol>
            ${formatearTareas(cargarTareas())}
        </ol>
    `
}


// function crearTarea() {
//     // TODO: Cambiar la estructura de datos a un modelo más flexible
//     const userInput = document.getElementById("nombreTarea")
//     tareasPendientes.push(userInput.value)
//     userInput.value = ""   
//     renderApp()
// }


function formatearTareas(listaDeTareas) {
    const tareasFormateadas = []

    listaDeTareas.forEach((tarea) => {
        tareasFormateadas.push(`<li>${tarea}</li>`)
    })

    return tareasFormateadas.join("")
}


// function eliminarTarea() {
//     const idTarea = document.getElementById("eliminarTarea")

//     if (!tareasPendientes[Number(idTarea.value - 1)]) {
//         alert("Tarea no existe")
//     } else {
//         tareasPendientes.splice(Number(idTarea.value - 1), 1)
//     }


//     idTarea.value = ""
//     renderApp()
// }


renderApp()
