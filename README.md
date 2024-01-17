Task 1: Titanic Classification - Make a system which tells whether the person will be save from sinking. What factors were most likely lead to success-socio-economic status, age, gender and more.

1. **Import Necessary Libraries:**
   - Imports essential libraries such as pandas for data manipulation, train_test_split for splitting data, RandomForestClassifier for building the classification model, and accuracy_score, classification_report for evaluating the model.

2. **Load the Titanic Dataset:**
   - Reads the Titanic dataset from a CSV file using pandas. Assumes the dataset includes features like 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', and the target variable 'Survived'.

3. **Preprocess the Data:**
   - Selects relevant features ('Pclass', 'Sex', 'Age', 'SibSp', 'Parch') and the target variable ('Survived') from the dataset.

4. **Convert Categorical Variables to Numerical:**
   - Utilizes one-hot encoding to convert categorical variables, such as 'Sex', into numerical form. This is necessary for machine learning algorithms to process these variables.

5. **Handle Missing Values:**
   - Fills missing values in the 'Age' column with the mean age. This step is performed to address missing data and ensure the dataset is ready for model training.

6. **Split the Data into Training and Testing Sets:**
   - Divides the dataset into training and testing sets using the train_test_split function. This is crucial for assessing the model's performance on unseen data.

7. **Create and Train the Model:**
   - Initializes a RandomForestClassifier and trains it on the training data. RandomForestClassifier is a machine learning algorithm suitable for classification tasks.

8. **Make Predictions on the Test Set:**
   - Uses the trained model to make predictions on the test set, allowing for the evaluation of the model's generalization performance.

9. **Evaluate the Model:**
   - Computes the accuracy of the model by comparing its predictions against the actual target values in the test set. Additionally, a detailed classification report is printed to provide insights into the model's precision, recall, and F1-score.

The overall goal of this code is to demonstrate the process of building a RandomForestClassifier model for predicting survival on the Titanic based on features like passenger class, gender, age, and family relationships. The accuracy and classification report offer a comprehensive evaluation of the model's performance.
