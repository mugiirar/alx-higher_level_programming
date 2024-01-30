#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, responseBody) {
  if (error) {
    console.log(error);
  } else {
    const tasksCompletedByUser = {};
    const tasks = JSON.parse(responseBody);
    
    for (let i = 0; i < tasks.length; i++) {
      const currentTask = tasks[i];
      
      if (!(currentTask.userId in tasksCompletedByUser)) {
        tasksCompletedByUser[currentTask.userId] = 0;
      }
      
      if (currentTask.completed) {
        tasksCompletedByUser[currentTask.userId] += 1;
      }
      
      if (tasksCompletedByUser[currentTask.userId] === 0) {
        delete tasksCompletedByUser[currentTask.userId];
      }
    }
    
    console.log(tasksCompletedByUser);
  }
});

