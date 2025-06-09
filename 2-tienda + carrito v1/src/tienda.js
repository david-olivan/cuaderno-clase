const carrito = {}

function renderTarjetaProducto(producto) {
	const tarjetaProducto = document.createElement("article");
	const titulo = document.createElement("h3");
	const imagen = document.createElement("img");
	const subtitulo = document.createElement("h4");

	const footer = document.createElement("footer");
	const precio = document.createElement("p");
	const botonMenos = document.createElement("button");
	const botonMas = document.createElement("button");

	tarjetaProducto.classList.add("tarjeta-producto");
	titulo.textContent = producto.nombre;
	imagen.src = producto.imageURL;
	subtitulo.textContent = producto.subtitulo;
	precio.textContent =
		(producto.precio * (1 + producto.iva)).toFixed(2) + " €";
	botonMenos.textContent = "➖";
	botonMas.textContent = "➕";

    botonMenos.addEventListener("click", (e) => restarProducto(producto.codigo))
    botonMas.addEventListener("click", (e) => sumarProducto(producto.codigo))

	footer.append(precio, botonMenos, botonMas);
	tarjetaProducto.append(titulo, imagen, subtitulo, footer);

	return tarjetaProducto;
}

function restarProducto(codigo) {
    if (carrito[codigo] > 0) {
        carrito[codigo] -= 1
    }

    mostrarCarrito()
}

function sumarProducto(codigo) {
    if (carrito[codigo]) {
        carrito[codigo] += 1
    } else {
        carrito[codigo] = 1
    }

    mostrarCarrito()
}

function mostrarCarrito() {
    const elementoCarrito = document.querySelector("#carrito-compra")

    const titulo = document.createElement("h3")
    let precioTotal = 0
    const textoTotal = document.createElement("h4")
    const listaProductos = []

    Object.entries(carrito).forEach((item) => {
        if (item[1] !== 0) {            
            const prod = document.createElement("p")

            const datosProducto = productos.filter(producto => producto.codigo === item[0])[0]
            const precioProductoTotal = ((datosProducto.precio * (1 + datosProducto.iva)) * item[1])

            console.log(datosProducto)

            prod.textContent = `${datosProducto.nombre} x${item[1]} --- ${precioProductoTotal.toFixed(2)} €`

            precioTotal += precioProductoTotal

            listaProductos.push(prod)
        }
    })

    titulo.textContent = "Carrito"
    textoTotal.textContent = "Total_________" + precioTotal.toFixed(2) + " €"

    elementoCarrito.replaceChildren(titulo, ...listaProductos, textoTotal)
}

window.onload = () => {
	const tienda = document.querySelector("#lista-productos");

	productos.forEach((producto) => {
		tienda.appendChild(renderTarjetaProducto(producto));
	});
};

