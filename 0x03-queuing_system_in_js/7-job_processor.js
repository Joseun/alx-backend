// Job processor for multiple jobs

const blacklisted = ['4153518780', '4153518781'];

const kue = require('kue');

const queue = kue.createQueue();

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100)
  if (blacklisted.includes(phoneNumber)) {
    done(`Phone number ${phoneNumber} is blacklisted`);
  } else {
    job.progress(50, 100)
    done();
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
  }
}

queue.process('email', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
