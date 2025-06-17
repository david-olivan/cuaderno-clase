const myApp = document.getElementById("app");

function mostrarDatos(data) {
	data.forEach((libro) => {
		const tarjeta = document.createElement("article");
		const titulo = document.createElement("h2");
		const autor = document.createElement("p");
		titulo.textContent = libro.titulo;
		autor.textContent = libro.autor;

		tarjeta.append(titulo, autor);
		myApp.appendChild(tarjeta);
	});
}

window.onload = () => {
	fetch("api/libros.json")
		.then((resultado) => resultado.json())
		.then((data) => mostrarDatos(data));
};
