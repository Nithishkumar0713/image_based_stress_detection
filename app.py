import random
import os

# FORCE LEGACY KERAS FOR TF 2.16+ compatibility
os.environ["TF_USE_LEGACY_KERAS"] = "1"

import pygame
from flask import Flask,request,render_template,send_from_directory,flash, redirect, url_for,session
from tensorflow.keras.models import load_model 
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import cv2
from tensorflow.keras.preprocessing.image import img_to_array
import sqlite3

db = sqlite3.connect('database.db', check_same_thread=False)
cursor = db.cursor()

app=Flask(__name__)
app.config['SECRET_KEY']='kbnfjbfgbfnghjfjk'

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/babout")
def babout():
    return render_template("babout.html")

@app.route("/logout")
def logout():
    return redirect(url_for('index'))

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        print(password)
        Gender = request.form['gen']
        print(Gender)
        contact = request.form['contact']
        address = request.form['address']
        dob = request.form['dob']
        Happy = request.form['Happy']
        Fear = request.form['Fear']
        Disgust = request.form['Disgust']
        Sad = request.form['Sad']
        Angry = request.form['Angry']
        Neutral = request.form.get('Neutral')
        Surprise = request.form['Surprise']
        print(Neutral)
        print(Fear)
        sql = "select * from users where email='%s' "%(email)
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)

        if data == []:
            sql="insert into users (name,password,email,Gender,mobile,address,dob,Happy,Fear,Disgust,Sad,Angry,Neutral,Surprise)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)" 
            val= (name,password,email,Gender,contact,address,dob,Happy,Fear,Disgust,Sad,Angry,Neutral,Surprise)
            cursor.execute(sql, val)
            db.commit()
            flash("Registration Successfull")
            return render_template("login.html")
    return render_template("register.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()
        
        if user:
            session['email']=email
            return redirect(url_for('home'))
        else:
            flash("Invalid Credentials")
            return redirect(url_for('login'))
    
    return render_template("login.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/prediction")
def prediction():
    f1 = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    c = load_model('models/Model.h5')
    final_labels = ['Angry','Disgust','Fear', 'Happy', 'Neutral', 'Sad','Surprise']
    c1 = cv2.VideoCapture(0)
    flag = 0
    play = 0
    while True:
        r, f = c1.read()
        l = []
        print(r)
        gray_data = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
        face_values = f1.detectMultiScale(gray_data, 1.3, 5)
        flag += 1
        if flag == 260:
            flag = 0
            play = 0
        for (x, y, w, h) in face_values:
            cv2.rectangle(f, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # roi_gray = gray[y:y + h, x:x + w]
            # roi_gray=cv2.
            roi_gray1 = cv2.resize(gray_data, (48, 48), interpolation=cv2.INTER_AREA)
            if np.sum([roi_gray1]) != 0:
                roi = roi_gray1.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)

                preds = c.predict(roi)[0]
                print(preds)
                l1 = final_labels[preds.argmax()]
                label_pos = (x, y)
                cv2.putText(f, l1, label_pos, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
                if play == 0:
                    if l1 == 'Angry':
                        path = "AUDIO/angry/"
                        file = os.path.join(path, random.choice(os.listdir(path)))
                        pygame.mixer.init()
                        pygame.mixer.music.load(file)
                        pygame.mixer.music.play()
                        # playsound('AUDIO/Kabali-Telugu-Songs-Nippu-Ra-Vid (mp3cut.net) (1).mp3', block=False)
                        play = 1
                    elif l1 == 'Happy':
                        path = "AUDIO/happy/"
                        file = os.path.join(path, random.choice(os.listdir(path)))
                        pygame.mixer.init()
                        pygame.mixer.music.load(file)
                        pygame.mixer.music.play()
                        # playsound('AUDIO/videoplayback (mp3cut.net) (1).mp3', block=False)
                        play = 1
                    elif l1 == 'Neutral':
                        path = "AUDIO/neutral/"
                        file = os.path.join(path, random.choice(os.listdir(path)))
                        pygame.mixer.init()
                        pygame.mixer.music.load(file)
                        pygame.mixer.music.play()
                        # playsound('AUDIO/videoplayback-1 (mp3cut.net) (1).mp3', block=False)
                        play = 1
                    elif l1 == 'Disgust':
                        path = "AUDIO/disgust/"
                        file = os.path.join(path, random.choice(os.listdir(path)))
                        pygame.mixer.init()
                        pygame.mixer.music.load(file)
                        pygame.mixer.music.play()
                        # playsound('AUDIO/videoplayback-1 (mp3cut.net) (1).mp3', block=False)
                        play = 1
                    elif l1 == 'Fear':
                        path = "AUDIO/fear/"
                        file = os.path.join(path, random.choice(os.listdir(path)))
                        pygame.mixer.init()
                        pygame.mixer.music.load(file)
                        pygame.mixer.music.play()
                        # playsound('AUDIO/videoplayback-1 (mp3cut.net) (1).mp3', block=False)
                        play = 1
                    elif l1 == 'Surprise':
                        path = "AUDIO/surprise/"
                        file = os.path.join(path, random.choice(os.listdir(path)))
                        pygame.mixer.init()
                        pygame.mixer.music.load(file)
                        pygame.mixer.music.play()
                        # playsound('AUDIO/videoplayback-1 (mp3cut.net) (1).mp3', block=False)
                        play = 1
                    else:
                        path = "AUDIO/sad/"
                        file = os.path.join(path, random.choice(os.listdir(path)))
                        pygame.mixer.init()
                        pygame.mixer.music.load(file)
                        pygame.mixer.music.play()
                        # playsound('AUDIO/Nee-Selavadigi-Full-Video-Song-J (mp3cut.net) (1).mp3', block=False)
                        play = 1

            else:
                cv2.putText(f, 'No Face Found', (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

        cv2.imshow('Emotion Detector', f)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    c.release()
    cv2.destroyAllWindows()
    return render_template("index.html")
@app.route("/upload", methods=["POST","GET"])
def upload():
    print('a')
    if request.method=='POST':
        myfile=request.files['file']
        # alg=request.form['alg']
        fn=myfile.filename
        mypath=os.path.join('images/', fn)
        myfile.save(mypath)
        accepted_formated=['jpg','png','jpeg','jfif']
        if fn.split('.')[-1] not in accepted_formated:
            flash("Image formats only Accepted","Danger")
        # if alg=="1":
        new_model = load_model(r"alg/FinalModel.h5")
        test_image = image.load_img(mypath, target_size=(224, 224))
        # elif alg == "2":
        #     new_model = load_model(r"models/ResNet50.h5")
        #     test_image = image.load_img(mypath, target_size=(224, 224))
        # else:
        #     new_model = load_model(r"models/VGG16Model2.h5")
        #     test_image = image.load_img(mypath, target_size=(128, 128))
        # else:
        #     new_model = load_model(r"models/Model.h5")
        #     test_image = image.load_img(mypath,target_size=(48, 48))

        test_image = image.img_to_array(test_image)
        test_image = test_image/255
        test_image = np.expand_dims(test_image, axis=0)
        result = new_model.predict(test_image)
        print(result)
        print(np.argmax(result))
        classes=['Angry','Disgust','Fear',
            'Happy','Neutral','Sad',
            'Surprise']
        prediction=classes[np.argmax(result)]
        cursor.execute("SELECT * FROM users WHERE email = ?", (session['email'],))
        user = cursor.fetchone()
         # Get the column names
        column_names = [desc[0] for desc in cursor.description]

        # Create a dictionary of column names and their values
        user_data = dict(zip(column_names, user))
        print(user_data)
    return render_template("template.html",image_name=fn, text=prediction,users=user_data)
@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

if __name__=='__main__':
    app.run(debug=True)