# 🚀 Quick Setup Guide

## Prerequisites

- **Python 3.8 or higher**
- **Git** (for cloning the repository)
- **pip** (Python package installer)

## Step-by-Step Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Harshkkk6/-AI-Powered-Task-Management-System.git
cd AI-Powered-Task-Management-System
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download NLTK Data (Required for NLP)
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

### 5. Run the Application
```bash
streamlit run streamlit_app.py
```

### 6. Access the App
Open your web browser and go to: **http://localhost:8501**

## 🎯 What You'll Get

### ✅ **Pre-trained Models Included:**
- `task_classifier.pkl` - AI model for task classification
- `priority_predictor.pkl` - AI model for priority prediction
- `tfidf_vectorizer.pkl` - Text vectorizer for task classification
- `priority_tfidf_vectorizer.pkl` - Text vectorizer for priority prediction

### ✅ **Sample Data Included:**
- `jira_dataset.csv` - Original Jira dataset
- `cleaned_jira_dataset.csv` - Processed and cleaned dataset
- `new_tasks.csv` - User-added tasks (starts empty)

### ✅ **Complete Application:**
- Interactive Streamlit web interface
- AI-powered task classification and priority prediction
- Smart assignment recommendations
- Team workload analysis
- Deadline alerts and monitoring
- Recent tasks management with delete functionality

## 🔧 Troubleshooting

### Common Issues & Solutions:

#### 1. **Port Already in Use**
```bash
# Use a different port
streamlit run streamlit_app.py --server.port 8502
```

#### 2. **Model Loading Warnings**
- The warnings about scikit-learn version differences are normal and won't affect functionality
- Models were trained with scikit-learn 1.7.0 but work fine with 1.5.1+

#### 3. **BERT Model Loading Issues**
- First run may take longer as BERT models download
- Ensure stable internet connection for initial setup
- Models are cached locally after first download

#### 4. **Memory Issues**
- Close other applications if you encounter memory errors
- The app uses about 2-3GB RAM when fully loaded

#### 5. **Permission Errors (Windows)**
```bash
# Run PowerShell as Administrator if needed
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 📱 Features Overview

### **🏠 Home Page**
- Quick overview of system capabilities
- Navigation to all features

### **➕ New Task**
- Submit task descriptions
- Automatic AI classification and priority prediction
- Smart assignee recommendations
- Similar task suggestions

### **📊 Team Projects**
- Project overview with progress tracking
- Team member workload analysis
- Performance analytics and charts

### **📋 Recent Tasks**
- View tasks added today and this week
- Delete individual tasks or bulk delete
- Task statistics and visualizations

### **🚨 Alerts**
- Deadline monitoring and alerts
- Performance tracking
- Team health analysis
- Project status monitoring
- Smart recommendations

### **📤 Data Export**
- Export task data to CSV
- Backup and restore functionality

## 🎨 Customization

### **Adding New Team Members**
Edit the `team_members` list in `streamlit_app.py`:
```python
team_members = [
    "John Doe",
    "Jane Smith", 
    "Your Name Here"
]
```

### **Modifying Project Types**
Update the `project_types` list in `streamlit_app.py`:
```python
project_types = [
    "Web Development",
    "Mobile App",
    "Data Science",
    "Your Project Type"
]
```

### **Changing UI Colors**
Modify the CSS in the `apply_custom_css()` function in `streamlit_app.py`

## 🔄 Retraining Models (Optional)

If you want to retrain models with your own data:

```bash
# Train task classification model
python train_model.py

# Train priority prediction model  
python train_priority_model.py

# Train TF-IDF vectorizers
python train_tfidf_vectorizer.py
python train_priority_tfidf_vectorizer.py
```

## 📞 Support

### **Getting Help:**
1. Check this setup guide first
2. Review the main README.md for detailed documentation
3. Open an issue on GitHub for bugs or feature requests

### **System Requirements:**
- **Minimum RAM:** 4GB
- **Recommended RAM:** 8GB+
- **Storage:** 2GB free space
- **Internet:** Required for initial BERT model download

## 🎉 Success Indicators

You'll know everything is working when:
- ✅ Streamlit app starts without errors
- ✅ Models load successfully (you'll see "Models loaded successfully!")
- ✅ You can access the web interface at localhost:8501
- ✅ You can submit a new task and get AI predictions
- ✅ All navigation tabs work properly

---

**🎯 Ready to manage tasks with AI!** 

Your AI-Powered Task Management System is now fully operational. Start by adding your first task and watch the AI work its magic! 🚀 