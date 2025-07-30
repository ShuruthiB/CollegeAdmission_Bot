*# 🎓 College Admission Helpdesk Chatbot 🤖*



*A simple machine learning-based chatbot that helps answer common queries about an engineering college — including courses, fees, placement information, campus life, and more.*



*Built with:*

*- 🧠 Scikit-learn (ML model using TF-IDF + Naive Bayes)*

*- 💬 Flask (backend)*

*- 🎨 HTML/CSS (frontend UI)*

*- 🗃️ intents.json for dynamic response training*



*---*



*## 📌 Features*



*- Answers frequently asked questions about:*

  *- Courses offered*

  *- Eligibility criteria*

  *- Admission process*

  *- Hostel and facilities*

  *- Campus placements*

  *- Companies visiting for recruitment*

*- Colorful GUI for better user experience*

*- Lightweight and easy to modify*

*- Works offline (no internet needed after setup)*



*---*



*## 🛠️ Installation*



*### 🔸 Clone the repository:*



*```bash*

*git clone https://github.com/ShuruthiB/CollegeAdmission_Bot*

*cd CollegeAdmissionBot*



*🔸 Install dependencies:*

*pip install -r requirements.txt*





*🚀 How to Run the Project*

*python app.py*

*Then open your browser and go to:*

*http://127.0.0.1:5000*



*🧠 How It Works*

*The intents.json file contains predefined tags and responses.*



*Text is vectorized using TF-IDF.*



*A Naive Bayes classifier is trained to map queries to intents.*



*Flask handles routing and response rendering.*



*The frontend interacts via a basic HTML/CSS page.*



*📦 File Structure*

*chatbot\_project/*

*│*

*├── app.py               # Flask app*

*├── train\_chatbot.py     # ML model trainer*

*├── intents.json         # Training data*

*├── chatbot\_model.pkl    # Saved model*

*├── templates/*

*│   └── index.html       # Frontend UI*

*├── static/*

*│   └── style.css        # Custom styling*

*└── README.md            # Project details*







*📄 License*

*This project is for educational purposes only.*





