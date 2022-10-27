from flask import Flask, flash, render_template, redirect, jsonify, url_for, request

app = Flask(__name__, static_folder='static', static_url_path='')
app.secret_key = "pks"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=6009)