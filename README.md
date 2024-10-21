# Python-based-plagiarism-detection-system-


# Create virtual environment
python -m venv venv

# Install required Python packages
pip install flask flask-cors nltk scikit-learn gunicorn

# Create requirements.txt
pip freeze > requirements.txt

# Terminal 1 - Run Backend
cd backend

source venv/bin/activate
# Run Flask app
python app.py

# Terminal 2 - Run Frontend
cd frontend
npm start
