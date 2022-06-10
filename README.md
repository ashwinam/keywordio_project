# keywordio_project (Library Management)

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/ashwinam/keywordio_project.git
$ cd keywordio_project
```

Create a virtual environment, install dependencies and activate it (here i use pipenv virtual environment):

```sh
$ pipenv install
$ pipenv shell
```
Note the `(keywordio_project<some_gibrish_thing>)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `pipenv`.

Once `pipenv` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
