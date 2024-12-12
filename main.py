from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Directory to save uploaded images
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # Render the `index.html` page
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    ######################
    # ✨ Your code here. #
    ######################

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # Serve uploaded files for access
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)