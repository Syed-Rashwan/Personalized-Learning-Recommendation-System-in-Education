import React from 'react';

const CourseCard = ({ course }) => {
    return (
        <div className="course-card">
            <h3>{course.title}</h3>
            <p>{course.description}</p>
        </div>
    );
};

export default CourseCard;