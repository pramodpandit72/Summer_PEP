import { Kafka } from "kafkajs";

const kafka = new Kafka({
    clientId:"email-service",
    brokers:["kafka:9092"]
})

const consumer = kafka.consumer({
    groupId: "email-group"
});

async function run() {
    await consumer.connect()

    await consumer.subscribe({
        topic:"order-topic",
        fromBeginning: true
    });
    console.log("Email Service Started");

    await consumer.run({
        eachMessage:async({message})=>{
            const order=JSON.parse(message.value.toString())

            console.log("-----Email Service-----");
            console.log("New Order Received");
            console.log("order");

            console.log("Email send successfully");
        }
    }) 
}

run();