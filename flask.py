from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot is Alive!'

if __name__ == '__main__':
    app.run(debug=True)
