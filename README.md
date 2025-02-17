# Product Title Classification
> 🚀 Intelligent e-commerce product categorization using machine learning

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)  
[![Flask](https://img.shields.io/badge/flask-latest-green.svg)](https://flask.palletsprojects.com/)  
[![scikit-learn](https://img.shields.io/badge/scikit--learn-latest-orange.svg)](https://scikit-learn.org/)

## Table of Contents
- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Models Implemented](#models-implemented)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## Overview

## Problem Statement
The aim of this project is to develop a machine learning model that accurately classifies product titles into their respective categories. This solution helps organize products efficiently and improves the user experience on e-commerce platforms.

## Key Features
- 🎯 Multi-level product categorization  
- 🔍 Advanced text preprocessing  
- 🤖 Multiple ML models (SVM, Random Forest, Decision Tree)  
- 🌐 User-friendly web interface  
- 📊 Real-time classification and performance visualization  

## Technology Stack
- **Backend:** Python 3.x, Flask  
- **Machine Learning:** scikit-learn, NLTK, pandas, numpy  
- **Data Visualization:** matplotlib, seaborn  
- **Development Tools:** Jupyter Notebook, Git, Virtual Environment (venv)  

## Models Implemented
- **Support Vector Machine (SVM)**  
- **Random Forest Classifier**  
- **Decision Tree Classifier**  

## Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/muhammadhamzagova666/product-title-classification.git
   cd product-title-classification
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   # or for Windows:
   .\venv\Scripts\activate
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK data:**
   ```bash
   python -m nltk.downloader stopwords
   ```

## Usage Guide
1. **Start the Flask application:**
   ```bash
   python Source\ Code/app.py
   ```
   *Note: Depending on your setup, the path to `app.py` may differ.*

2. **Access the web interface:**
   - Open your web browser.
   - Navigate to `http://127.0.0.1:5000/`.

3. **Upload and classify product titles:**
   - Use the provided interface to upload product titles and descriptions for classification.

## Project Structure
```
Product Title Classification/
├── Source Code/
│   ├── app.py                  # Main Flask application
│   ├── Utilities.py            # Helper functions
│   ├── KNNImpute.py            # KNN imputation implementation
│   ├── templates/              # HTML templates
│   ├── static/                 # Static assets (CSS, images)
│   └── Svm_Models/             # Trained model files
├── data/                      # Training and validation datasets (CSV files)
├── notebooks/                 # Jupyter notebooks and model training scripts
└── other_files/               # Additional resources (e.g., labels.csv)
```
*Note: Directory names may vary slightly between versions.*  

## Configuration
Create a `.env` file in the root directory with the following content:
```env
FLASK_APP=app.py
FLASK_ENV=development
DEBUG=True
```

## Documentation
For more detailed information about the project and its underlying models, please refer to the documentation available in the Project Documentation directory.  

## Contributing
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a Pull Request.

**Contributors:**
- Muhammad Hamza Gova
- Muhammad Salar
- Talha Bilal  

## Roadmap
- [ ] Add support for more languages  
- [ ] Implement deep learning models  
- [ ] Enhance API documentation  
- [ ] Add batch processing capability  

## Contact
For any queries or further information, please contact:  
- **Muhammad Hamza Gova** - [@muhammadhamzagova666](https://github.com/muhammadhamzagova666)  

Project Link: [https://github.com/muhammadhamzagova666/product-title-classification](https://github.com/muhammadhamzagova666/product-title-classification)  

## Acknowledgments
- Many thanks to all the contributors for their support.
- Special thanks to the scikit-learn team for their excellent machine learning library.
- Appreciation goes to the Flask team for providing a robust web framework.  
