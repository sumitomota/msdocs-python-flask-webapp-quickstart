from datetime import datetime
import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
# from azure.storage.blob import BlockBlobService, PublicAccess, ContentSettings
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
app = Flask(__name__)

connect_str = 'DefaultEndpointsProtocol=https;AccountName=storegeaccount1;AccountKey=Zz4fWjzS3VfsGL3GwKc+3LRuPFGEYElzdfZ7npFPbEa/xGudg+p0h1O4EzsqwgPs7khO7QhSxrZ3+AStmys8ZQ==;EndpointSuffix=core.windows.net'

container_name = 'container1'
ALLOWED_EXTENSION = 'csv'

def allowed_file(filename):
    return '.' in filename and \
          filename.rsplit('.', 1)[1].lower() == ALLOWED_EXTENSION
  
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
    
    if sendForm:
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
        # Create the BlobServiceClient object
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        uploadfilename = file.filename.replace('.csv', '_' + datetime.now().isoformat('_') + '.csv',)

        blob_client = blob_service_client.get_blob_client(container='container1', blob=uploadfilename)
        blob_client.upload_blob(file, blob_type="BlockBlob")

#        block_blob_service = BlockBlobService(account_name=account_name, account_key=account_key)
#       block_blob_service.create_blob_from_stream(
 #           container_name,
 #           file.filename,
 #           file,
 #       )
        return render_template('finishRequest.html', filename=file.filename)

@app.route('/signinform', methods=['GET', 'POST'])
def signinForm():
    print('Request for login page received')
    return render_template('signin.html')

@app.route('/request', methods=['GET'])
def request():
    print('Request for request page received')
    return render_template('request.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    print('Request for dashboard page received')
    return render_template('dashboard.html')

if __name__ == '__main__':
   app.run()
