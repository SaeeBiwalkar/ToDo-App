const API_BASE_URL = "https://todo-app-si20.onrender.com/todos";

// Fetch and display tasks
function fetchTasks() {
  fetch(API_BASE_URL)
    .then((response) => response.json())
    .then((data) => {
      const taskList = document.getElementById("tasks");
      taskList.innerHTML = ""; // Clear the list

      // Loop through each task and display it
      data.forEach((task) => {
        const li = document.createElement("li");
        li.innerHTML = `
          <strong>${task.title}</strong>: ${task.description}
          <div class="task-actions">
            <button onclick="deleteTask(${task.id})">Delete</button>
            <button onclick="editTask(${task.id})">Edit</button>
          </div>
        `;
        taskList.appendChild(li);
      });
    })
    .catch((error) => console.error("Error fetching tasks:", error));
}

// Add a new task
function addTask() {
  const title = document.getElementById("task-title").value;
  const description = document.getElementById("task-desc").value;

  // Send POST request to FastAPI backend
  fetch(API_BASE_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ title, description }),
  })
    .then((response) => response.json()) // Get the response from the backend
    .then((data) => {
      document.getElementById("task-title").value = "";  // Clear the input fields
      document.getElementById("task-desc").value = "";
      fetchTasks();  // Refresh the task list after adding a task
    })
    .catch((error) => console.error("Error adding task:", error));
}

// Delete a specific task
function deleteTask(id) {
  fetch(`${API_BASE_URL}/${id}`, {
    method: "DELETE",
  })
    .then(() => fetchTasks()) // Refresh the list after deleting the task
    .catch((error) => console.error("Error deleting task:", error));
}

// Edit a specific task
function editTask(id) {
  const newTitle = prompt("Enter new title:");
  const newDescription = prompt("Enter new description:");

  if (newTitle && newDescription) {
    fetch(`${API_BASE_URL}/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ title: newTitle, description: newDescription }),
    })
      .then(() => fetchTasks()) // Refresh the list after editing the task
      .catch((error) => console.error("Error editing task:", error));
  }
}

// Delete all tasks
function deleteAllTasks() {
  fetch(API_BASE_URL, {
    method: "DELETE",
  })
    .then(() => fetchTasks()) // Refresh the list after deleting all tasks
    .catch((error) => console.error("Error deleting all tasks:", error));
}

// Call fetchTasks to populate the task list when the page loads
window.onload = fetchTasks;
