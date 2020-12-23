from flask import Flask, render_template
from form import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']="kbfvizrguzourgu"

@app.route('/')
#@app.route('/home')
def index():
    return render_template('index.html', message="Hello")

@app.route('/status')   #get
def status():
    return render_template('status.html')

@app.route('/login')    #post
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

if __name__ == '__main__':
   app.run()