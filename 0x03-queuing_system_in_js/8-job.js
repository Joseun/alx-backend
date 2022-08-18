//Que jobs for processing

function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
      throw new Error('Jobs is not an array');
    }
    jobs.forEach(async (job) => {
      const push_notification_code_3 = queue.create('email', job)
      await push_notification_code_3.save((err) => {
        if (!err) {
          console.log('Notification job created:', push_notification_code_3.id);
        }
      });
      push_notification_code_3.on('complete', () => {
        console.log(`Notification job #${push_notification_code_2.id} completed`);
      });
      push_notification_code_3.on('failed', (err) => {
        console.log('Notification job failed:', err);
      });
      push_notification_code_3.on('progress', (progress, data) => {
        console.log(`Notification job #${push_notification_code_2.id} ${progress}% complete`);
      });
    });
}

export default createPushNotificationsJobs;
  