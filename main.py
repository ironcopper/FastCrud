from fastapi import FastAPI, Body

app = FastAPI()

courses_db = [
    {
        "id": 1,
        "instructor": "Joshua",
        "title": "Python",
        "category": "Development"
    },
    {
        "id": 2,
        "instructor": "John",
        "title": "Java",
        "category": "Development"
    },
    {
        "id": 3,
        "instructor": "John",
        "title": "Deep Learning",
        "category": "AI"
    },
    {
        "id": 4,
        "instructor": "Seth",
        "title": "Jenkins",
        "category": "Devops"
    }
]

@app.get("/")
async def hello():
    return {"msg": "hello"}

@app.get("/courses")
async def get_all_courses():
    return courses_db

#path parameters
@app.get("/courses/{course_title}")
async def get_course(course_title):
    for course in courses_db:
        if course.get('title').casefold() == course_title.casefold():
            return course

#this function does not work due to path çakışması
@app.get("/courses/{course_id}")
async def get_course(course_id):
    for course in courses_db:
        if course.get('id') == course_id:
            return course

#it can work by creating new path
@app.get("/courses/byid/{course_id}")
async def get_course(course_id):
    for course in courses_db:
        if course.get('id') == course_id:
            return course

#by query
@app.get("/courses/")
async def get_category_by_query(category):
    courses_to_return = []
    for course in courses_db:
        if course.get('category').casefold() == category.casefold():
            courses_to_return.append(course)
    return courses_to_return

#query and path used
@app.get("/courses/{course_instructor}/")
async def get_instructor_category_by_query(course_instructor, category):
    courses_to_return = []
    for course in courses_db:
        if course.get('instructor').casefold() == course_instructor.casefold() and course.get('category').casefold() == category.casefold():
            courses_to_return.append(course)
    return courses_to_return

#post
@app.post("/courses/create_course")
async def create_course(new_course=Body()):
    courses_db.append(new_course)

#put updates
@app.put("/courses/update_course")
async def update_course(updated_course=Body()):
    for index in range(len(courses_db)):
        if courses_db[index].get('id') == updated_course.get('id'):
            courses_db[index] = updated_course


#delete
@app.delete("/courses/delete_course/{course_id}")
async def delete_course(course_id):
    for index in range(len(courses_db)):
        if courses_db[index].get('id') == course_id:
            courses_db.pop(index)
            break
