# Import necessary modules
from flask import Flask, render_template, url_for, request
from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
import dill as pickle
import warnings

warnings.filterwarnings("ignore")


try:
    interpreter = pickle.load(open('data/rasa_interpreter.sav', 'rb'))
except:
    # Create args dictionary
    args = dict({"pipeline":"spacy_sklearn"})

    # Create a configuration and trainer
    config = RasaNLUConfig(cmdline_args=args)
    trainer = Trainer(config)

    # Load the training data
    training_data = load_data("data/testData.json")

    # Create an interpreter by training the model
    interpreter = trainer.train(training_data)

    # PIckle serialization
    pickle.dump(interpreter, open('data/rasa_interpreter.sav', 'wb'))

# Returns most likely intent
def intent_parser(message):
    try:
        intent = interpreter.parse(message)['intent']['name']
    except:
        intent = None
    return intent

# Flask

app = Flask(__name__)

@app.route('/',methods=["GET", "POST"])
def chat_bot():
    return render_template("home.html")

@app.route('/process', methods=["GET", 'POST'])
def process():
    intent = None
    response = ''
    try:
        user_input = request.form['textinput']
        intent = intent_parser(user_input)
    except:
        user_input = "ERROR"
    #return response
    return response

if __name__ == '__main__':
    app.run(debug=True)