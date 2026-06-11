AI Code Ethics Checker
Description

The AI Code Ethics Checker is a web application built in Python using Streamlit and the Gemini model. It enables the ethical analysis of source code or descriptions of AI systems.

After entering the code or system description, the user receives a report containing:

identification of potential risks,
explanation of detected issues,
recommendations for mitigating them,
risk level assessment (Low / Medium / High).

The analysis takes the following aspects into account:

Bias
Privacy
Fairness
Transparency
Security
Requirements
Python 3.10 or later
pip
Installation
1. Clone or download the project
git clone <repository_url>
cd AI-Code-Ethics-Checker
2. Create a virtual environment (optional)
python -m venv .venv
3. Activate the environment

Windows:

.venv\Scripts\activate
4. Install the required libraries
pip install -r requirements.txt
5. Create a .env file

In the project’s root directory, create a .env file:

API_KEY=your_gemini_api_key
6. Run the application
streamlit run main.py
7. Open the application in your browser
http://localhost:8501
Technologies used
Python
Streamlit
Google Gemini API
python-dotenv
Author

Project created for educational and research purposes.