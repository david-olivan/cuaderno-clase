function promesa(nombre) {
	return new Promise((resolve, reject) => {
		if (nombre === "David") {
			resolve({
                nombre: nombre,
                token: "abc123"
            });
		} else {
			reject("Nombre incorrecto");
		}
	});
}

promesa("David")
	.then((resultado) => {
		console.log(resultado);
	})
	.catch((err) => console.log(err));
