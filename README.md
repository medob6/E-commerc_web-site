## E-commerce Store API (Django + DRF)

Django REST API backend for a simple e-commerce store with **products**, **users**, **orders**, and **authentication**.

> Note: This repository’s README previously contained duplicated content and some outdated references. It has been cleaned up and simplified.

---

## Features

- Products & categories
- User authentication
- Orders
- Admin panel

## Tech stack

- Python / Django
- Django REST Framework
- SQLite (dev) or MySQL (optional)

---

## Project structure (high level)

- `manage.py` — Django entry point
- `storefont/settings.py` — project settings
- `store/` — store app (products, customers, addresses, etc.)
- `tags/` — generic tagging app

---

## Quick start (local development)

### 1) Prerequisites

- Python 3.10+ recommended
- `pip` and `venv` (or `pipenv`)

On Debian/Ubuntu:

```sh
sudo apt update
sudo apt install -y python3 python3-venv python3-pip build-essential
# optional for MySQL backend:
sudo apt install -y default-libmysqlclient-dev
```

### 2) Create a virtual environment

Using `venv`:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Or using `pipenv`:

```sh
python3 -m pip install --user pipenv
export PATH="$HOME/.local/bin:$PATH"
pipenv install --dev
pipenv shell
```

### 3) Install dependencies

If you are using `pipenv`, dependencies are installed in the previous step.

If you are using `pip` + `requirements.txt` (if present in your repo):

```sh
pip install -r requirements.txt
```

### 4) Configure the database

By default, Django often uses SQLite for development. If your project is configured for MySQL by default and you want to run quickly on SQLite, update `storefont/settings.py`:

```py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

### 5) Run migrations and start the server

```sh
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## Common commands

```sh
# run tests
python manage.py test

# create migrations
python manage.py makemigrations

# apply migrations
python manage.py migrate
```

---

## API documentation

If you have Swagger/OpenAPI enabled, add the URL here (for example `/swagger/` or `/api/schema/swagger-ui/`).

---

## Contributing

1. Fork the repo
2. Create a feature branch
3. Open a pull request
