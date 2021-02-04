import os
from flask import Flask, request, flash, redirect
from werkzeug.utils import secure_filename
from models.model0 import Classifier

app = Flask(__name__)

UPLOAD_FOLDER = './images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def file_is_allowed(filename):
    # give a condition after if inplace of True
    if True:
        return True

model = Classifier()

@app.route('/', methods=['POST'])
def upload_file():
    
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and file_is_allowed(file.filename):
        filename = secure_filename(file.filename)
        print(filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return model.predict(filename)


# check the post api : curl -v -X POST -H "Content-Type: multipart/form-data" -F "file=@<file location>" http://localhost:5000
# replace <file location> with the image name

if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)