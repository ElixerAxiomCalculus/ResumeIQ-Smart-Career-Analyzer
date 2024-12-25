# ResumeIQ : Smart Resume Analyzer

Welcome to the **Smart Resume Analyzer** repository! This project allows users to upload resumes in various formats (`PDF`, `DOCX`, and `TXT`) to identify the most compatible job field based on the content of the resume. It uses Natural Language Processing (NLP) and machine learning models to analyze the resume and predict the job category.

## Features

- **Upload a Resume**: Users can upload resumes in `.pdf`, `.docx`, and `.txt` formats.
- **Text Extraction**: Extracts readable text from uploaded resumes using format-specific libraries.
- **Job Field Prediction**: Classifies the resume into a predefined category using a machine learning model (Naive Bayes).
- **Responsive Frontend**: Clean and simple UI powered by HTML, CSS, and JavaScript with Bootstrap for styling.
- **Fast Processing**: Provides a quick response after the user uploads the resume.

## Project Structure

This project is divided into four main components:

1. **Backend (Flask App)**:
   - The backend is a Flask web server that accepts resume uploads, processes the resume and predicts the job field.
   - The machine learning model used for classification is a pre-trained Naive Bayes model.

2. **Frontend (HTML, CSS, JavaScript)**:
   - Simple and user-friendly interface allowing users to upload their resumes.
   - Displays extracted text and predicted job field once the file is processed.

3. **Model**:
   - The model is trained on sample resumes and uses the Naive Bayes classifier to predict the job field.

4. **Supporting Files**:
   - Includes libraries and scripts for handling text extraction from PDF, DOCX, and TXT files.

## Technologies Used

- **Backend**: Flask, Python
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Machine Learning**: Scikit-learn, Naive Bayes, CountVectorizer
- **Libraries**:
  - PyPDF2 for extracting text from PDF files
  - python-docx for extracting text from DOCX files
  - Custom JavaScript code for handling file upload and displaying results

## Installation Instructions

To run this project locally, follow the instructions below.

### Step 1: Clone the Repository
Clone the repository to your local machine using the following command:

`git clone https://github.com/yourusername/Smart-Resume-Analyzer.git`

### Step 2: Install Dependencies
Navigate to the project directory and install the required Python dependencies using pip:

`cd Smart-Resume-Analyzer
pip install -r requirements.txt`

The requirements.txt file includes the following dependencies:

- Flask
- Flask-CORS
- scikit-learn
- PyPDF2
- python-docx
   
You may need to install these manually if you encounter issues.

### Step 3: Running the Flask Application
To start the backend, navigate to the project directory and run the following command:

`python app.py`

This will start a local server (typically on http://127.0.0.1:5000) where the backend will be running.

### Step 4: Access the Frontend
Open the index.html file in your browser or serve it through a simple local server to interact with the project.

Alternatively, you can use the following command to start a simple HTTP server:

`python -m http.server`

Then, access the frontend via http://localhost:8000/index.html.

### Step 5: Test the Application
Upload a resume in PDF, DOCX, or TXT format.
After uploading, the system will process the resume and display:
- Extracted Text
- Predicted Job Field

### How It Works :
### Text Extraction:

The backend extracts the text from the uploaded resume using specific Python libraries.
- For PDFs, it uses PyPDF2.
- For DOCX files, it uses python-docx.
- For TXT files, it uses Python’s built-in file handling.
- Text Vectorization:

Once the text is extracted, the words are vectorized using CountVectorizer from scikit-learn.
This converts the resume text into a numerical format that can be used by the machine learning model.
- Model Prediction:

The pre-trained Naive Bayes model (MultinomialNB) is used to classify the resume into predefined job categories such as Software, Marketing, Data Science, Web Development, etc.
The model predicts the job field based on the text content of the resume.

### Example of Usage
- Uploading a Resume:
- Choose a resume from your local computer (PDF, DOCX, or TXT format).
- After selecting the file, the application will automatically upload and process the resume.

Result Display:
After processing, the application will display the extracted text and predicted job field.

### Contributions
We welcome contributions to this project! If you have any improvements or ideas, feel free to fork the repository, create a new branch, and submit a pull request.

### To contribute:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them.
- Push to your fork and submit a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgements
- Flask for the backend web framework.
- Scikit-learn for machine learning and text vectorization.
- PyPDF2 for handling PDF file extraction.
- python-docx for extracting content from DOCX files.
- Bootstrap for responsive frontend design.

### Contact
For any questions or suggestions, please feel free to open an issue in this repository or reach out to the project creator:

GitHub: https://github.com/ElixerAxiomCalculus

Email: sayakmondal10@gmail.com

Thank you for checking out this project!
