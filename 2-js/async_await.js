async function llamarAPI(url) {
	// return fetch(url)
	// 	.then((resultado) => resultado.json())
	// 	.then((datos) => datos);
    const resultado = await fetch(url)
    const datos = await resultado.json()
    return datos
}

function mostrarResultado(datos) {
	console.log(datos);
}

const loQueMeDevuelve = await llamarAPI("https://rickandmortyapi.com/api")
//mostrarResultado(loQueMeDevuelve)