const express = require("express");
const redis = require("redis");
require("dotenv").config();

const app = express();
const client = redis.createClient({
	socket: {
		host: process.env.REDIS_HOST,
		port: 6379,
	},
});

app.get("/", (req, res) => {
	res.json({ message: "Hola que tal por aquí" });
});

app.get("/contador", async (req, res) => {
	try {
		const reply = await client.incr("contador");
		res.json({ contador: reply });
	} catch (err) {
		res.status(500).send("error incrementando");
	}
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, async () => {
	await client.connect();
	console.log(`App funcionado en el puerto ${PORT}`);
});
