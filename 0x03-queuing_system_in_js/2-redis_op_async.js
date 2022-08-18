// Connect to a Redis server

import { createClient } from 'redis';

const redis = require('redis');

const util = require('util');

const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server: ', err));

const readCache = util.promisify(client.get).bind(client);

client.on('connect', () => {
    console.log('Redis client connected to the server')
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  console.log(await readCache(schoolName));
}

displaySchoolValue('Holberton')
setNewSchool('HolbertonSanFrancisco', '100');
