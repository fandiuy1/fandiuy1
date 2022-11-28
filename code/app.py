import os
from test import application
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
	return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@application.route('/i')
def index():
    return render_template('sign-up.html')
 
@application.route('/i',  methods=('POST', 'GET'))
def uploadFile():
	if 'file' not in request.files:
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))
		#print('upload_image filename: ' + filename)
		return render_template('upload.html', filename=filename)
	else:
		return redirect(request.url)

@application.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__":
    application.run()