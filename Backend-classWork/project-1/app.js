import express from "express";

const app = express();

// Middleware
app.use(express.json());

// =======================
// Student Data
// =======================
const students = [
    { id: 1, name: "Mukund", course: "CSE" },
    { id: 2, name: "Rahul", course: "AI" },
    { id: 3, name: "Aman", course: "IT" }
];   

// =======================
// Product Data
// =======================
const products = [
    { id: 1, name: "Laptop", price: 50000 },
    { id: 2, name: "Phone", price: 20000 },
    { id: 3, name: "Mouse", price: 800 }
];

// =======================
// Home Route
// =======================
app.get("/", (req, res) => {
    res.send("Welcome to Express.js Lab");
});

// ===================================================
// STUDENT API
// ===================================================

// Get All Students
app.get("/students", (req, res) => {
    res.json(students);
});

// Get Student by ID
app.get("/students/:id", (req, res) => {

    const id = parseInt(req.params.id);

    const student = students.find(s => s.id === id);

    if (student) {
        res.json(student);
    } else {
        res.status(404).send("Student Not Found");
    }
});

// Add New Student
app.post("/students", (req, res) => {

    students.push(req.body);

    res.send("Student Added Successfully");
});

// ===================================================
// PRODUCT API
// ===================================================

// Get All Products
app.get("/products", (req, res) => {
    res.json(products);
});

// Get Product by ID
app.get("/products/:id", (req, res) => {

    const id = parseInt(req.params.id);

    const product = products.find(p => p.id === id);

    if (product) {
        res.json(product);
    } else {
        res.status(404).send("Product Not Found");
    }
});

// Add New Product
app.post("/products", (req, res) => {

    products.push(req.body);

    res.send("Product Added Successfully");
});

// ===================================================
// Server
// ===================================================
app.listen(3001, () => {
    console.log("Server is running on http://localhost:3001");
});