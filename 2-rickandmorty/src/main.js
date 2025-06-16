// Variable global para tener acceso a mi "ventana" de contenidos desde cualquier función
let contenidos;
// La url base para todas las llamadas a la app de Rick&Morty
const baseURL = "https://rickandmortyapi.com/api/";

/**
 * Recibe los resultados de una llamada de Fetch API y los formatea y muestra en "contenidos"
 * @param {Object} algo El objeto devuelto por .json() tras el último .then de la promesa
 */
function mostrarResultados(algo) {
    // .map() me permite iterar una lista, aplicar una transformación a cada elemento de la lista
    // y devuelve una nueva lista con los elementos transformados, la cual puedo guardar en una 
    // constante como hacemos aquí
	const listaFormateada = algo.map((item) => {
        // Creo un contenedor "article" para cada item así como un párrafo para el texto
		const tarjeta = document.createElement("article");
		const parrafo = document.createElement("p");

        // Guardo el valor de episode
		const nombreEpisodio = item.episode;

        // Formateo los contenidos del párrafo, añadiendo el nombre del episodio si existe (solamente
        // estará en las entidades 'episode') y luego el nombre de cada item que estará presente
        // en todas las entidades.
		parrafo.textContent = `${
			typeof nombreEpisodio == "string" ? nombreEpisodio : ""
		} ${item.name}`;

        // Si existe una entrada en el objeto bajo la clave 'image' entonces ejecuta este código
		if (item.image) {
            // Crea un Nodo de imagen, configura el src de la imagen y añádelo a la tarjeta
			const tmp = document.createElement("img");
			tmp.src = item.image;
			tarjeta.appendChild(tmp);
		}

        // Añade el párrafo a la tarjeta
		tarjeta.appendChild(parrafo);

        // Si en el objeto hay una entrada bajo la clave 'origin' entonces ejecuta este código
		if (item.origin) {
            // Si además tiene una url que no esté vacía entonces haz esto
            // Con esto estamos evitando crear botones si la url está vacía porque me dará problemas
			if (item.origin.url) {
                // Crea un botón y asígnale el texto Origen
				const btn = document.createElement("button");
				btn.textContent = "Origen";

                // Añade un event listener para el evento 'click' y pasale la url a la función
                // mostrarOrigen. Esta url la recibo de la API y referencia la llamada GET para
                // un lugar.
				btn.addEventListener("click", () =>
					mostrarOrigen(item.origin.url),
				);

                // Añade el botón a la tarjeta
				tarjeta.appendChild(btn);
			}
		}

        // Devuelve la tarjeta a la nueva lista
		return tarjeta;
	});

    // Ahora reemplaza los contenidos de nuestra 'ventana' con los elementos
    // uno a uno de la listaFormateada. Con los tres puntos ... desestructuramos la lista
    // pasándosela a la función de elemento en elemento en vez de como una lista entera.
	contenidos.replaceChildren(...listaFormateada);
}

/**
 * Recibe la url del origen de un personaje, vacía los contenidos y muestra los valores de la nueva llamada API
 * @param {string} url La url del origen de un personaje
 */
function mostrarOrigen(url) {
    // Hace un fetch sobre la url recibida
	fetch(url)
		.then((resultado) => resultado.json())
		.then((texto) => {
            // Tras convertir a json los resultados, hace un replaceChildren para vaciar la 'ventana'
            // y luego rellena dicha ventana con html a pelo, incluyendo valores del nuevo objeto recibido.
			contenidos.replaceChildren();
			contenidos.innerHTML = `
                ${texto.name}<br>
                ${texto.type}<br>
                ${texto.dimension}<br>
            `;
		});
}

/**
 * Hace una llamada a la API de Rick&Morty usando la baseURL y el argumento
 * @param {string} userInput La segunda parte de la URL para la llamada a la API
 */
function llamarAPI(userInput) {
    // Monto la URL completa con la base y lo que me hayan pasado a la función
	const urlCompleta = baseURL + userInput;

    // Hago un fetch sobre la URL, me devuelve una promesa, sobre la cual llamo a 
    // .json() que me devuelve otra promesa, por eso encadeno .then()
    // Con el resultado ya transformado en json, hago una llamada a mostrarResultados()
	fetch(urlCompleta)
		.then((resultado) => resultado.json())
		.then((texto) => mostrarResultados(texto.results))
		.catch((err) => console.log(err));
}


// Este evento se dispara cuando la ventana se ha terminado de cargar
window.onload = () => {
    // Referencio toda mi app que es una section vacía en el html
	const myApp = document.getElementById("app");

	// Creo un contenedor div y 3 botones
	const botones = document.createElement("div");
	const btnCharacters = document.createElement("button");
	const btnLocations = document.createElement("button");
	const btnEpisodes = document.createElement("button");

    // Añado el texto de los botones
	btnCharacters.innerText = "Personajes";
	btnLocations.innerText = "Lugares";
	btnEpisodes.innerText = "Episodios";

    // Añado un listener para el evento click a cada botón, llamando a la función
    // que hará la llamada a la API con el endpoint asociado a cada botón (por entidad)
	btnCharacters.addEventListener("click", () => llamarAPI("character"));
	btnLocations.addEventListener("click", () => llamarAPI("location"));
	btnEpisodes.addEventListener("click", () => llamarAPI("episode"));

    // Uno los tres Nodos de los botones a su contenedor
	botones.append(btnCharacters, btnLocations, btnEpisodes);

	// Crear un contenedor vacío para los contenidos que muestro
	const contenedor = document.createElement("div");
    // Le añado id y clases
	contenedor.id = "contenidos";
	contenedor.classList.add("contenidos");
    // Lo referencio en la variable global que he creado previamente
	contenidos = contenedor;

    // Uno el contenedor de los botones y el contenedor vacío para mostrar la info a la section de mi app
	myApp.append(botones, contenidos);
};
