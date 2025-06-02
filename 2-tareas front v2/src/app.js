// TODO: implementar persistencia de tareas

// TODO: Rehacer el diseño del código para utilizar nombres más ilustrativos

// TODO: desacoplar funciones comunes


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


function formatearTareas(tareas) {
    const tareasFormateadas = []

    tareas.forEach((tarea) => {
        tareasFormateadas.push(`<li>${tarea.nombre}</li>`)
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
