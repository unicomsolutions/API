import os
from flask import Flask, url_for, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from sentry import convert
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

variable = 'a'
app = Flask(__name__)
UPLOAD_FOLDER = '/home/rahul/API/projects/project1/files'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@139.59.5.153/postgres'
db = SQLAlchemy(app)


app.debug = True

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80), unique=True)

    def __init__(self,username):
        self.username = username

    def __repr__(self):
        return '<user %s>'%self.username

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/about')
def about():
    ab = "Team Unicom Solutions is one of the 9 teams in the world to be selected to pitch for the final of enable makeathon 2.0"
    return ab

@app.route('/convert/<string:text>')
def con(text):
    # show the post with the given id, the id is an integer
    ans = convert(text)
    ret = ans + "<br>" + "to correct any other sentence type after convert in the url"
    return ret

@app.route('/')
def index():

    return render_template('home.html')
@app.route('/answer')
def answer():

    return variable

@app.route('/post', methods = ['POST'])
def post():
    user = User(request.form['username'])
    db.session.add(user)
    db.session.commit()
    return render_template('add_user.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:

            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':

            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print "here:", os.path.join(app.config['UPLOAD_FOLDER'])
            global variable
            variable = 'I'
            return variable

    return render_template('upload.html')





if __name__== "__main__":
    app.run()

