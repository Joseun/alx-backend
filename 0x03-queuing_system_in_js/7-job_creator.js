// Multiple jobs

const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
];

const kue = require('kue');

const queue = kue.createQueue();

(async () => {
  jobs.forEach(async (job) => {
    const push_notification_code_2 = queue.create('email', job)
    await push_notification_code_2.save((err) => {
      if (!err) {
        console.log('Notification job created:', push_notification_code_2.id);
      }
    });

    push_notification_code_2.on('complete', () => {
        console.log(`Notification job #${push_notification_code_2.id} completed`);
      });
    
    push_notification_code_2.on('failed', (err) => {
      console.log('Notification job failed', err);
    });

    push_notification_code_2.on('progress', (progress, data) => {
      console.log(`Notification job #${push_notification_code_2.id} ${progress}% complete`);
    });
  });
})();
