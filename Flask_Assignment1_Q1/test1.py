#1. Create a Flask app that displays "Hello, World!" on the homepage.




from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the app
    app.run(debug=True)