/**
 * Guarda una lista de tareas en localStorage
 * @param {string[]} lista lista de tareas para guardar
 */
function guardarTareas(lista) {
    localStorage.setItem("tareas", JSON.stringify(lista))
}


/**
 * Devuelve la lista de tareas guardadas en localStorage
 * @returns {string[]}
 */
function cargarTareas() {
    let tareas = localStorage.getItem("tareas")
    
    if (!tareas) {
        tareas = [
                {
                    "nombre": "Tarea de ejemplo",
                    "prioridad": 1,
                    "estado": "pendiente"
                },
                {
                    "nombre": "Segunda tarea de ejemplo",
                    "prioridad": 2,
                    "estado": "pendiente"
                }
            ]
        guardarTareas(tareas)
    }

    return JSON.parse(tareas)
}