#3. Develop a Flask app that uses URL parameters to display dynamic content.


from flask import Flask

app = Flask(__name__)

# Route with a dynamic parameter
@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}! Welcome to the dynamic greetings page.'

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000)
