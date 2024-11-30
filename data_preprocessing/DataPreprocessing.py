import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

class DataPreprocessor:

    """
    Example usage:
    
    # Load data
    df = pd.read_csv('data.csv')

    # Define features and target
    X = df.drop('target', axis=1)
    y = df['target']

    # Define numerical and categorical features
    numerical_features = ['age', 'salary']
    categorical_features = ['gender', 'city']

    # Preprocess data
    preprocessor = DataPreprocessor()
    X_processed = preprocessor.fit_transform(X, numerical_features, categorical_features)

    # Split data
    X_train, X_test, y_train, y_test = preprocessor.split_data(X_processed, y)

    """


    # Constructor
    def __init__(self):
        """The Preproceessor class is used to preprocess data before training a model."""
        self.numerical_features = None
        self.categorical_features = None
        self.preprocessor = None

    # Fit the preprocessor
    def fit(self, X, numerical_features, categorical_features):
        """Fit the preprocessor on the data."""
        self.numerical_features = numerical_features
        self.categorical_features = categorical_features

        # Numerical pipeline
        numerical_pipeline = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='mean')),
            ('scaler', StandardScaler())
        ])

        # Categorical pipeline
        categorical_pipeline = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ])

        # Combine pipelines
        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', numerical_pipeline, self.numerical_features),
                ('cat', categorical_pipeline, self.categorical_features)
            ]
        )

        self.preprocessor.fit(X)

    # Transform the data
    def transform(self, X):
        """Transform the data using the preprocessor."""
        return self.preprocessor.transform(X)

    # Fit and transform the data
    def fit_transform(self, X, numerical_features, categorical_features):
        """Fit and transform the data using the preprocessor"""
        self.fit(X, numerical_features, categorical_features)
        return self.transform(X)

    # Split the data
    def split_data(self, X, y, test_size=0.2, random_state=42):
        """Split the data into training and testing sets."""
        return train_test_split(X, y, test_size=test_size, random_state=random_state)