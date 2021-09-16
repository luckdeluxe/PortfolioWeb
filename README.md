# Portfolio Web

_Personal portfolio web_

## Starting 🚀

_These instructions will allow you to get a copy of the project running on your local machine for development and testing purposes._

Look **Deployment** to know how to deploy the project.


### Pre requirements 

_A series of step-by-step examples that tells you what to run to get a development environment running_

_Clone the repository_

```
git clone https://github.com/luckdeluxe/portfolioweb.git && cd portfolioweb
```

_Create a virtual Python environment:_

```
python3 -m venv .venv
```

_Activate the virtual environment_

```
sorce .venv/bin/activate
```

### Installation 🔧

_What things do you need to install the software and how to install them_

_You can install the requirements.txt file recursively_
```
pip install requirements.txt
```
_If you have any errors in the above way you can install it manually_

```
pip install [dependency==version]
```

```
asgiref==3.4.1
astroid==2.6.5
dj-database-url==0.5.0
Django==3.2.3
gunicorn==20.1.0
isort==5.9.3
lazy-object-proxy==1.6.0
mccabe==0.6.1
Pillow==8.2.0
psycopg2-binary==2.9.1
pylint==2.9.6
python-decouple==3.4
pytz==2021.1
sqlparse==0.4.1
toml==0.10.2
wrapt==1.12.1

```

## Running the tests ⚙️

_Create database from models_

```
python3 manage.py makemigrations
python3 manage.py migrate
```

```
python3 manage.py runserver
```

