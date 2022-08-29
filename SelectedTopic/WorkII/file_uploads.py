import os
from flask import Flask,request, render_template

UPLOAD_FOLDER = 'WorkII/uploads' #จะเป็นโฟล์เดอร์ที่เก็บไฟล์ที่เรา upload
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def uploader():
    if request.method == 'POST':
        f= request.files['filename']
        f.save(os.path.join (app.config['UPLOAD_FOLDER'],f.filename))
        return render_template("home.html",msg="File has been uploaded successfully.")
    return render_template("home.html",msg="Please choose a file.")
if __name__=='__main__':
    app.run(debug=True)