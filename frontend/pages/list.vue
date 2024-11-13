<template>
  <div class="hero">
    <div class="container">
      <h1 class="hero-text">Tasks List</h1>

      <!-- Tasks form -->
      <form @submit.prevent="saveItem" class="mb-3 form-container">
        <div class="input-group">
          <input v-model="newItem.title" type="text" class="form-control" placeholder="Task Name" required />
          <input v-model="newItem.description" type="text" class="form-control" placeholder="Description" />
          <button type="submit" class="btn btn-primary">{{ editingItem ? 'Guardar' : 'Add' }}</button>
        </div>
      </form>

      <!-- Search tasks filter -->
      <div class="mb-3">
        <input v-model="searchQuery" type="text" class="form-control search-box" placeholder="Search task" />
      </div>

      <!-- Filters -->
      <div class="mb-3 d-flex justify-content-end">
        <!-- Favorite tasks filter -->
        <button
          :class="['btn', favoriteFilter ? 'btn-warning btn-sm' : 'btn-secondary btn-sm']"
          @click="toggleFavoriteFilter"
        >
          <i class="bi bi-star"></i> Favorites
        </button>
        
        <!-- Completed tasks filter -->
        <button
          :class="['btn', completedFilter ? 'btn-success btn-sm' : 'btn-secondary btn-sm']"
          @click="toggleCompletedFilter"
          style="margin-left: 10px;"
        >
          <i class="bi bi-check-circle"></i> Completed
        </button>

        <!-- Pending tasks filter -->
        <button
          :class="['btn', pendingFilter ? 'btn-danger btn-sm' : 'btn-secondary btn-sm']"
          @click="togglePendingFilter"
          style="margin-left: 10px;"
        >
          <i class="bi bi-x-circle"></i> Pending
        </button>
      </div>

      <!-- Tasks table -->
      <table class="table table-bordered table-hover">
        <thead>
          <tr>
            <th>Task</th>
            <th>Description</th>
            <th>Completed</th>
            <th>Favorites</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in filteredItems" :key="item.id">
            <td>{{ item.title }}</td>
            <td>{{ item.description }}</td>
            <td>
              <input type="checkbox" v-model="item.completed" @change="updateItem(item)" />
            </td>
            <td>
              <input type="checkbox" v-model="item.favorite" @change="updateFavorite(item)" />
            </td>
            <td>
              <button class="btn btn-warning" @click="editItem(item)">Edit</button>
              <button class="btn btn-danger ms-2" @click="deleteItem(item.id)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  
  <footer>
    <div class="container-fluid">
      <div class="row footer">
        <div class="col-md-12 text-center">
          <h1>Jose Luis Cáceres</h1>
          <h6>Interview for BASF</h6>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:8000';

const newItem = ref({
  title: '',
  description: '',
  completed: false,
  favorite: false
})

const searchQuery = ref('')
const items = ref([])
const favoriteFilter = ref(false)
const completedFilter = ref(false)
const pendingFilter = ref(false)  
const editingItem = ref(null)

const fetchItems = async () => {
  const response = await axios.get('/items')
  items.value = response.data.map(item => ({
    ...item,
    favorite: item.favorite === true
  }))
}

const filteredItems = computed(() => {
  let filtered = items.value.filter(item =>
    item.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    item.description.toLowerCase().includes(searchQuery.value.toLowerCase())
  )

  if (favoriteFilter.value) {
    filtered = filtered.filter(item => item.favorite)
  }
  
  if (completedFilter.value) { 
    filtered = filtered.filter(item => item.completed)
  }

  if (pendingFilter.value) { 
    filtered = filtered.filter(item => !item.completed)
  }

  return filtered
})

const addItem = async () => {
  try {
    const response = await axios.post('/items', newItem.value)
    items.value.push(response.data)
    newItem.value = { title: '', description: '', completed: false, favorite: false }
  } catch (error) {
    console.error('Error al agregar la tarea:', error)
  }
}

const deleteItem = async (id) => {
  await axios.delete(`/items/${id}`)
  items.value = items.value.filter(item => item.id !== id)
}

const updateItem = async (item) => {
  await axios.put(`/items/${item.id}`, item)
}

const updateFavorite = async (item) => {
  try {
    const response = await axios.put(`/items/${item.id}/favorite`, { favorite: item.favorite })
    console.log('Tarea actualizada:', response.data)
  } catch (error) {
    console.error('Error al actualizar la tarea:', error)
  }
}

const toggleFavoriteFilter = () => {
  favoriteFilter.value = !favoriteFilter.value
}

const toggleCompletedFilter = () => { 
  completedFilter.value = !completedFilter.value
}

const togglePendingFilter = () => { 
  pendingFilter.value = !pendingFilter.value
}

const editItem = (item) => {
  newItem.value = { ...item }
  editingItem.value = item
}

const saveItem = async () => {
  if (editingItem.value) {
    await axios.put(`/items/${editingItem.value.id}`, newItem.value)
    Object.assign(editingItem.value, newItem.value)
    editingItem.value = null
  } else {
    addItem()
  }
  newItem.value = { title: '', description: '', completed: false, favorite: false }
}

fetchItems()
</script>

<style scoped>
.hero {
  background-color: #f7f7f7;
  padding: 80px 0;
  text-align: center;
}
.hero-text {
  max-width: 600px;
  margin: 0 auto;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

.hero-text h1 {
  font-size: 50px;
  font-weight: bold;
}

.hero-text h3 {
  font-size: 24px;
  color: #888;
  margin-bottom: 20px;
  margin-top: 20px;
  padding: 20px;
}

.hero-text .btn {
  background-color: #3498db;
  color: white;
  padding: 12px 30px;
  margin-top: 20px;
  text-decoration: none;
}

.hero-text .btn:hover {
  background-color: #2980b9;
}

.container {
  max-width: 960px;
  margin: 0 auto;
}

.purple {
  color: #6104df;
}

.table {
  margin-top: 20px;
  width: 100%;
}

.table-bordered {
  border: 1px solid #ddd;
  border-radius: 10px;
}

.table-hover tbody tr:hover {
  background-color: #f1f1f1;
  cursor: pointer;
  transform: scale(1.02);
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.btn-primary {
  background-color: #3498db;
  color: white;
  border-radius: 5px;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.btn-primary:hover {
  background-color: #2980b9;
  transform: scale(1.05);
}

.btn-warning {
  background-color: #f39c12;
  color: white;
  border-radius: 5px;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.btn-warning:hover {
  background-color: #e67e22;
  transform: scale(1.05);
}

.btn-danger {
  background-color: #e74c3c;
  color: white;
  border-radius: 5px;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.btn-danger:hover {
  background-color: #c0392b;
  transform: scale(1.05);
}

.form-container {
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  background-color: white;
  border-radius: 8px;
}

.form-control {
  border-radius: 5px;
  transition: box-shadow 0.3s ease, border-color 0.3s ease;
}

.form-control:focus {
  box-shadow: 0 0 8px rgba(0, 123, 255, 0.6);
  border-color: #3498db;
}

.search-box {
  border-radius: 5px;
  transition: box-shadow 0.3s ease, border-color 0.3s ease;
}
  
  .input-group .form-control {
    margin-right: 10px;
  }
  
  .input-group button {
    background-color: #3498db;
    color: white;
    border: none;
    border-radius: 5px;
    transition: background-color 0.3s ease, transform 0.3s ease;
  }
  
  .input-group button:hover {
    background-color: #2980b9;
    transform: scale(1.05);
  }
  
  .mb-3 {
    margin-bottom: 20px;
  }
  
  .d-flex {
    display: flex;
  }
  
  .justify-content-end {
    justify-content: flex-end;
  }
  .footer {
    background-color: #2c3e50;
    padding: 40px 0;
    color: white;
  }
  
  .footer h1 {
    font-size: 36px;
  }
  
  .footer .social-links {
    list-style-type: none;
    padding: 0;
  }
  
  .footer .social-links li {
    display: inline-block;
    margin: 10px;
  }
  
  .footer .social-links a {
    color: #3498db;
    text-decoration: none;
  }
  
  .footer .social-links a:hover {
    color: #2980b9;
  }
    .table thead {
    background-color: #34495e; 
    color: rgb(187, 29, 29); 
    font-family: 'Roboto', sans-serif; 
    font-weight: 500; 
    }

    .table thead th {
    padding: 12px; 
    text-align: center; 
    }

    .table-bordered {
    border: 1px solid #b4b3b3;
    }
  </style>