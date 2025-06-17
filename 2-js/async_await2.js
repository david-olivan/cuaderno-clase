async function obtenerUsuario(id) {
	try {
		const resultado = await fetch(
			`https://jsonplaceholder.typicode.com/users/${id}`,
		);

		if (!resultado.ok) {
			throw new Error(`Error de HTTP: ${resultado.status} : ${resultado.statusText}`);
		}

		const usuario = await resultado.json();

		validarUsuario(usuario);

		return usuario;
	} catch (error) {
		console.error(error.message);
	} 
	
	return null;
}

function validarUsuario(usuario) {
	if (!usuario.email) {
		throw new Error("Oye, este usuario no tiene email");
	}
}

async function obtenerClima(ciudad) {
	//const btnCargar = document.getElementById("btnCargar")
	try {
		const url = `db/zaragoza.json`
		const response = await (fetch(url))
		const datos = await response.json()
		//document.getelementById('temperatura').textContent = datos.main.temp
		console.log(datos)
	} catch (error) {
		console.error(`Error: ${error.message}`)
	}	
}

const clima = await obtenerClima("zaragoza")