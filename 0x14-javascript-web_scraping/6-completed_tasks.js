#!/usr/bin/node

const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

if (apiUrl) {
  // Make a GET request to the API
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }
    // Parse the response body as JSON
    const tasks = JSON.parse(body);
    // Initialize an object to store completed task counts per user ID
    const completedTasksByUser = {};

    // Iterate over the tasks
    tasks.forEach(task => {
      // Check if the task is completed
      if (task.completed) {
        // Increment the completed task count for the user ID
        completedTasksByUser[task.userId] = (completedTasksByUser[task.userId] || 0) + 1;
      }
    });

    // Print the completed task counts by user ID
    console.log(completedTasksByUser);
  });
} else {
  console.error('Usage: ./6-completed_tasks.js <API_URL>');
}
