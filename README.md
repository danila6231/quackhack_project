# Promptly Puzzled

A game where you guess the prompt given an image.  Compete with your friends to see who is the best prompt guesser!

## Prerequisites

The following are required to build and run the project:

* [Python 3](https://www.python.org/downloads/)
* [Node.js](https://nodejs.org/en/download/prebuilt-installer/current) - Used to build and package Javascript files


## Installation

To get the virtual environment set up, type in the shell:

```bash
python -m venv venv
```

On **Windows**:

```bash
source venv/Scripts/activate
```

On **Unix**:

```bash
source venv/bin/activate
```

Then install the requirements:

```bash
pip install -r requirements.txt
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
python ./manage.py makemigrations
python ./manage.py migrate
python ./manage.py runserver
```

## Setting up OpenAI key or any other ai key
Run the following first in the same window you plan to run the app in:
```bash
export OPENAI_KEY=<your-key-here>
```

Run the following to check if the variable has been set 
```bash
echo $OPENAI_KEY
```
The terminal should output <your-key-here>


## How the game works

Player 1 enters a prompt which is used to generate an image that is shown to player 2

Player 2 uses the image to try and guess what the prompt was

Points are assigned bases on how many words in the guess match with thte original prompt.

![Alt Text for the Image](/prompt_guesser/images/man_boxing_bear.png)

![Alt Text for the Image](/prompt_guesser/images/Hagrid1.png)

![Alt Text for the Image](/prompt_guesser/images/Hagrid2.png)
