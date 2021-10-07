# lets-learn-to-code

1. Open PyCharm
2. Select 'Get from VCS'
3. Select Version control 'Git', url 'https://github.com/lomittable/lets-learn-to-code.git', directory wherever you'd like (mine lives in /Users/lauren/CODE)
4. In PyCharm, open terminal. Run `python3 --version` to ensure python3 installed then `python3 -m venv env` to create your virtual environment inside your lets-learn-to-code directory
5. Activate virtual enviroment: `source env/bin/activate`
6. Install Django: `python3 -m pip install django`
7. Install requirements: `pip install -r requirements.txt`
8. Start your server: `python3 manage.py runserver`
9. Take down server with "Ctrl + C" then run `python3 manage.py migrate`
10. Create super user: `python manage.py createsuperuser` - I like to use 'admin' and 'password'

