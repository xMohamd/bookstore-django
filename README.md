# Simple book store using Django and tailwindcss

## Demo

https://github.com/xMohamd/bookstore-django/assets/10786768/54adbd8c-d286-4e8c-bc3d-ec4c60619402

## Installation

1. Clone the repository

```bash
git clone https://github.com/xMohamd/bookstore-django.git
cd bookstore-django
```

2. Create a virtual environment (optional but recommended)

```bash
python -m venv choose-a-name
source choose-a-name/bin/activate
```

2. Install the requirements

```bash
pip install -r requirements.txt
```

3. Check Database settings in `bookstore/settings.py` and make necessary changes if needed.

4. Run the migrations

```bash
python manage.py migrate
```

5. Run the server

```bash
python manage.py runserver
```

6. Visit `http://localhost:8000` in your browser

## Features

- List books
- View book details
- Add books
- Update books
- Delete books
- Tailwindcss for styling
- Responsive design
