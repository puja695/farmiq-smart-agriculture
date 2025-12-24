# 🌱 FarmIQ 

FarmIQ is a **FastAPI-powered REST API** designed to manage agricultural data efficiently.
It provides structured APIs for handling farmers, crops, and related records using a clean backend architecture with SQLite.

This backend can be easily extended into a **full-stack AgriTech platform** with analytics, ML models, and dashboards.

---

## 🚀 Tech Stack

* **Backend Framework:** FastAPI
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Validation:** Pydantic
* **Server:** Uvicorn
* **Language:** Python 3.10+

---

## 📂 Project Structure

```
farmiq-backend/
│
├── main.py          # FastAPI app entry point
├── models.py        # Database models (SQLAlchemy)
├── schemas.py       # Pydantic schemas
├── crud.py          # CRUD operations
├── database.py      # Database connection & session
├── requirements.txt # Project dependencies
├── farmiq.db        # SQLite database
└── .env             # Environment variables
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/farmiq-backend.git
cd farmiq-backend
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file if not already present:

```env
DATABASE_URL=sqlite:///./farmiq.db
```

---

## ▶️ Running the Server

```bash
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 📘 API Documentation

FastAPI provides **automatic interactive docs**:

* **Swagger UI:**
  👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

* **ReDoc:**
  👉 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧠 Features

* RESTful API architecture
* SQLite database integration
* Modular CRUD operations
* Data validation using Pydantic
* Easy to scale with ML models & analytics
* Clean separation of concerns

---

## 🔮 Future Enhancements

* 🌦 Weather & soil data integration
* 🤖 ML-based crop yield prediction
* 📊 Farmer dashboard (React / Next.js)
* 🔐 Authentication & role-based access
* ☁️ Cloud database (PostgreSQL / MySQL)

---

## 🧑‍💻 Ideal Use Cases

* AgriTech platforms
* Smart farming dashboards
* Hackathons & research projects
* AI/ML integration for agriculture
