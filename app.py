from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot = ChatBot("budgy", storage_adapter="chatterbot.storage.SQLStorageAdapter")

english_bot.set_trainer(ChatterBotCorpusTrainer)

english_bot.train('chatterbot.corpus.english.greetings')
english_bot.train("./Final_2017.yml")
english_bot.train("./Final_2016.yml")
english_bot.train("./Final_GST.yml")
english_bot.train("./trainerdata.yml")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
