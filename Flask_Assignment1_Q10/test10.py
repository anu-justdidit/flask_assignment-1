#10. Design a Flask app with proper error handling for 404 and 500 errors.



from flask import Flask, jsonify

app = Flask(__name__)

# Route that triggers a 404 error
@app.route('/not_found')
def not_found():
    # Simulate a resource not found scenario
    abort(404)

# Route that triggers a 500 error
@app.route('/server_error')
def server_error():
    # Simulate a server-side error
    1 / 0  # This will raise a ZeroDivisionError intentionally

# Custom error handler for 404 error
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'error': 'Not Found', 'message': 'The requested URL was not found on the server'}), 404

# Custom error handler for 500 error
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error', 'message': 'An internal server error occurred'}), 500

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000)
