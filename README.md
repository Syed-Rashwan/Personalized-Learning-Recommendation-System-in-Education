# Personalized-Learning-Recommendation-System-in-Education

## **Overview**  
The **AI-Powered Intelligent Tutoring System** is a cutting-edge educational platform designed to provide personalized, AI-driven learning experiences. It integrates advanced **Natural Language Processing (NLP)** models and recommendation systems to adapt to each student's unique learning needs.  

---

## **Features**  

- **Real-Time Q&A Chatbot**:  
  AI-powered chatbot to answer subject-specific questions instantly.  

- **Personalized Learning Paths**:  
  Dynamic curriculum suggestions tailored to individual progress.  

- **Resource Recommendations**:  
  Smart system to suggest videos, articles, and exercises using collaborative filtering.  

- **Performance Tracking**:  
  Visualize progress with graphs and metrics to monitor growth.  

---

## **Technology Stack**  

### **Frontend**  
- **React.js**: User-friendly interface for seamless navigation.  
- **Chart.js**: Interactive charts to display performance metrics.  
- **Bootstrap**: Clean and modern UI design.  

### **Backend**  
- **Python (Flask/Django)**: API and server-side logic.  
- **FastAPI** (optional): For high-performance API services.  

### **AI Models**  
- **GPT/BERT**: NLP models for Q&A functionality.  
- **Collaborative Filtering**: For resource recommendations.  
- **Matrix Factorization**: Enhances personalized suggestions.  

### **Database**  
- **PostgreSQL**: To store user data and learning progress.  

---

## **Setup and Installation**

### **Prerequisites**  
- **Node.js** (v16+)
- **Python** (v3.8+)
- **PostgreSQL** (or another RDBMS)
- **Git**  

## Project Architecture  

```
├── backend/
│   ├── app/
│   │   ├── models/         # AI and ML models
│   │   ├── routes/         # API routes for user and admin endpoints
│   │   └── utils/          # Utility functions and scripts
│   ├── config.py           # Application configuration
│   └── requirements.txt    # Backend dependencies
├── frontend/
│   ├── src/
│   │   ├── components/     # React components for UI
│   │   ├── pages/          # User-facing pages
│   │   └── utils/          # Helper functions
│   ├── package.json        # Frontend dependencies
│   └── public/             # Static assets (images, icons, etc.)
├── data/
│   ├── datasets/           # Example datasets for testing
│   └── trained_models/     # Pre-trained or fine-tuned AI models
└── README.md
```

---

## Setup and Installation

### Prerequisites
- **Node.js** (v16+)
- **Python** (v3.8+)
- **PostgreSQL** (or another RDBMS)
- **Git** and **GitHub CLI** (optional)

### Step 1: Clone the Repository  
```
git clone https://github.com/yourusername/ai-tutoring-system.git
cd ai-tutoring-system
```

### Step 2: Set Up the Frontend

Navigate to the frontend directory:

```
cd frontend
```

Install dependencies:
```
npm install
```

Start the frontend server:

```
npm start
```

### Step 3: Set Up the Backend
Navigate to the backend directory:
```
cd backend
```
Create a virtual environment:
```
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

Install dependencies:
```
pip install -r requirements.txt
```
Start the backend server:
```
python manage.py runserver
```


### Step 4: Configure the Database
Install PostgreSQL and create a database named ai_tutoring.
Update config.py in the backend to include your database credentials.


### Step 5: Run the Application
Access the app in  your browser at http://localhost:3000.

The backend API runs at http://localhost:8000.


## How It Works:
## User Workflow

#### Sign Up/Login:

Users register or log in using the frontend interface.

#### Ask Questions:
The AI chatbot responds to queries based on trained NLP models.

#### **Get Recommendations**:
Learning materials are suggested based on user progress and preferences.

#### **Track Performance**:
View a dashboard with detailed insights into learning metrics.

### Admin Features
Manage users and content.

Add or modify learning resources.

Monitor system performance.

Future Improvements

Gamification: Add quizzes, badges, and leaderboards.

Multilingual Support: Use translation APIs for non-English learners.

Video Analysis: Use AI to summarize videos and extract key points.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Fork the repository.

#### Create a new branch for your feature:
```
git checkout -b feature-name
Submit a pull request. 
```
## **Contributors**
- **Syed Rashwan** (Project Lead)






