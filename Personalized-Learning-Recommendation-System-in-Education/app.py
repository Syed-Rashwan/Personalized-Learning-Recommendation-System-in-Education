from flask import Flask, jsonify, request
from models import CourseRecommender, StudentRecommender
from data import load_courses, load_students

app = Flask(__name__)

# Load data
courses = load_courses()
students = load_students()

# Initialize machine learning models
course_recommender = CourseRecommender()
student_recommender = StudentRecommender()

# Define API routes
@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify(courses)

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    student_id = request.json['student_id']
    course_id = request.json['course_id']
    recommendations = course_recommender.get_recommendations(student_id, course_id)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)