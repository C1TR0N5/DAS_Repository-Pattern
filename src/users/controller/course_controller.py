from flask import Blueprint, jsonify, request
from users.model.course_model import Course
from users.repository.memory_repository import CourseRepository


blueprint = Blueprint('course_controller', __name__)
repository = CourseRepository()


# Endpoint to insert course
@blueprint.route("/courses", methods=["POST"])
def insert_course():
    # Get the course data from the request
    course_data = request.get_json()

    # Create a new course
    course = Course(
        id=len(repository.courses) + 1,
        name=course_data["name"],
        description=course_data["description"]
    )

    # Add the new course to the list of course
    repository.add(course)

    # Return the newly inserted course
    return jsonify(course)


# Endpoint to retrieve course based on course_id
@blueprint.route("/courses/<course_id>", methods=["GET"])
def get_course(course_id):
    # Find the course with the given course_id
    course = repository.get(course_id)

    # If the course is not found, return a 404 error
    if course is None:
        return jsonify({"message": "Course not found"}), 404

    # Return the retrieved course
    return jsonify(course)