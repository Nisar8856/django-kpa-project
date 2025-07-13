
# 🚀 KPA Project – Django REST API with PostgreSQL

A complete backend project built using **Django**, **PostgreSQL**, and **Django REST Framework**.  
Includes a fully functional **admin panel**, tested APIs via **Postman**, and deployed on **Render**.

---

## 📌 Features

- ✅ Create and fetch form data via REST API
- ✅ Admin panel to manage form submissions
- ✅ PostgreSQL database integration
- ✅ Render deployment for live access
- ✅ Environment variables handled securely
- ✅ Tested with Swagger UI & Postman

---

## 🔧 Tech Stack

| Tech             | Description                        |
|------------------|------------------------------------|
| Django           | Web Framework (Backend)            |
| Django REST Framework | API Creation                    |
| PostgreSQL       | Relational Database                |
| Render           | Deployment & Hosting               |
| Postman          | API Testing                        |
| Git & GitHub     | Version Control                    |

---

## 📁 API Endpoints

| Method | Endpoint              | Description         |
|--------|------------------------|---------------------|
| GET    | `/api/formdata/`      | List all records    |
| POST   | `/api/formdata/`      | Create new record   |
| GET    | `/admin/`             | Admin login panel   |

---

## 📸 Screenshots

### ✅ Swagger UI - FastAPI GET Response
![UI](https://github.com/user-attachments/assets/a80f29e9-a089-4859-b1c1-206caf43347f)

### ✅ Postman - API Test
![Postman](https://github.com/user-attachments/assets/475f33f1-7b23-4c47-b16a-3aa2118ad139)

### ✅ Render Deployment
![Render](https://github.com/user-attachments/assets/b075c665-4805-457d-ac6e-7fc3fd08c0cd)

### Django Admin Panel
![Pane](https://github.com/user-attachments/assets/c5791e34-5567-4a67-b986-bbdab435ec51)

---

## 🚀 Deployment (Render)

- Site: [https://django-kpa-project.onrender.com](https://django-kpa-project.onrender.com)
- Repo: [GitHub – django-kpa-project](https://github.com/Nisar8856/django-kpa-project)

---

## 💡 How to Run Locally

```bash
git clone https://github.com/Nisar8856/django-kpa-project.git
cd django-kpa-project
python -m venv env
env\Scripts\activate    # For Windows
pip install -r requirements.txt
