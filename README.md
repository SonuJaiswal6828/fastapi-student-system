# FastAPI Student Management System

A simple, production-style backend API built with **FastAPI** and **MySQL** for managing students.  
This project demonstrates clean REST APIs, proper error handling, and a structured backend architecture.

---

## 🚀 Features

- Create, Read, Update, Delete (CRUD) for students  
- Proper RESTful routes  
- Input validation (400 Bad Request)  
- Not found handling (404)  
- Server error handling (500)  
- MySQL database integration  
- Environment-based configuration using `.env`  
- Clean folder structure (routes, models, db)

---

## 🧱 Tech Stack

- **Backend:** FastAPI (Python)  
- **Database:** MySQL  
- **ORM/Driver:** mysql-connector-python  
- **Config:** python-dotenv (for environment variables)  
- **Version Control:** Git + GitHub  

---

## 📁 Project Structure


fastapi-student-system/                             
│                                  
├── app/                           
│ ├── main.py                                   
│ ├── db.py                             
│ ├── models.py                                                                                                     
│ └── routes/                                         
│ ├── init.py                             
│ └── students.py                           
│                                     
├── .env.example                                  
├── .gitignore                                 
└── README.md                                                                   


## ⚙️ Setup & Run (Local)

### 1️⃣ Clone the repository

git clone https://github.com/<your-username>/fastapi-student-system.git
cd fastapi-student-system

### 2️⃣ Create virtual environment & install dependencies
python -m venv venv
venv\Scripts\activate    # Windows
pip install fastapi uvicorn mysql-connector-python python-dotenv

### 3️⃣ Create .env file
copy .env.example .env   # Windows

Update .env with your DB credentials:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password_here
DB_NAME=your_db_name

⚠️ Do NOT commit .env file to GitHub. It contains secrets.

### 4️⃣ Create MySQL table                    
CREATE TABLE students (                          
  id INT AUTO_INCREMENT PRIMARY KEY,                        
  name VARCHAR(100) NOT NULL,                                         
  age INT NOT NULL,                                                   
  marks INT NOT NULL,                              
  result VARCHAR(10) NOT NULL                   
);                                            

### 5️⃣ Run the server
uvicorn app.main:app --reload

Server will start at:

http://127.0.0.1:8000

Swagger docs:

http://127.0.0.1:8000/docs

### 📌 API Endpoints

| Method | Endpoint       | Description        |
| ------ | -------------- | ------------------ |
| GET    | /students      | Get all students   |
| GET    | /students/{id} | Get student by ID  |
| POST   | /students      | Create new student |
| PUT    | /students/{id} | Update student     |
| DELETE | /students/{id} | Delete student     |

##🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss what you would like to change.
