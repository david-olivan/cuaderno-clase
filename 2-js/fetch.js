const url = "https://jsonplaceholder.typicode.com/users";

fetch(url)
	.then((respuesta) => {
        if (!(respuesta.status === 200)) {
            throw new Error(respuesta.status)
        }
		return respuesta.json();
	})
	.then((data) => {
		data.forEach(usuario => console.log(usuario.name))
	})
	.catch((error) => {
		console.log(error);
	});
