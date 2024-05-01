from flask import Flask, render_template, request, redirect, url_for
import os
import glob
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    image_name = glob.glob('/home/nick/SecurDriveFlask/static/Image/*.jpg')
    if image_name: # there is an image in the file containing activity pictures
        img = os.path.join('static', 'Image')
        file_path = os.path.join(img, image_name[0])
        full_name = os.path.basename(file_path)
        # collecting the file to upload to the website
        file = os.path.join(img, full_name)
        # find time that the picture was taken/last modified
        secondsTime = os.path.getmtime(file_path)
        modificationTimeAcc = datetime.datetime.fromtimestamp(secondsTime)
        # formatting time to be more legible for user
        modificationTime = str(modificationTimeAcc).split('.')[0]
        return render_template('img_render.html', image=file, activity=True, dateOfPicture=modificationTime)
    else: # there was no activity in the car, upload placeholder image telling user car is secure
        img = os.path.join('static', 'Image', 'default')
        file = os.path.join(img, 'DefualtStatus.jpg')
        return render_template('img_render.html', image=file, activity=False, dateOfPicture="")

@app.route('/delete_photo', methods=['POST'])
def delete_photo():
    image_name = glob.glob('/home/nick/SecurDriveFlask/static/Image/*.jpg')
    if image_name:
       os.remove(image_name[0])
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
