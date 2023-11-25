#5. Implement user sessions in a Flask app to store and display user-specific data.



from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

# Set a secret key for session management
app.secret_key = 'super_secret_key'

# Route for the form page
@app.route('/')
def index():
    return render_template('form_session.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        user_input = request.form['user_input']
        session['user_input'] = user_input  # Store user input in session
        return redirect(url_for('display'))

# Route to display user input from the session
@app.route('/display')
def display():
    user_input = session.get('user_input')  # Retrieve user input from session
    return render_template('display_session.html', user_input=user_input)

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000)
