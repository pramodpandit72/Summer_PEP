import { Kafka, Partitioners } from "kafkajs";

const kafka = new Kafka({
    clientId:"order_service",
    brokers:["kafka:9092"]
})

const producer = kafka.producer({
    createPartitioner: Partitioners.LegacyPartitioner
});

async function sendOrder(order) {
    await producer.connect()

    await producer.send({
        topic:"order-topic",
        messages: [
            {
                value:JSON.stringify(order)
            }
        ]
    });
    console.log("I have Published my order to kafka");

    await producer.disconnect()
}
export default sendOrder;
