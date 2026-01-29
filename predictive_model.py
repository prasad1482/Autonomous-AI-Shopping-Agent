from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

def train_churn_model(rfm):
    print("Step 3: Training Predictive AI...")
    rfm['Churned'] = (rfm['Recency'] > 90).astype(int)
    X = rfm[['Recency', 'Frequency', 'Monetary']]
    y = rfm['Churned']
    
    model = XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=5)
    model.fit(X, y)
    
    rfm['Churn_Probability'] = model.predict_proba(X)[:, 1]
    return rfm, model