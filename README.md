Image-Based Stress Detection System
=================================

Project Description
-------------------
The Image-Based Stress Detection System is a deep learning–based application developed to analyze facial images and determine the stress level of an individual. Stress is an important psychological factor that affects human performance, mental health, and decision-making. Traditional stress detection methods rely on questionnaires or physiological sensors, which are time-consuming and intrusive. This project provides a non-intrusive, automated solution using computer vision and machine learning techniques.

The system detects human facial expressions from images and classifies emotions such as happy, sad, angry, neutral, fear, and surprise. These emotions are further mapped to stress levels. The application is implemented as a web-based system, allowing users to upload an image and receive stress analysis results in real time.

This project demonstrates the practical application of Artificial Intelligence, Deep Learning, and Web Technologies in the domain of mental health analysis.

---

Objectives
----------
The main objectives of the project are:
1. To detect facial expressions from images using computer vision techniques.
2. To classify emotions using deep learning models.
3. To analyze and predict stress levels based on detected emotions.
4. To develop a user-friendly web interface for stress prediction.
5. To achieve high accuracy using transfer learning models.
6. To provide a scalable and reproducible stress detection system.

---

System Overview
---------------
The system follows a client-server architecture. Users interact with the system through a web interface. Uploaded images are processed on the server, where facial features are extracted and passed to trained deep learning models. The predicted emotion and corresponding stress level are then displayed to the user.

---

Technologies Used
-----------------

Programming Languages:
- Python
- HTML
- CSS
- JavaScript

Frameworks and Libraries:
- Flask (Web Framework)
- TensorFlow
- Keras
- OpenCV
- NumPy

Deep Learning Models:
- Convolutional Neural Networks (CNN)
- VGG16
- ResNet50
- MobileNet

Database:
- SQLite (used for user and application data storage)

---

System Architecture
-------------------
1. User uploads an image through the web interface.
2. The system detects the face using Haar Cascade classifiers.
3. The detected face is preprocessed (resizing, normalization).
4. The preprocessed image is passed to the deep learning model.
5. The model predicts the facial emotion.
6. The emotion is mapped to a stress level.
7. The result is displayed to the user.

---

Project Structure
-----------------
image_based_stress_detection/

- app.py                  : Main Flask application file
- training.py             : Script used for training deep learning models
- model.py                : Model loading and prediction logic
- vgg.py                  : VGG-based model architecture
- requirements.txt        : Required Python dependencies
- setup_db.py             : Database initialization script
- db.sql                  : Database schema

Folders:
- templates/              : HTML templates for frontend
- static/                 : CSS, JavaScript, and UI images
- haarcascades/           : Haar Cascade XML files for face detection
- models/                 : Model performance graphs and plots
- alg/                    : Algorithm diagrams and workflow images

---

Model Training
--------------
The deep learning models are trained on facial emotion datasets. Data augmentation techniques such as rotation, flipping, and scaling are applied to improve generalization. Transfer learning is used to leverage pre-trained models such as VGG16, ResNet50, and MobileNet, which significantly improves accuracy and reduces training time.

---

How to Run the Project
---------------------

Step 1: Clone the Repository
git clone https://github.com/Nithishkumar0713/image_based_stress_detection.git

Step 2: Navigate to the Project Folder
cd image_based_stress_detection

Step 3: Install Required Dependencies
pip install -r requirements.txt

Step 4: Run the Application
python app.py

Step 5: Open the Application in Browser
http://127.0.0.1:5000/

---

Security and Best Practices
---------------------------
- Input validation is implemented to handle user uploads safely.
- Large files such as datasets and trained models are excluded using .gitignore.
- Separation of frontend and backend logic is maintained.
- Version control is managed using Git and GitHub.

---

Limitations
-----------
- Stress prediction is based only on facial expressions.
- Accuracy may vary with lighting conditions and image quality.
- Real-time video stress detection is not implemented in this version.

---

Future Enhancements
-------------------
- Real-time stress detection using live webcam feed.
- Integration of physiological signals such as heart rate.
- Deployment on cloud platforms.
- Mobile application support.
- Improved accuracy using larger datasets.

---

Academic Relevance
------------------
This project is developed as a Final Year Engineering Project. It demonstrates the application of Artificial Intelligence, Machine Learning, Computer Vision, and Web Development concepts in solving real-world problems related to mental health and human behavior analysis.

---

Author
------
Name: Nithish Kumar Pamidi  
Degree: Bachelor of Engineering and Technology   
Specialization: Computer Science Engineering in Cybersecurity 

---

Declaration
-----------
This project is intended strictly for academic and educational purposes. The datasets and trained models are excluded from this repository due to GitHub file size limitations.
