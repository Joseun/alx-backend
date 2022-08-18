// Create a queue for jobs

const kue = require('kue');

//const string = kue.string;
const queue = kue.createQueue();

(async () => {
  const objData = {
    phoneNumber: "4153518780",
    message: "This is the code to verify your account",
  }
  const push_notification_code = queue.create('email', objData)
  await push_notification_code.save( (err) => {
    if (!err) {
      console.log('Notification job created:', push_notification_code.id);
    }
  });

  push_notification_code.on('complete', () => {
    console.log('Notification job completed');
  });

  push_notification_code.on('failed', () => {
    console.log('Notification job failed');
  });
})();
