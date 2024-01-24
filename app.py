import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
# from azure.storage.blob import ContentSettings

app = Flask(__name__)

account_name = 'cs1100320010dc66396'
account_key = 'o46GVNrsMLsM/XcPN+SE2CW0wps/IUcKq6awhKJUzZ7hxFpU1scPye0hTFbuV6U+IW3mZ2EmfHSi+AStbZDNfQ=='
container_name = 'container1'
# ALLOWED_EXTENSIONS = {'csv'}

# def allowed_file(filename):
#    return '.' in filename and \
#           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.route('/')
def index():
    print('Request for index page received')
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/uploadForm', methods=['POST'])
def uploadForm():
    name = request.form.get('name')
    sendForm = request.form.get('SendForm')
    language = request.form.get('Lang')
    numberOfTarget = request.form.get('NoOfTarget')
    
    if name:
        print('Request for hello page received with name=%s' % name)
        return render_template('uploadForm.html', sendForm = sendForm, language=language)
    else:
        print('Request for hello page received with no name or blank name -- redirecting')
        return redirect(url_for('index'))

@app.route('/upload', methods=['POST'])
def upload():
    # check if the post request has the file part
    if 'file' not in request.files:
        # flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        # flash('No selected file')
        return redirect(request.url)
    # if file and allowed_file(file.filename):
    if file:
#        block_blob_service = BlockBlobService(account_name=account_name, account_key=account_key)
#        block_blob_service.create_blob_from_stream(
#            container_name,
#            file.filename,
#            file,
#        )
        return redirect(url_for('finishRequest'))

if __name__ == '__main__':
   app.run()
