/**
 * Guarda una lista de tareas en localStorage
 * @param {{}[]} lista lista de tareas para guardar
 */
function guardarTareas(lista) {
    localStorage.setItem("tareas", JSON.stringify(lista))
}


/**
 * Devuelve la lista de tareas guardadas en localStorage
 * @returns {{}[]}
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
        return tareas
    }

    return JSON.parse(tareas)
}