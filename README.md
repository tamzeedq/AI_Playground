# AI_Playground
An AI/ML playground made with Python to play and experiment with different models.


## Setting Up API Keys

**This project requires a personal OpenAI API token.** You can sign up for the API and get a key here, [Open AI API](https://openai.com/blog/openai-api).

To set up the environment variables for the API Keys, create a `.env` file in the project directory containing the following

```
OPENAI_API_KEY = INSERT_API_KEY_HERE 
```


## Virtual Environment

Running the project in a virtual environment may be ideal to avoid conflicts.

To create an environment, clone the repo and inside the directory run the following:

```
python -m venv env
```

**"env"** can be replaced with whatever you would like to name the environment.


After creating the environment run either of the following to activate the environment:

For Windows
```
env\Scripts\activate
```

For Unix or Mac OS
```
source env/bin/activate
```

## Dependencies

To install the required dependencies run the following either in the project directory or in a virtual environment:
```
pip install -r requirements.txt
```

## Run GUI
To run the GUI run the following either in the project directory or in a virtual environment:

```
python gui.py
```

Or:
```
python3 gui.py
```

