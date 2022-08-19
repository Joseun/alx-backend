// Seat reservation system

const redis = require('redis');

const util = require('util');

const client = redis.createClient();

const kue = require('kue');

const express = require('express');

async function reserveSeat(number) {
  console.log(number)
  client.set('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const getSeats = util.promisify(client.get).bind(client);
  return await getSeats('available_seats')
}

client.set('available_seats', 50);
client.set('reservationEnabled', true);

const queue = kue.createQueue();
const app = express();
app.listen(1245, () => console.log('Express app started!'));

app.get('/available_seats', (req, res) => {
  getCurrentAvailableSeats()
    .then((seats) => {
      res.send({"numberOfAvailableSeats":seats});
    })
});

app.get('/reserve_seat', (req, res) => {
  const reservationStatus = client.get('reservationEnabled');
  if (!reservationStatus) {
    res.send({ "status": "Reservation are blocked" });
  }
  const reserveSeat = queue.create('reserve_seat');
  var resStatus = {};
  reserveSeat.save((err) => {
    if (!err) {
      res.send({ "status": "Reservation in process" });
    } else {
      resStatus.status = "Reservation failed";
    }
  });

  reserveSeat.on('complete', () => {
    console.log(`Seat reservation job ${reserveSeat.id} completed`);
  });

  reserveSeat.on('failed', ()=> {
    console.log(`Seat reservation job ${reserveSeat.id} completed`);
  });
});

app.get('/process', (req, res) => {
  queue.process('email', (job, done) => {
    getCurrentAvailableSeats()
      .then((seats) => {
        reserveSeat(seats - 1);
        console.log('processed')
        if (seats === 0) {
          client.set('reservationEnabled', false);
        } else if (seats >= 0) {
          done();
        } else {
          job.failed('Not enough seats available');
        }
    });
  });
  res.send({ "status": "Queue processing" });
})
