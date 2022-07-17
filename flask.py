from flask import *
import os

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))

@app.route('/')
def home():
    return 'Bot is Alive!'

if __name__ == '__main__':
    app.run(debug=True, port=port)
