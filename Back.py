from flask import Flask, request,jsonify
from flask_cors import CORS
import os
import docx
import PyPDF2
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle


server=Flask(__name__)
CORS(server)

ext={'pdf','docx','txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ext 

def expdf(path):
     try:
          file=open(path,'rb')
          reader=PyPDF2.PdfReader(file)
          text=""
          for page in range(len(reader.pages)):
               text+=reader.pages[page].extract_text()
          return text
     except Exception as e:
          return str(e)
     
def exdoc(path):
     try:
          file=docx.Document(path)
          text=""
          for para in file.paragraphs:
               text+=para.text+"\n"
          return text
     except Exception as e:
          return str(e)
def extxt(path):
     try:
          file=open(path,'r')
          text=file.read()
          return text
     except Exception as e:
          return str(e)
def text_extract(path):
     file_ext=path.rsplit('.',1)[1].lower()

     if file_ext=='pdf':
          return expdf(path)
     elif file_ext=='docx':
          return exdoc(path)
     elif file_ext=='txt':
          return extxt(path)
     else:
          return "Unsupported file format"
     
def train_model():
    resumes = [
        "Experienced software engineer with expertise in Python and machine learning.",
        "Digital marketing specialist skilled in SEO and social media advertising.",
        "Data scientist proficient in data analysis and visualization.",
        "Web developer experienced in React and JavaScript.",
        "Mechanical engineer with a background in CAD and thermal systems."
    ]

    labels = ["Software", "Marketing", "Data Science", "Web Development", "Mechanical"]

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(resumes)

    model = MultinomialNB()
    model.fit(X, labels)

    with open("model.pkl", "wb") as model_file:
        pickle.dump((vectorizer, model), model_file)

    print("Model trained and saved!")

#initialise model
if not os.path.exists("model.pkl"):
    train_model()
     
@server.route('/upload', methods=['POST'])
def upload_file():
    if 'File' not in request.files:
        return jsonify({"message":"No file part"}),400
    
    file=request.files['File']

    if file.filename=="":
        return jsonify({"message":"No selected file"}),400
    
    if file and allowed_file(file.filename):
        file_path=os.path.join("uploads",file.filename)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        file.save(file_path)
        extracted_text=text_extract(file_path)
        with open("model.pkl", "rb") as model_file:
            vectorizer, model = pickle.load(model_file)

        text_vector = vectorizer.transform([extracted_text])
        prediction = model.predict(text_vector)[0]  
        return jsonify({"message": f"File {file.filename} uploaded successfully","extracted_text":extracted_text,"predicted_field": prediction}),200
 
    
    else:
        return jsonify({"message":"Invalid file type : only .pdf,.docx and .txt files accepted"}),400
    
    

if __name__=="__main__":
        server.run(debug=True)