import os
from flask import Flask, request, flash, redirect, send_file
from werkzeug.utils import secure_filename
from models.model0 import Classifier
from img_func import save_bbox

app = Flask(__name__)

# Set up the directory where the files are to stored
UPLOAD_FOLDER = './images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def file_is_allowed(filename):
    # We need give a proper condition for checking filename
    if True:
        return True

# Our trained model
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
        filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filename)
        results = model.predict(filename)
        save_bbox(filename, results)
        # os.remove(filename)
        return send_file(filename, as_attachment=True)


# check the post api : curl -v -X POST -H "Content-Type: multipart/form-data" -F "file=@<file location>" http://localhost:5000 -o <output file>
# replace <file location> with the image name

if __name__ == '__main__':
    app.run(debug=True)