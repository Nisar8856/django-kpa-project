# Django KPA API Assignment

## Setup Instructions

1. Create PostgreSQL DB `kpadb`.
2. Update the `.env` file with your DB credentials.
3. Run the following:

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## API Endpoints

- POST `/api/formdata/` - Submit form data
- GET `/api/formdata/<id>/` - Get form data by ID

## Tech Stack

- Python + Django REST Framework
- PostgreSQL
- dotenv for environment variables
