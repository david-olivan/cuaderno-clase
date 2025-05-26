const tareasPendientes = ["Limpiar ordenador","Explicar JS", "Resolver dudas"]
const tareasCompletas = []

function main() {
    renderApp()
}
// Recargar interfaz
function renderApp() {
    const myApp = document.getElementById("app")    

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

// Crear tareas
function crearTarea() {
    const userInput = document.getElementById("nombreTarea")
    tareasPendientes.push(userInput.value)
    userInput.value = ""   
    renderApp()
}

// Muestra las tareas
function formatearTareas(listaDeTareas, completo) {
    const tareasFormateadas = []

    listaDeTareas.forEach((tarea) => {
        tareasFormateadas.push(`<li ${completo ? "class='tachado'": ""}>${tarea}</li>`)
    })

    return tareasFormateadas.join("")
}

// Complete una tarea

// Eliminar Tarea
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
