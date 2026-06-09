# Learning Log

A Django web app for tracking what you're learning. Create topics, write journal entries, search your notes.

## Live Demo

🔗 http://89.169.173.3/

## Screenshots

![register](screenshots/register.png) 
![home](screenshots/home.png) 
![topics](screenshots/topics.png) 
![entries](screenshots/entries.png)

## Features

- Register and log in to your personal account
- Create, view, and delete learning topics
- Add and delete journal entries for each topic
- Search topics

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=flat&logo=bootstrap&logoColor=white)

- Django 6
- Bootstrap 5
- SQLite
- Gunicorn + Nginx (deployed on VPS)

## Setup

```bash
git clone https://github.com/useinov09/learning_log
cd learning_log
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## What I Learned

- Full Django project structure: models, views, URLs, templates
- User authentication and per-user data isolation
- Deploying a Django app to a VPS with Gunicorn + Nginx
- Using Bootstrap to build a clean responsive UI without custom CSS
