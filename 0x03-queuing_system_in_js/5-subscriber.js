// Subscribe to a news channel

import { createClient } from 'redis';

(async () => {
  const client = createClient();

  client.on('error', (err) => console.log('Redis client not connected to the server: ', err));

  client.on('connect', () => {
    console.log('Redis client connected to the server')
  });

  const subscriber = client.duplicate();

  subscriber.subscribe('holberton school channel');

  subscriber.on('message', async (err, msg) => {
    console.log(msg);
    if (msg === 'KILL_SERVER') {
      await subscriber.unsubscribe('holberton school channel');
      process.exit(0);
    }
});

  //await subscriber.subscribe('holberton school channel', (err, msg) => {
  //console.log(msg);
  //if (msg === 'KILL_SERVER') {
    //subscriber.unsubscribe('holberton school channel');
  ///}
  //});
})();
