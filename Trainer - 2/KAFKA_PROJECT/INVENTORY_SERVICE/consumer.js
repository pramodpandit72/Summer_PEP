import { Kafka } from "kafkajs";

const kafka = new Kafka({
    clientId:"inventory-service",
    brokers:["kafka:9092"]
})

const consumer = kafka.consumer({
    groupId: "inventory-group"
});

async function run() {
    await consumer.connect()

    await consumer.subscribe({
        topic:"order-topic",
        fromBeginning: true
    });
    console.log("inventory Service Started");

    await consumer.run({
        eachMessage:async({message})=>{
            const order=JSON.parse(message.value.toString())

            console.log("-----Inventory Service-----");
            console.log("New Order Received");
            console.log("order");
            
        }
    }) 
}

run();