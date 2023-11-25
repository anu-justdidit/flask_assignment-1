
#6. Build a Flask app that allows users to upload files and display them on the website.from flask import Flask, render_template, request, redirect, url_for


import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('upload.html', files=files)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
            return redirect(url_for('index'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000)
