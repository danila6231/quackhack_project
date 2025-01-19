# Prompt Guesser

A game where you guess the prompt given an image.  Compete with your friends to see who is the best prompt guesser!

## Prerequisites

The following are required to build and run the project:

* [Python 3](https://www.python.org/downloads/)
* [Node.js](https://nodejs.org/en/download/prebuilt-installer/current) - Used to build and package Javascript files


## Installation

To get the virtual environment set up, type in the shell:

```bash
python -m venv venv
source venv/Scripts/activate
```

You should see (venv) pop up in your terminal and set up the environment.

After this is complete, set up the front end environment by switching to the `frontend` directory:

```bash
cd frontend
```

Then install the required Node.js packages:

```bash
npm i
```

Finally build the static page

```bash
npm run build
```


## Running the server

In order to run the backend erver execute the following:

```bash
$ python ./manage.py migrate
$ python ./manage.py runserver
```

