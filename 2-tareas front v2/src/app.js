// TODO: implementar persistencia de tareas

// TODO: Rehacer el diseño del código para utilizar nombres más ilustrativos
// olvidándonos de main.

// TODO: desacoplar funciones comunes

const tareasPendientes = ["Limpiar ordenador","Explicar JS", "Resolver dudas"]
const tareasCompletas = []

function main() {
    renderApp()
}

function renderApp() {
    const myApp = document.getElementById("app")    

    // TODO: crear los componentes de tareas de manera programática
    myApp.innerHTML = `
        <h2>Bienvenid@ a la App</h2>

        <h3>Tareas pendientes</h3>
        <ol>
            ${formatearTareas(tareasPendientes, completo=false)}
        </ol>

        <h3>Tareas Completas</h3>
        <ul>
            ${formatearTareas(tareasCompletas, completo=true)}
        </ul>
    `
}


function crearTarea() {
    // TODO: Cambiar la estructura de datos a un modelo más flexible
    const userInput = document.getElementById("nombreTarea")
    tareasPendientes.push(userInput.value)
    userInput.value = ""   
    renderApp()
}


function formatearTareas(listaDeTareas, completo) {
    const tareasFormateadas = []

    listaDeTareas.forEach((tarea) => {
        tareasFormateadas.push(`<li ${completo ? "class='tachado'": ""}>${tarea}</li>`)
    })

    return tareasFormateadas.join("")
}


function eliminarTarea() {
    const idTarea = document.getElementById("eliminarTarea")

    if (!tareasPendientes[Number(idTarea.value - 1)]) {
        alert("Tarea no existe")
    } else {
        tareasCompletas.push(tareasPendientes.splice(Number(idTarea.value - 1), 1))
    }


    idTarea.value = ""
    renderApp()
}


main()
