import React, { useEffect, useState } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import CourseCard from './components/CourseCard';

const App = () => {
    const [courses, setCourses] = useState([]);

    useEffect(() => {
        fetch('/courses')
            .then(response => response.json())
            .then(data => setCourses(data));
    }, []);

    return (
        <div>
            <Header />
            <div className="course-list">
                {courses.map(course => (
                    <CourseCard key={course.id} course={course} />
                ))}
            </div>
            <Footer />
        </div>
    );
};

export default App;