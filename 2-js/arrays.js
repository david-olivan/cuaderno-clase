const nombres = ["David", "Goliath", "elDelo", "Fran", "Sam", "Dani"]

// () => {}
const nombresFiltrados = nombres.filter(nombre => nombre[0].includes("D"))
nombresFiltrados.forEach(nombre => console.log("Hola " + nombre));

console.log(nombres)
console.log(nombresFiltrados)
nombresFiltrados.push("AleAlejandro")
console.log(nombresFiltrados)
nombresFiltrados.unshift("Gaga")
console.log(nombresFiltrados)
console.log(nombresFiltrados.shift())
console.log(nombresFiltrados)