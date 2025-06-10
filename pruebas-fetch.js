async function pruebasFetch() {
	return fetch("https://jsonplaceholder.typicode.com/usjers/")
		.then((response) => {
			if (!response.ok) throw new Error(response.status);
			return response.json();
		})
		.catch((error) => error.message);
}

const pruebas = await pruebasFetch();
const pruebas2 = await fetch("https://jsonplaceholder.typicode.com/users/1")
	.then((response) => {
		if (!response.ok) throw new Error(response.status);
		return response.json();
	})
	.catch((error) => error.message);

console.log(pruebas)
console.log(pruebas2)
