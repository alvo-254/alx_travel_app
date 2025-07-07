# 🧭 ALX Travel App

A scalable travel listing platform built with **Django**, **MySQL**, and **Swagger**, designed as part of the ALX Software Engineering program.

---

## 🚀 Features

- ✅ User-friendly REST API
- ✅ MySQL-backed scalable database
- ✅ Swagger (drf-yasg) for live API documentation
- ✅ Environment variable management via `.env`
- ✅ Modular project structure ready for production

---

## 📦 Tech Stack

- **Backend:** Django 5.x
- **Database:** MySQL 9.x
- **API Docs:** Swagger UI via `drf-yasg`
- **Environment Config:** `django-environ`
- **Task Queue (Planned):** Celery + RabbitMQ

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/alx_travel_app.git
cd alx_travel_app
2. Set Up Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/Scripts/activate  # On Windows
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
Make sure MySQL is installed and running.

4. Configure .env
Create a .env file at the root:

env
Copy
Edit
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=alx_travel_db
DB_USER=root
DB_PASSWORD=your-mysql-password
DB_HOST=localhost
DB_PORT=3306
🧱 Run Migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
🧪 Run the Server
bash
Copy
Edit
python manage.py runserver
Visit:

http://127.0.0.1:8000/admin – Django Admin

http://127.0.0.1:8000/swagger – API Docs (Swagger UI)

