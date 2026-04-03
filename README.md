---

```markdown
# Flask REST API for Blog Posts

This project is a **RESTful API** built using **Flask**, designed for educational to demonstrate backend development skills. It includes user authentication, CRUD operations for blog posts, and token revocation with rate limiting and schema validation.

---

## 🚀 Features

- **User authentication (signup/login/logout)**
- **JWT-based access control**
- **Rate limiting** via Flask-Limiter
- **Role-based post access (public/private)**
- **Schema validation** with Marshmallow
- **Database migrations** using Flask-Migrate
- **Secure password hashing** via Passlib
- **OpenAPI documentation** with Flask-Smorest
- **Dockerized** for production deployment
- **Gunicorn-ready** for WSGI hosting

---

## 🧠 Tech Stack

- **Flask**
- **Flask-SQLAlchemy**
- **Flask-JWT-Extended**
- **Flask-Smorest**
- **Flask-Limiter**
- **Marshmallow**
- **Passlib**
- **Gunicorn**
- **PostgreSQL (or any SQL DB)**
- **Docker**

---

## 📁 Project Structure

```

.
├── api/
│   ├── **init**.py
│   ├── db.py
│   ├── extensions.py
│   ├── models/
│   │   ├── User.py
│   │   ├── Post.py
│   │   └── RevokedToken.py
│   ├── resources/
│   │   ├── users.py
│   │   └── posts.py
│   └── schemas/
│       ├── user_schema.py
│       └── post_schema.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .env

```

---

## 📦 Installation

### 🔧 Prerequisites

- Python 3.10+
- PostgreSQL or compatible SQL database
- [Docker](https://www.docker.com/) (for containerized deployment)
- `pip`, `virtualenv` or `venv`

### 🧪 Local Development Setup

1. **Clone the repository**:

```bash
git clone https://https://github.com/chiragsd94/Flask-Blog-RestApi.git
```

cd Flask-Blog-RestApi

````

2. **Create a virtual environment**:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Configure environment**:

Create a `.env` file:

```env
DATABASE_URL=sqlite:///data.db  # or your Postgres URL
SECRET_KEY=your-secret
JWT_SECRET_KEY=your-jwt-secret
```

5. **Run database migrations**:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

6. **Run the application**:

```bash
flask run
```

The API will be available at `http://localhost:5000`.

---

## 🐳 Docker Deployment

1. **Build Docker image**:

```bash
docker build -t blog-api .
```

2. **Run the container**:

```bash
docker run -d -p 80:5000 --env-file .env blog-api
```

> The API will now be available at `http://localhost`.

---

## 🧪 Example Endpoints

### 🔐 User Authentication

* **Signup**: `POST /api/v1/users/signup`
* **Login**: `POST /api/v1/users/login`
* **Logout**: `POST /api/v1/users/logout` (Requires JWT)

### 📝 Posts

* **Create Post**: `POST /api/v1/posts/` *(JWT required)*
* **Get Posts**: `GET /api/v1/posts/?is_private=true/false&page=1` *(JWT required)*
* **Get Post**: `GET /api/v1/posts/<post_id>` *(JWT required)*
* **Update Post**: `PUT /api/v1/posts/<post_id>` *(JWT required)*
* **Delete Post**: `DELETE /api/v1/posts/<post_id>` *(JWT required)*

---

## 📚 API Documentation

Once the app is running, OpenAPI (Swagger UI) is available at:

```
http://localhost:5000/swagger-ui
```

---

## 🛡 Disclaimer

> This project is built for **educational purposes only** and to showcase my backend development skills to potential employers.
> I do not claim ownership over any external libraries or dependencies used in this project.
>**I am not liable for any loss, damage, data breach, misuse, or legal consequences resulting from the use, deployment, or modification of this code. Use this project at your own risk.**
> **This API is not intended for production use without further security audits and testing.**

---

## 👨‍💻 Author

**Chirag SD**
GitHub: \chiragsd94
Email: \[[s.chirag.danavendra@gmail.com](mailto:s.chirag.danavendra@gmail.com)]

---

## 📃 License

This project is provided **as-is** without any warranty. All rights belong to their respective owners. You're free to fork, modify, or use it for learning.

```

---

```
````
