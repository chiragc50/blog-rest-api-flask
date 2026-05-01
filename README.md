# 🚀 Flask Blog API (Educational Project)

## 📌 Overview
This is a **fully self-designed and self-developed REST API project** built using Flask.  
The purpose of this project is to **demonstrate my backend development skills, API design knowledge, and understanding of authentication & security concepts**.

This project is purely **educational** and was created to showcase my capabilities to potential employers.

---

## 🧠 Key Highlights
- Designed and implemented **from scratch**
- Clean and structured **RESTful API architecture**
- Implements **JWT Authentication**
- Secure password hashing using `pbkdf2_sha256`
- Token revocation (logout mechanism)
- Pagination and filtering support
- Rate limiting for API protection
- Modular and scalable code structure

---

## ⚙️ Tech Stack
- **Backend:** Flask  
- **Database:** SQLAlchemy ORM  
- **Authentication:** JWT (Flask-JWT-Extended)  
- **Validation:** Marshmallow  
- **Migrations:** Flask-Migrate  
- **Rate Limiting:** Flask-Limiter  
- **API Docs:** Swagger UI (OpenAPI)

---

## 🗂️ Project Structure
```
blog-rest-api-flask/
│
├── api/
│ ├── models/
│ │ ├── User.py
│ │ ├── Post.py
│ │ └── RevokedToken.py
│ │
│ ├── resources/
│ │ ├── users.py
│ │ └── posts.py
│ │
│ ├── schemas/
│ │ ├── user_schema.py
│ │ └── post_schema.py
│ │
│ ├── db.py
│ ├── extensions.py
│ └── init.py
│
├── .dockerignore
├── .env.example
├── .flaskenv
├── .gitignore
├── Dockerfile
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 🔐 Authentication Flow
- User Signup → Create account  
- User Login → Receive JWT token  
- Protected Routes → Require JWT  
- Logout → Token gets revoked and stored  

---

# Example:
- Login returns access token
- Token is required in headers for protected enpoints

---

## 📡 API Features

### 👤 User Endpoints
- `POST /api/v1/users/signup` → Register user  
- `POST /api/v1/users/login` → Authenticate user  
- `POST /api/v1/users/logout` → Revoke token  

### 📝 Post Endpoints
- `GET /api/v1/posts/` → Get posts (with pagination & filters)  
- `POST /api/v1/posts/` → Create post  
- `GET /api/v1/posts/<id>` → Get single post  
- `PUT /api/v1/posts/<id>` → Update post  
- `DELETE /api/v1/posts/<id>` → Delete post  

---

## Core Implementation Details
# Models
- User model with relationship to posts `User`
- Post model with privacy control and timestamps `Post`
- Revoked token model for logout security `RevokedToken`

# API Logic
- Post filtering and pagination implemented in routes `posts`
- Authentication and token handling logic `users`

# Schemas
- Input validation using marshmallow

# App Configuration
- Modular app factory pattern used `__init__`
- Extensions initialized seperately for scalability `extensions`

---
## 🛡️ Security Features
- Password hashing (no plain-text storage)
- JWT-based authentication
- Token revocation (blacklisting)
- Rate limiting to prevent abuse
- Input validation for all endpoints

---

## 🚀 How to Run

### 1. Clone Repository
```bash
git clone https://github.com/chiragc50/blog-rest-api-flask.git
cd blog-rest-api-flask
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Variables
Create a `.env` file:
```
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
```

### 5. Run Migrations
```bash
flask db init
flask db migrate
flask db upgrade
```

### 6. Run Server
```bash
flask run
```

---

## 📖 API Documentation
Swagger UI available at:
```
/swagger-ui
```

---

## ⚠️ Disclaimer
This project is developed **entirely by me for educational and portfolio purposes**.  
It is intended to demonstrate backend development, API design, and security concepts.

This project is **not production-ready** and should not be used in real-world applications without proper security reviews, testing, and improvements.

This software is provided **"as is"**, without any warranties of any kind, express or implied.
I am **not liable for any misuse, damage, data loss, or security vulnerabilities, or other issues** arising from the use of this project.

Any use of this project is done **at your own risk**.

---

## License
- This project is licensed under the **MIT License**.
- See the `LICENSE` file for more details

---


## 📌 Copyright & Usage
- This project intended for educational and portfolio purposes. 
- Feel free to explore, use and learn from the code 

- This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🎯 Purpose
This project reflects my ability to:
- Design real-world APIs  
- Implement authentication and security  
- Write clean, maintainable backend code  
- Understand scalable architecture  
