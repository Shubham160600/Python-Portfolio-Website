from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>My Python Portfolio</h1>
    <p>Welcome to my portfolio!</p>
    '''

if __name__ == '__main__':
    app.run(debug=True)

