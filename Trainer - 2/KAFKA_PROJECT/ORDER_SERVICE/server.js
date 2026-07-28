import express from "express";
import sendOrder from "./producer.js";
const app = express();
let orderID = 1;

app.use(express.json());

app.post("/orders", async(req, res)=>{
    const order = {
        orderID: orderID++,
        customer:req.body.customer,
        product:req.body.product,
        quantity:req.body.quantity
    };
    try{
        await sendOrder(order);
        res.status(201).json({
            message:"Order Created",
            order
        });
    } catch(err) {
        console.log(err);
        res.status(500).json({
            message:"Kafka error"
        })
    }
})

app.listen(3001, () => {
    console.log("Order service running on port 3001");
});
