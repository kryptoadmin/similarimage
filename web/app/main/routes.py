import os
from flask import Blueprint, request, redirect, url_for, flash, render_template, current_app
from werkzeug.utils import secure_filename
from skimage.metrics import structural_similarity
import imutils
import cv2
from PIL import Image

main = Blueprint('main', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@main.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the files part
        if 'file1' not in request.files or 'file2' not in request.files:
            flash('No file part')
            return redirect(request.url)
        original = request.files['file1']
        tampered = request.files['file2']
        # If user does not select file, browser also submits an empty part without filename
        if original.filename == '' or tampered.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if original and allowed_file(original.filename) and tampered and allowed_file(tampered.filename):
            # Resize and save uploaded images
            original = Image.open(original).resize((250,160))
            original.save(os.path.join(current_app.config['UPLOAD_DIR'], "original.png"))

            tampered = Image.open(tampered).resize((250, 160))
            tampered.save(os.path.join(current_app.config["UPLOAD_DIR"], "tampered.png"))
            
            # Read uploaded images as array
            original = cv2.imread(os.path.join(current_app.config["UPLOAD_DIR"], "original.png"))
            tampered = cv2.imread(os.path.join(current_app.config["UPLOAD_DIR"], "tampered.png"))

            # Convert the images into grayscale
            original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
            tampered_gray = cv2.cvtColor(tampered, cv2.COLOR_BGR2GRAY)

            # Calculate the structural similarity
            (score, diff) = structural_similarity(original_gray, tampered_gray, full=True)
            diff = (diff * 255).astype("uint8")

            # Calculate threshold and contours
            threshold = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
            contours = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(contours)

            # Draw contours on image
            for contour in contours:
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(original, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.rectangle(tampered, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # Remove the uploaded files
            os.remove(os.path.join(current_app.config["UPLOAD_DIR"], "original.png"))
            os.remove(os.path.join(current_app.config["UPLOAD_DIR"], "tampered.png"))
            
            flash("Above images are predicted to be {} percentage similar".format(str(round(score*100, 2))))
            return redirect(url_for('main.upload_file'))
    return render_template('upload.html')
