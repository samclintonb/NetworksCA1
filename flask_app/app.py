from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # loads a form

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    return render_template('thanks.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
