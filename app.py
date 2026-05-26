from flask import Flask jsonify, render_template_string, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("<h1>Welcome to the CI/CD Pipeline App!</h1>")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 7000))
    app.run(host='0.0.0.0', port=port)
