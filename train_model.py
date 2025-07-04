import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from xgboost import XGBClassifier
import joblib
from sentence_transformers import SentenceTransformer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score

# Load BERT model
print('Loading BERT model...')
bert_model = SentenceTransformer('all-MiniLM-L6-v2')

def get_bert_embeddings(texts):
    return bert_model.encode(texts, show_progress_bar=True)

def train_and_save_model():
    print('Loading dataset...')
    df = pd.read_csv('cleaned_jira_dataset.csv')
    df['clean_summary'] = df['clean_summary'].fillna('')
    features = ['clean_summary', 'priority', 'project_type', 'text_length']
    X = df[features]
    y = df['issue_type']

    # Sample 50% of the data
    sample_size = int(len(df) * 0.5)
    df_sample = df.sample(n=sample_size, random_state=42)
    X_sample = df_sample[features]
    y_sample = df_sample['issue_type']

    # Encode target labels
    print('Encoding target labels...')
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y_sample)

    # BERT embeddings for summaries
    print('Generating BERT embeddings for summaries...')
    bert_features = get_bert_embeddings(X_sample['clean_summary'].tolist())

    # One-hot encode categorical features
    print('One-hot encoding categorical features...')
    ohe = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    cat_features = ohe.fit_transform(X_sample[['priority', 'project_type']])

    # Scale numerical feature
    print('Scaling numerical features...')
    scaler = StandardScaler()
    num_features = scaler.fit_transform(X_sample[['text_length']])

    # Combine all features
    print('Combining features...')
    X_all = np.hstack([bert_features, cat_features, num_features])

    # Split for evaluation
    print('Splitting data for evaluation...')
    X_train, X_test, y_train, y_test = train_test_split(X_all, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded)

    # Define simplified hyperparameter grid for XGBoost
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [3, 5],
        'learning_rate': [0.1, 0.2],
        'subsample': [0.8, 1.0],
        'colsample_bytree': [0.8, 1.0],
        'min_child_weight': [1, 3]
    }

    # Initialize XGBoost classifier
    print('Initializing XGBoost classifier...')
    xgb = XGBClassifier(eval_metric='mlogloss', random_state=42)

    # Perform grid search with cross-validation
    print('Performing hyperparameter tuning with cross-validation...')
    grid_search = GridSearchCV(estimator=xgb, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=1)
    grid_search.fit(X_train, y_train)

    # Get best model
    best_model = grid_search.best_estimator_
    print(f'Best parameters: {grid_search.best_params_}')

    # Evaluate
    train_acc = accuracy_score(y_train, best_model.predict(X_train))
    test_acc = accuracy_score(y_test, best_model.predict(X_test))
    print(f'Training accuracy: {train_acc:.3f}')
    print(f'Testing accuracy: {test_acc:.3f}')

    # Save everything needed for inference
    print('Saving model and encoders...')
    joblib.dump({
        'model': best_model,
        'label_encoder': label_encoder,
        'ohe': ohe,
        'scaler': scaler,
        'bert_model_name': 'all-MiniLM-L6-v2'
    }, 'task_classifier.pkl')
    print('Model and encoders saved as task_classifier.pkl')

if __name__ == "__main__":
    train_and_save_model() 