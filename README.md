# Flask Web Application with Named Entity Recognition (NER)

This project is a Flask-based web application that integrates Named Entity Recognition (NER) functionality using the Hugging Face Transformers library. It features user registration, login, and NER processing for input text.

## Features

- **User Authentication:**
  - Registration with a unique email.
  - Login functionality to access the application.

- **Named Entity Recognition (NER):**
  - Uses a pre-trained BERT model (dbmdz/bert-large-cased-finetuned-conll03-english) for NER.
  - Extracts and categorizes entities such as PERSON, LOCATION, ORGANIZATION, and MISC.
  - GPU acceleration support for faster processing.

- **Interactive Web Pages:**
  - User-friendly HTML templates for login, registration, and NER functionality.

- **Backend Database:**
  - Stores user data in a JSON file (`users.json`).

## File Structure

project-folder/ ├── api.py # Implements the NER functionality using Hugging Face ├── app.py # Main Flask application with routes and session handling ├── db.py # Database operations (JSON-based storage) ├── users.json # JSON file for user data ├── settings.cfg # Configuration file (contains API key placeholder) ├── requirements.txt # Python dependencies ├── templates/ # HTML templates for the web pages │ ├── login.html # Login page │ ├── register.html # Registration page │ ├── profile.html # User profile page │ ├── ner.html # NER processing page │ ├── error.html # Error page for invalid routes │ ├── base.html # Base template for consistent layout └── static/ # Static files (CSS, JavaScript, images)


## HTML Files and Their Purpose

1. **login.html**  
   - Provides a form for users to log in to the application.  
   - Includes fields for email and password.

2. **register.html**  
   - Allows users to create an account.  
   - Includes fields for name, email, and password.

3. **profile.html**  
   - Displays user information after a successful login.  
   - Acts as a dashboard for accessing other features.

4. **ner.html**  
   - Contains a form for submitting text to extract named entities.  
   - Displays categorized entities in a table format after processing.

5. **error.html**  
   - Generic error page shown for invalid routes or server errors.  
   - Provides a link to navigate back to the home page.

6. **base.html**  
   - A common layout template that other HTML files extend.  
   - Ensures consistent headers, footers, and styles across pages.

## Prerequisites

1. **Python Environment:** Ensure you have Python 3.8+ installed.
2. **CUDA:** For GPU acceleration, ensure CUDA is properly configured.
3. **Virtual Environment (Optional):** Create and activate a virtual environment for the project.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```