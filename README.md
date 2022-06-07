# Combined Blog
Combined Blog Project for Django Catch Up Session - Moringa School

## SetUp Instructions

- Go to the `.env.sample` file and configure the neccessary environment variable values then rename the file to `.env`
- Create a virtual environment (`python -m venv virtual`)
- Activate your virtual environment --> on linux run (`source virtual/bin/activate`) / on windows run (`source virtual/Scripts/activate`)
- Make your migrations (`python manage.py makemigrations`)
- Migrate (`python manage.py migrate`)
- Run the server (`python manage.py runserver`)