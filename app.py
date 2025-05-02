from flask import Flask

app = Flask(__name__)

@app.route(‘/greet’, methods=[‘POST’])
def greet():
  name = request.form[‘name’]
  return f’Hello, {name}!’
@app.route("/")
def hello():
    return render_template('index.html', message='Hello, World!')

if __name__ == "__main__":
    app.run(debug=True)
