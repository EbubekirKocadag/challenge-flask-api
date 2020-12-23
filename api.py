from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
#@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/status')   #get
def status():
    return render_template('status.html')

@app.route('/login')    #post
def login():
    return render_template('login.html')

if __name__ == '__main__':
   app.run()