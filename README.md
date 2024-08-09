# Text Translation Application

This is a simple text translation application built using Flask and the Transformers library. The application allows users to input text and receive translations in required language using pre-trained models from the Transformers library.

## Getting Started

Follow these steps to set up and run the application locally.

### Prerequisites

Ensure you have Python 3.10 installed. 

### 1. Create a Virtual Environment

Create a virtual environment to manage project's dependencies. In your terminal, run:

```
python -m venv venv
```

### 2. Activate the Virtual Environment
```
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages listed in requirements.txt and any other(if needed) :
```
pip install -r requirements.txt
```

### 4. Run the Application
```
python app.py
```

### 5. Access the Application
Open your web browser and navigate to:

```
http://127.0.0.1:5000
```

### Project Structure
Here is a brief overview of the project structure:
```
.
├── app.py                 # Main application file
├── requirements.txt       # List of dependencies
├── venv/                  # Virtual environment directory (excluded from version control)
└── README.md              # This file
```

### Notes
  - If you encounter any issues with package versions, consider updating your requirements.txt file or installing specific versions of dependencies.
  - For further customization or development, refer to the documentation of Flask and Transformers.
