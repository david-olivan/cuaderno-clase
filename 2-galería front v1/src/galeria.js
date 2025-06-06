function agregarImagen() {
	// Pillar el valor del input
	const userURL = document.getElementById("url-image");
	const finalURL = userURL.value.trim();

	// Validar que en el input hay algo que me vale
	if (!finalURL) {
		mensajeInterfaz("No se ha introducido URL");
		userURL.value = "";
		return;
	}

	const extensionURL = finalURL.split(".").reverse()[0];
	if (!["jpg", "jpeg", "webp", "png"].includes(extensionURL)) {
		mensajeInterfaz("Esta galeria no soporta ese formato");
		userURL.value = "";
		return;
	}

	// Pillar el contenedor que es la galería
	const galeria = document.querySelector("#galeria"); //=== document.getElementById("galeria")

	// Crear nuevo elemento y guardar en constante
	const contenedorImagen = document.createElement("div");
	const nuevaImagen = document.createElement("img");
	const nuevoBoton = document.createElement("button");

	// Añadir clase al contenedor
	contenedorImagen.classList.add("tarjeta-imagen");

	// Modificar la const del nuevo elemento
	nuevaImagen.src = finalURL;
	nuevaImagen.alt = "Una imagen de la galería";
	nuevaImagen.title = "Galería v1";

	// Rellenar cosicas del botón
	nuevoBoton.textContent = "❌";
	nuevoBoton.addEventListener("click", () => {
		contenedorImagen.remove();
		mensajeInterfaz("Imagen borrada de la galería", "exito");
	});

	userURL.value = "";

	mensajeInterfaz("Imagen añadida correctamente", "exito");

	// Añadir nuevos elementos
	contenedorImagen.append(nuevoBoton, nuevaImagen);
	galeria.append(contenedorImagen);
}

window.addEventListener("load", () => {
	document.querySelector("#galeria-form").addEventListener("submit", (e) => {
		e.preventDefault();
	});
});

/**
 * Mostrar un mensaje al usuario integrado en la interfaz
 * @param {string} errorText El mensaje que quiero enviar
 * @param {string} tipo El tipo de mensaje (exito|error)
 */
function mensajeInterfaz(errorText, tipo = "error") {
	const errorMessage = document.createElement("p");
	errorMessage.textContent = errorText;

	if (tipo === "error") {
		errorMessage.classList.add("mensaje-error");
	} else if (tipo === "exito") {
		errorMessage.classList.add("mensaje-exito");
	}

	document.querySelector("#galeria-form").append(errorMessage);
	setTimeout(() => errorMessage.classList.add("hidden"), 1500);
	setTimeout(() => errorMessage.remove(), 2000);
}
