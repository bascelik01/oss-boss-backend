# Technique Collector Backend

## Prerequisites
- Python 3.11+ (project `Pipfile` targets 3.14 but 3.11/3.12 also work locally)
- Pipenv (`pip install pipenv` or `brew install pipenv`)

## Setup & Run (Pipenv)
```bash
# Install deps
pipenv install

# Activate shell (optional if you prefer pipenv run)
pipenv shell

# Apply migrations
python manage.py migrate

# Create an admin (optional)
python manage.py createsuperuser

# Start dev server
python manage.py runserver
```

Without activating the shell:
```bash
pipenv install
pipenv run python manage.py migrate
pipenv run python manage.py runserver
```

## Endpoints (summary)
- Auth: `POST /users/register/`, `POST /users/login/`, `GET /users/token/refresh/`
- Categories (read-only): `GET /categories/`, `GET /categories/<id>/`
- Techniques (auth required): `GET/POST /techniques/`, `GET/PATCH/DELETE /techniques/<id>/`
