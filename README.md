# Work Wize

______________________ 

## Description

Workwize is a fully integrated,  project that represents  the skills I've learned in the software engineering Bootcamp. It's a project and task management system designed for businesses and teams to streamline workflows efficiently. The application allows users to create workspaces, manage tasks, assign team members, and monitor progress through an interactive dashboard. The backend was developed using Python, the Django REST framework (DRF), and PostgreSQL, while the frontend was built using React and Tailwind CSS, with JWT authentication for secure access.

## ✅ Technologies Used

| Area          | Technologies |
|---------------|--------------|
| **Backend**   | Python, Django REST Framework (DRF), PostgreSQL |
| **Frontend**  | React, Tailwind CSS |
| **Dev Tools** | Git, GitHub, Postman |


## 🔗 Back End Repository

You can find the Backend source code here:  
👉 [Backend Repository](https://github.com/AbrarAlabbad77/workWize_backend)
👉 [Frontend Repository](https://github.com/AbrarAlabbad77/workWize_frontend)

---

## ✅ Planning

### 📌 Entity Relationship Diagram (ERD)
![ERD Diagram](images/ERD.png)

# RESTful Routing 
## Routing Table (Server/Backend) 
---Projects---
| Method | Endpoint            | Description             |
| ------ | -----------------   | ------------------------|
| GET    | `/api/projects`     | Get all projects        |
| POST   | `/api/projects`     | Create a new project.   |
| GET    | `/api/projects/:id` | Get specific project    |
| PUT    | `/api/projects/:id` | Update aspecific project|
| DELETE | `/api/projects/:id` | Delete aspecific project|

---Task---
| Method | Endpoint                         | Description                   | 
| ------ | ------------------------------   | ----------------------------- | 
| GET    | `/api/projects/:projectId/tasks` | Get all tasks for a project   | 
| POST   | `/api/projects/:projectId/tasks` | Create a task under a project | 
| GET    | `/api/tasks/:id`                 | Get specific task             | 
| PUT    | `/api/tasks/:id`                 | Update specific task          | 
| DELETE | `/api/tasks/:id`                 | Delete specific task          | 


---Team Member---
| Method | Endpoint                     | Description                    | 
| ------ | --------------------------   | ------------------------------ | 
| GET    | `/api/tasks/:taskId/members` | Get members assigned to a task | 
| POST   | `/api/tasks/:taskId/members` | Add a member to a task         | 
| PUT    | `/api/members/:id`           | Update member details          | 
| DELETE | `/api/members/:id`           | Remove a member                |

---Manager---
| Method | Endpoint            | Description             | CRUD   |
| ------ | ------------------- | ----------------------- | ------ |
| GET    | `/api/managers`     | Get all managers        | Read   |
| POST   | `/api/managers`     | Create a new manager    | Create |
| GET    | `/api/managers/:id` | Get specific manager    | Read   |
| PUT    | `/api/managers/:id` | Update specific manager | Update |
| DELETE | `/api/managers/:id` | Delete specific manager | Delete |


## Routing Table (Client/Frontend)
| **Path**                      | **Component**     | **Description**                                 |
| ----------------------------- | ----------------- | ----------------------------------------------- |
| `/landhome`                   | `<LandPage />`    | Landing page introducing the platform           |
| `/aboutUs`                    | `<AboutUs />`     | About page with company or team information     |
| `/signup`                     | `<Signup1 />`     | User registration page                          |
| `/login`                      | `<Login />`       | User login page                                 |
| `/newspace`                   | `<NewProject />`  | Create a new workspace or project               |
| `/home`                       | `<Home />`        | Main dashboard or home page after login         |
| `/spaces/:project_id`         | `<SpaceDetail />` | View details of a specific workspace or project |
| `/spaces/:project_id/newtask` | `<NewTask />`     | Create a new task inside a specific workspace   |


## IceBox Features
1. Add comments model
2. user can add comments to specific Task 
3. DasshBoard 
4. Add graph in DasshBoard showing task with high priority 
5. Add graph in DasshBoard showing task that due soon 
6. Add Team model
7. Add group of uers to one team
8. Add Profile 
9. Add about me page
10. Add notification model
11. Add calander  
