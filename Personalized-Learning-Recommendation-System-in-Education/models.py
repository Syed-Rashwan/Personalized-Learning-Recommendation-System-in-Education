

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class CourseRecommender:
    def __init__(self):
        self.model = RandomForestClassifier()

    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        print('Accuracy:', accuracy_score(y_test, y_pred))

    def get_recommendations(self, student_id, course_id):
        # Get student and course data
        student_data = pd.read_csv('data/students.csv')
        course_data = pd.read_csv('data/courses.csv')

        # Get student and course features
        student_features = student_data.loc[student_data['id'] == student_id]
        course_features = course_data.loc[course_data['id'] == course_id]

        # Get recommendations
        recommendations = self.model.predict(student_features, course_features)
        return recommendations

class StudentRecommender:
    def __init__(self):
        self.model = RandomForestClassifier()

    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        print('Accuracy:', accuracy_score(y_test, y_pred))

    def get_recommendations(self, student_id):
        # Get student data
        student_data = pd.read_csv('data/students.csv')

        # Get student features
        student_features = student_data.loc[student_data['id'] == student_id]

        # Get recommendations
        recommendations = self.model.predict(student_features)
        return recommendations