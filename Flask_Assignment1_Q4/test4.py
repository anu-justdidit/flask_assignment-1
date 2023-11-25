#4. Create a Flask app with a form that accepts user input and displays it.


from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the form page
@app.route('/')
def index():
    return render_template('form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        user_input = request.form['user_input']
        return render_template('display.html', user_input=user_input)

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000)
