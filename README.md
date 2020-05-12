![license](https://img.shields.io/github/license/mashape/apistatus.svg)


## Name of Project
- description

### Required Features
-
-
-

### Additional Features
-
-
-

## Prerequisite

- [Python3.6](https://www.python.org/downloads/release/python-365/)
- [Virtual Environment](https://virtualenv.pypa.io/en/stable/installation/)
- [Flask](http://flask.pocoo.org/)
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)

## Technologies & Languages

**Project management (Agile)** [https://www.pivotaltracker.com](url)

**Version control (Git)** [https://git-scm.com/](url)

**Version control (Flask)** [https://flask.palletsprojects.com/en/1.1.x/](url)

**Version control (Python)** [https://www.python.org/](url)

# Installation and Setup

Clone the repository below

```
git clone https://github.com/{username}/{repo_name}.git
```

### Create and activate a virtual environment

    virtualenv venv --python=python3.6

    source venv/bin/activate

### Install required Dependencies

    pip install -r requirements.txt

### Copy environment variable

    cp env.sample .env

### Load/refresh .environment variables

    source .env

## Running the application

```
python manage.py server
```


## Endpoints Available
 - update your available endpoints

| Method | Endpoint                        | Description                           | Roles         |
| ------ | ------------------------------- | ------------------------------------- | ------------  |
| POST   |        /auth/signup             | sign up a user                        | users         |
| POST   |        /auth/login              | log in  a user                        | users         |



## License

MIT
