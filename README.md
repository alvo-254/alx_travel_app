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

# 🧳 ALX Travel App — Milestone 2: Database Modeling and Seeding

This project is part of the ALX Backend Specialization and focuses on building core backend functionality using Django. It involves creating models, serializers, and a custom seeder command for a travel booking application.

---

## 📁 Project Structure

alx_travel_app_0x00/
├── alx_travel_app/
│ ├── settings.py
│ └── urls.py
├── listings/
│ ├── models.py
│ ├── serializers.py
│ └── management/
│ └── commands/
│ └── seed.py

markdown
Copy
Edit

---

## 📌 Features Implemented

### ✅ Models (`listings/models.py`)
- **Listing**: Represents a travel destination or place to stay.
- **Booking**: Represents a user's reservation for a listing.
- **Review**: Represents user feedback on a listing.

### ✅ Serializers (`listings/serializers.py`)
- `ListingSerializer`: Serializes listing data for the API.
- `BookingSerializer`: Serializes booking data.

### ✅ Seeder Script (`listings/management/commands/seed.py`)
- Populates the database with sample data for listings.
- Easily run using:
  ```bash
  python manage.py seed
🚀 How to Run Locally
Clone the repo:

bash
Copy
Edit
git clone https://github.com/alvo-254/alx_travel_app.git
cd alx_travel_app/alx_travel_app_0x00
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
.\venv\Scripts\activate   # For Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Apply migrations:

bash
Copy
Edit
python manage.py migrate
Run the seeder:

bash
Copy
Edit
python manage.py seed
Start the server:

bash
Copy
Edit
python manage.py runserver
🔍 Endpoints Overview
API Root: /api/listings/ (if configured with routers)

Admin: /admin/

📚 Milestone Objectives
 Define models with relationships and constraints.

 Create serializers for API representation.

 Implement and test a custom seeding script.

💡 Author
ALX Student — alvo-254

yaml
Copy
Edit

---

### ✅ Next Step:
- Save this as `README.md` in the root of your `alx_travel_app_0x00` project.
- Commit and push it:
  ```bash
  git add README.md
  git commit -m "Improve README for Milestone 2"
  git push
