const mqtt = require('mqtt');
const admin = require('firebase-admin');
const serviceAccount = require('./firebase.json');

admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
    databaseURL: "https://your-database-url.firebaseio.com"
});

const client = mqtt.connect('mqtt://broker.hivemq.com');
const db = admin.database();

client.on('connect', () => {
    client.subscribe('energy/data');
});

client.on('message', (topic, message) => {
    const data = JSON.parse(message.toString());
    db.ref('energy').set(data);
});
