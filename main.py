from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Welcome!</h1>'
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0", debug=True,port=port)