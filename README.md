# **BASF Technical - ToDo App**
### **Project Description**
This project is a to-do list application with a separate **frontend** and **backend architecture**.

The user must launch the backend and frontend separately in their local environment, both will connect once they are running.
Once the project is launched, the web application will be running on a local server **"localhost:3000"**.

The section where the proposed exercise is located is easy to understand. It is a page that loads a VUE component in charge of calling all the **CRUD processes** of the backend and displaying them in a list in a reactive way. In the component we can find the following functionality:
- **Create new task**: Allows the user to create new tasks from a name and description.
- **Delete task**: Allows the user to completely delete a task individually using a delete button found in the actions column.
- **Edit task**: The user can edit the task in two ways: marking it as a favorite and/or marking it as completed. All you have to do is check the boxes created for this purpose within each task.
- **Search tasks**: The user can dynamically and reactively search for the task based on its name by entering text in the Search input.
- **Filter favorite tasks**: The user will be able to filter the tasks to find the tasks that they have previously marked as favorites.

### **Structure**
**Backend**: API built with **Python** and **FastAPI** to handle task list CRUD operations.

**Frontend**: Application in **Vue.j**s that allows users to visually interact with the task list.

## **Prerequisites**

 1. **Python 3.9** or higher (for the backend)
 2. **Node.js** and **npm** (for the frontend in Vue)
 3. **PostgreSQL** configured and running (It is necessary to have PostgreSQL installed for this project and change the constants)
 4. **Docker**

## **Configuration and execution**

#### **Clone the repository**
  ```bash
  git clone <URL_of_the_repo>
	cd BASF_FS_TECHINT
  ```
 ## Deploy with Docker
 It does not work in an optimal way
 ####**1. Review Docker Configuration Files**
 Inside the project directory, make sure you have the following files:

- **docker-compose.yml**: File that defines all Docker services (database, backend, and frontend).
- **Dockerfile** (in the backend and frontend directory): Files to build the backend and frontend service images.
**wait-for-it.sh**: Script to make sure the database container is ready before starting the backend.

#### **2. Build and Start Containers**
In the project directory, run the following command to build and start containers using Docker Compose:
```bash
docker-compose up --build
```
This command will download the necessary images (if not available locally), build the custom images for the backend and frontend, and start the database, backend, and frontend containers.

#### **3. Accessing the Application**
Once the containers are up and running, you will be able to access the application in your browser.

- **Frontend (Vue.js)**: Go to http://localhost:3000 to see the user interface.
- **Backend (FastAPI)**: If you need to access the backend API directly, go to http://localhost:8000.
- **Database (PostgreSQL)**: The PostgreSQL database is accessible on port 5434. You can use tools like pgAdmin or any PostgreSQL client to connect with the following configuration:
- **Host**: localhost
- **Port**: 5434
- **User**: myuser
- **Password**: mypassword
- **Database**: todoapp

#### **4. View Container Logs**
If you need to view container logs for debugging or monitoring, you can run:
```bash
docker-compose logs
```
To view the logs for a specific service (for example, the frontend), you can use:
```bash
docker-compose logs-frontend
```

#### **5. Stopping Containers**
If you want to stop all containers, simply run the following command:
```bash
docker-compose down

```

## **Backend: FastAPI and PostgreSQL**

**Installation and Configuration**

1. Navigate to the **backend** folder:
```bash
cd backend
```
2. Create a **virtual environment** and install the dependencies:

```bash
python -m venv venv

venv\Scripts\activate # in Windows

source venv/bin/activate # in UNIX/Linux

pip install -r requirements.txt
```
#### Configure the **PostgreSQL** database:
You will need to have PostgreSQL installed on your computer
1. Create a database called **"todoapp"**.
2. In the file **src/constants/app_constants.py**, update the connection data in user and pwd:

```python
user = "<your_user>"
pwd = "<your_password>"
```
- Run the script **db_test.py** to test the connection to the database:
```bash
python db_test.py
```
- Start the **FastAPI** server:
```bash
uvicorn main:app --reload
```
The server will be available at http://localhost:8000 by default.

##### **API Endpoints**
The main endpoints are:

- **GET /items**: Returns the list of tasks.
- **POST /items**: Create a new task.
- **DELETE /items/{item_id}**: Delete a task.
- **PUT /items/{item_id}**: Updates the details of a task.
- **PUT /items/{item_id}/favorite**: Updates the favorite field of the task.

For more details, visit the documentation automatically generated by FastAPI while the server is running.

#### Backend Structure

```bash
#### Backend structure:
BASFTECHNICAL/
├── backend/
│   ├── src/
│   │   ├── blueprints/           # Contains FastAPI routes and drivers
│   │   ├── commons/              # Database configuration
│   │   ├── constants/            # App constants
│   │   ├── models/               # SQLAlchemy Models and Pydantic DTOs
│   │   ├── services/             # Business logic
│   │   └── utils/                # Aux functions
│   ├── venv/                     # Virtual Env
│   ├── main.py                   # FastAPI entry point
│   ├── db_test.py                # Script to test the connection to the database
│   ├── config.py                 # Connection settings
│   └── requirements.txt          # Python dependencies
```
## **Frontend: VUE3 and NUXT**

This project is the user interface of the BASF ToDo App, developed with **Nuxt.js 3** and **Vue.js**. It uses **Bootstrap** for visual design and **Axios** for communication with the backend.

#### **Facility**
1. **Clone the repository** and navigate to the **frontend** folder:
```bash
git clone [<URL_of_the_repo>]
cd frontend
```
2. Install the necessary **dependencies**: (Use the command depending on the package manager your computer uses.)
```bash
# npm
npm install
# pnpm
pnpm install
# yarn
yarn install
# bun
bun install
```
#### **Development Use**
To **start the development server** at http://localhost:3000:
```bash
# npm
npm run dev
# pnpm
pnpm dev
# yarn
yarn dev
# bun
bun run dev
```
#### **Deployment in production**
To **build the application for production**:
```bash
# npm
npm run build
# pnpm
pnpm build
# yarn
yarn build
# bun
bun run build
```
#### **Folder and File Structure**
The project structure is organized into the following main folders and files:

- **assets/**: Images and other static files used in the application.
- **components/**: Reusable components, such as Navbar.vue.
- **pages/**: Contains the main views of the application, such as index.vue and list.vue.
- **public/**: Public files accessible from the server root.
- **.nuxt/**, .output/, node_modules/: Automatically generated output directories and dependencies (ignored in .gitignore).
- **nuxt.config.ts**: Nuxt configuration file, where custom paths, styles and other settings are specified.
- **app.vue**: Application root file.
- **package.json**: Information about the application's dependencies and scripts.

#### **Key Files**

##### **.gitignore**
The .gitignore file excludes automatically generated files and folders, such as .nuxt, node_modules, log files, and local environment variables, from version control.

##### **app.vue**
This file establishes the basic layout of the application, which includes the **Navbar** component and settings for internal navigation (NuxtPage).
```html
<template>
  <Navbar />
  <NuxtPage />
</template>
```

##### **nuxt.config.ts**
This is where routes, CSS and other Nuxt options are configured. This file includes Bootstrap and establishes an automatic root (/) redirection to the /home page.

```javascript
export default defineNuxtConfig({
    compatibilityDate: '2024-04-03',
    devtools: { enabled: true },
    router: {
      extendRoutes(routes) {
        routes.push({
          path: '/',
          redirect: '/home',
        });
      },
    },
    css: [
      'bootstrap/dist/css/bootstrap.min.css'
    ]
  })  
```
##### **package.json**
This file manages the project's dependencies and scripts. Key dependencies include:

**Nuxt**: Main framework.
**Bootstrap**: CSS framework.
**Axios**: HTTP client to connect to the backend.


##### **tsconfig.json**
Extends Nuxt's TypeScript configuration, providing support for TypeScript in the application.

###End
