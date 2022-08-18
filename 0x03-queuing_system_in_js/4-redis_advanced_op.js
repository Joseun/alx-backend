// HSet in redis

import { createClient } from 'redis';

const redis = require('redis');

const util = require('util');

const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server: ', err));

client.on('connect', () => console.log('Redis client connected to the server'));

function hashSet(hash, key, value) {
  client.hset(hash, key, value, redis.print);
}

function hashGet(hash) {
    client.hgetall('HolbertonSchools', (err, val) => console.log(val));
}

//client.hset('HolbertonSchools', 'Portland', 50, (val) => console.log(val));
hashSet('HolbertonSchools', 'Portland', 50);
hashSet('HolbertonSchools', 'Seattle', 80);
hashSet('HolbertonSchools', 'New York', 20);
hashGet('HolbertonSchools');
//client.hgetall('HolbertonSchools', (val) => console.log(val));
