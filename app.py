from flask import Flask

app = Flask(__name__)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


if __name__ == "__main__":
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 - 3 = {subtract(5, 3)}")


@app.route('/')
def home():
    return "Hello from Jenkins jkj Python Pipeline!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001)
