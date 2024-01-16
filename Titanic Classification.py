
# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load Titanic dataset
titanic_data = pd.read_csv('titanic_dataset.csv')

# Preprocess data
features = titanic_data[['TicketClass', 'Gender', 'Age', 'SiblingsSpousesAbroad', 'ParentsChildrenAbroad']]
survival_status = titanic_data['Survived']

# Convert categorical variables to numerical using one-hot encoding
features = pd.get_dummies(features, columns=['Gender'], drop_first=True)

# Split data into training and testing sets
features_train, features_test, survival_train, survival_test = train_test_split(features, survival_status, test_size=0.2, random_state=42)

# Create and train the model
titanic_model = RandomForestClassifier(random_state=42)
titanic_model.fit(features_train, survival_train)

# Make predictions on test set
predictions = titanic_model.predict(features_test)

# Evaluate model
accuracy = accuracy_score(survival_test, predictions)
print(f"Accuracy: {accuracy:.2f}")

# Classification report for more detailed performance metrics
print(classification_report(survival_test, predictions))
