async function pruebasFetch() {
	return fetch("https://jsonplaceholder.typicode.com/usjers/")
		.then((response) => {
            if (!response.ok) throw new Error(response.status)
            return response.json()
        })
		.catch((error) => console.log(error.message));
}

const pruebas = await pruebasFetch();
console.log(pruebas);
