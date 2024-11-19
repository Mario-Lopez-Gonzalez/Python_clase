use mi_basededatos
db.createCollection("usuarios")
db.createCollection("coches")
db.usuarios.insertMany([
    {
        nombre: "Usuario 1",
        edad: 30,
        correo: "usuario1@example.com"
    },
    {
        nombre: "Usuario 2",
        edad: 25,
        correo: "usuario2@example.com"
    },
    {
        nombre: "Usuario 3",
        edad: 35,
        correo: "usuario3@example.com"
    }
])
db.coches.insertMany([
    {
        marca: "Toyota",
        modelo: "Corolla",
        año: 2020
    },
    {
        marca: "Ford",
        modelo: "Mustang",
        año: 2019
    },
    {
        marca: "Honda",
        modelo: "Civic",
        año: 2021
    }
])
