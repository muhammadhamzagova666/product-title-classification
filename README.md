# Product Title Classification
> 🚀 Intelligent e-commerce product categorization using machine learning

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-latest-green.svg)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-latest-orange.svg)](https://scikit-learn.org/)

## Overview
Product Title Classification is a sophisticated web application that leverages machine learning to automatically categorize product titles into predefined categories. Built for e-commerce platforms, it streamlines product management and enhances user experience through intelligent classification.

### Key Features
- 🎯 Multi-level product categorization
- 🔍 Advanced text preprocessing
- 🤖 Multiple ML models (SVM, Random Forest, Decision Tree)
- 🌐 User-friendly web interface
- 📊 Real-time classification
- 📈 Performance visualization

### Target Audience
- E-commerce platforms
- Product managers
- Data scientists
- Web developers

## Technology Stack
- **Backend**: Python 3.x, Flask
- **Machine Learning**: scikit-learn, NLTK, pandas, numpy
- **Data Visualization**: matplotlib, seaborn
- **Development Tools**: Jupyter Notebook, Git
- **Frontend**: HTML, CSS, Bootstrap

## Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/muhammadhamzagova666/product-title-classification.git
cd product-title-classification
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Download NLTK data:
```bash
python -m nltk.downloader stopwords
```

## Usage Guide

1. Start the Flask application:
```bash
python Source\ Code/app.py
```

2. Access the web interface:
   - Open your browser
   - Navigate to `http://127.0.0.1:5000/`
   - Use the upload interface to classify product titles

## Project Structure
```
Source Code/
├── app.py                  # Main Flask application
├── Utilities.py            # Helper functions
├── KNNImpute.py            # KNN imputation implementation
├── templates/              # HTML templates
├── static/                 # Static assets (CSS, images)
├── Svm_Models/             # Trained model files
└── data/                   # Training and validation datasets
```

## Configuration
Create a `.env` file in the root directory:
```env
FLASK_APP=app.py
FLASK_ENV=development
DEBUG=True
```

## Documentation
Detailed documentation is available in the Project Documentation directory.

## Contributing
Contributions are welcome! Please read our Contributing Guidelines first.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Roadmap
- [ ] Add support for more languages
- [ ] Implement deep learning models
- [ ] Enhance API documentation
- [ ] Add batch processing capability

## Contact
Muhammad Hamza Gova - [@muhammadhamzagova666](https://github.com/muhammadhamzagova666)

Project Link: [https://github.com/muhammadhamzagova666/product-title-classification](https://github.com/muhammadhamzagova666/product-title-classification)

## Acknowledgments
- Contributors
- scikit-learn team for their excellent machine learning library
- Flask team for the web framework
