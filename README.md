#  My Portfolio App

This is a full-stack web application built using Flask.
Users can submit their contact details, which are stored in a database and displayed on a separate page.

---

##  Features

* Home page
* About page
* Contact form (user input)
* Save contacts to SQLite database
* View saved contacts
* Prevent duplicate email entries
* Docker support (containerized app)

---

##  Technologies Used

* Python
* Flask
* HTML & CSS
* SQLite (Database)
* Docker

---



##  Run Locally

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the app:

```bash
python app.py
```

3. Open in browser:

```bash
http://localhost:8080
```

---

##  Run with Docker

Build image:

```bash
docker build -t my-portfolio .
```

Run container:

```bash
docker run --name my-portfolio -p 8080:8080 -v $(pwd):/app my-portfolio
```

---

## Deployment

This app can be deployed using:

* Render (recommended, no card required)
* Google Cloud Run

---

## Notes

* SQLite database (`contacts.db`) is used for storing data
* Duplicate email entries are prevented
* When using Docker, volume mapping (`-v $(pwd):/app`) is used to persist data

---

##  Author

Nadeem Ahmad
Student & Beginner Developer 



