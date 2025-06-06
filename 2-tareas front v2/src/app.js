// ESTRUCTURA DE TAREAS
// {
//  nombre, prioridad, estado
// }

function renderizarTarea(tarea, indice) {
	const tablaTareas = document.getElementById("tablaTareas");

	const prioridades = ["Normal", "Importante", "SuperUrgente"];
	const estados = {
		pendiente: "Pendiente",
		progreso: "En progreso",
		completa: "Tarea completada",
	};

	// Crearé y rellenaré cosicas del tr
	const fila = document.createElement("tr");
	const [col1, col2, col3, col4] = [
		document.createElement("td"),
		document.createElement("td"),
		document.createElement("td"),
		document.createElement("td"),
	];
	const btnBorrar = document.createElement("span");

	col1.textContent = tarea.nombre;
	col2.textContent = prioridades[tarea.prioridad - 1];
	col3.textContent = estados[tarea.estado];

	btnBorrar.innerHTML = "&#9760;";
	btnBorrar.classList.add("btnBorrar");
	btnBorrar.addEventListener("click", () => {
		eliminarTarea(indice);
		fila.remove();
	});

	col4.append(btnBorrar);
	fila.append(col1, col2, col3, col4);

	// Añado al final de tabla de tareas
	tablaTareas.append(fila);
}

/**
 * Hace una llamada a añadirTareas y resetea el valor del input
 */
function crearTarea() {
	const userInput = document.getElementById("nombreTarea");
	const userPrioridad = document.getElementById("prioridadTarea");
	const userEstado = document.getElementById("estadoTarea");

	const nuevaTarea = {
		nombre: userInput.value,
		prioridad: Number(userPrioridad.value),
		estado: userEstado.value,
	};

	if (nuevaTarea.nombre.length < 3 || nuevaTarea.nombre.length > 63) {
		console.warn(
			"El nombre de la tarea debe tener entre 3 y 63 caracteres",
		);
		return;
	}

	if (![1, 2, 3].includes(nuevaTarea.prioridad)) {
		console.warn("Prioridad no es válida");
		return;
	}

	if (!["pendiente", "progreso", "completa"].includes(nuevaTarea.estado)) {
		console.warn(
			"El estado debe ser 'pendiente', 'progreso' o 'completa'",
		);
		return;
	}

	guardarTarea(nuevaTarea);
	renderizarTarea(nuevaTarea);
}

/**
 * La función crea un objeto con las propiedades de tarea (nombre, prioridad, estado) y lo guarda en localStorage
 * @param {string} nombre El nombre de la tarea
 * @param {number} prioridad La prioridad de la tarea
 * @param {string} estado El estado de la tarea
 * @returns
 */
function guardarTarea(tarea) {
	const tareas = cargarTareasDB();
	tareas.push(tarea);
	guardarTareasDB(tareas);
}

/**
 * Elimina una tarea en base a un índice
 * @param {number} idTarea El índice de la lista de tareas
 * @returns
 */
function eliminarTarea(idTarea) {
	if (typeof idTarea !== "number" || idTarea < 0) {
		console.warn("El id no es válido --- idTareas: " + typeof idTarea);
		return;
	}

	const tareas = cargarTareasDB();

	if (tareas[idTarea]) {
		tareas.splice(idTarea, 1);
		guardarTareasDB(tareas);
	}
}

window.onload = () => {
	document
		.getElementById("formTareas")
		.addEventListener("submit", (e) => e.preventDefault());

	cargarTareasDB().forEach((tarea, indice) =>
		renderizarTarea(tarea, indice),
	);
};

// LISTENERS PARA FADE-IN-OUT DE LA TABLA DE TAREAS
// document.getElementById("formTareas").addEventListener("mouseenter", (e) => {
//     document.getElementById("laTabla").classList.add("oculto")
// })

// document.getElementById("formTareas").addEventListener("mouseleave", (e) => {
//     document.getElementById("laTabla").classList.remove("oculto")
// })
