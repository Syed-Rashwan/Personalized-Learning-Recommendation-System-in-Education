from flask import Flask, jsonify, request
from models import CourseRecommender, StudentRecommender
from data import load_courses, load_students

app = Flask(__name__)

# Load data
courses = load_courses()
students = load_students()

# Initialize machine learning models
course_recommender = CourseRecommender(courses, students)
student_recommender = StudentRecommender(courses, students)

# Define API routes
@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify(courses)

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    data = request.get_json()
    student_id = data.get('student_id')
    course_id = data.get('course_id')

    if student_id is None or course_id is None:
        return jsonify({"error": "Missing student_id or course_id"}), 400

    recommendations = course_recommender.get_recommendations(student_id, course_id)
    return jsonify({"recommended_courses": recommendations})

if __name__ == '__main__':
    app.run(debug=True)
