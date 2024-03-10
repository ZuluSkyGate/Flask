from flask import Flask


app = Flask(__name__)


@app.route("/") # Гланая страница сайта
def index():
    return "Hello, world!"

@app.route("/info") # Страница сайта info
def info():
    return "Меня создала команда GeekBrains!"



if __name__ == "__main__":
    app.run()