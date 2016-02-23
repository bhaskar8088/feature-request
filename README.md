Feature Request
===============

Installation:
-------------
1. Clone the repo

        git clone git@github.com:bhaskar8088/feature-request.git

2. Create a virtual environment

        mkvirtual envname

2. Install requirements

        pip install -r requirements.txt

3. Run migrations

        python manage.py migrate

4. Create a super user and visit admin page to see features requests and any other admin data.

        python manage.py createsuperuser

5. Run the server and access website at http://localhost:8000

        python manage.py runserver