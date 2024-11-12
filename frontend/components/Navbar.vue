<template>
    <nav class="navbar navbar-expand-lg">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">BASF ToDo App</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <NuxtLink to="/" class="nav-link active">Home</NuxtLink>
            </li>
            <li class="nav-item">
              <NuxtLink to="/list" class="nav-link">Task List</NuxtLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </template>
  
  <script setup>
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
  
  .navbar {
    background-color: #2c3e50; 
    font-family: 'Roboto', sans-serif; 
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); 
    transition: background-color 0.3s ease; 
  }
  
  .navbar .navbar-brand {
    color: #ecf0f1;
    font-weight: 500;
    font-size: 24px;
    transition: color 0.3s ease;
  }
  
  .navbar .navbar-brand:hover {
    color: #3498db; 
  }
  
  .navbar-nav .nav-item .nav-link {
    color: #ecf0f1; 
    padding: 10px 20px;
    font-size: 16px;
    transition: color 0.3s ease, transform 0.3s ease;
  }
  
  .navbar-nav .nav-item .nav-link:hover {
    color: #3498db; 
    transform: scale(1.1); 
  }
  
  .navbar-toggler {
    border-color: #ecf0f1; 
  }
  
  .navbar-toggler-icon {
    background-color: #ecf0f1; 
  }
  
  .navbar.scrolled {
    background-color: #34495e;
  }
  </style>
  