
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return "This is main page"

@app.route('/login')
def login():
    return render_template('/authentication/login.html', pageName= 'Login')

@app.route('/signup')
def signup():
    return render_template('/authentication/signup.html', pageName= 'Sign Up')
    
@app.route('/student/profile')
def studentProfile():
    return render_template('/student/profile.html', pageName= 'Student Profile')

@app.route('/student/course')
def studentCourse():
    return render_template('/student/course.html', pageName= 'Student Course')

@app.route('/student/course/statistic')
def studentCourseStatistic():
    return render_template('/student/statistic.html', pageName= 'Course Statistic')
    
@app.route('/student/course/feedback')
def studentCourseFeedback():
    return render_template('/student/feedback.html', pageName= 'Course Feedback')

@app.route('/student/course/score')
def studentCourseScore():
    return render_template('/student/score.html', pageName= 'Course Score')

@app.route('/teacher/profile')
def teacherProfile():
    return render_template('/teacher/profile.html', pageName= 'Teacher Profile')

@app.route('/teacher/course')
def teacherCourse():
    return render_template('/teacher/course.html', pageName= 'Teacher Course')

@app.route('/teacher/course/feedback')
def teacherFeedback():
    return render_template('/teacher/feedback.html', pageName= 'Teacher Feedback')

@app.route('/teacher/course/student')
def teacherStudentList():
    return render_template('/teacher/student_list.html', pageName= 'Course Student List')

@app.route('/program_director/statistic')
def programDirectorStatistic():
    return render_template('/program_director/statistic.html', pageName= 'Course Statistic')

@app.route('/program_director/course')
def programDirectorCourse():
    return render_template('/program_director/course.html', pageName= 'Program Director Course')

@app.route('/program_director/course/appeal')
def programDirectorCourseAppealList():
    return render_template('/program_director/appeal_list.html', pageName= 'Course Appeal List')

@app.route('/program_director/course/appeal/detail')
def programDirectorCourseAppealDetail():
    return render_template('/program_director/appeal_detail.html', pageName= 'Course Appeal Detail')

if __name__ == '__main__':
    app.run(debug=True)