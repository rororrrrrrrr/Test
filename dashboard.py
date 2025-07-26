from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    metrics = {
        'users': 150,
        'active_sessions': 45,
        'revenue': 1234.56
    }
    return render_template('dashboard.html', metrics=metrics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
