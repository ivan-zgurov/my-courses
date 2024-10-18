def softuni_students(*student_data, **course_data):
    valid_students = []
    invalid_students = []

    course_dict = {
        course_id: course_name for course_id, course_name in course_data.items()
    }

    for course_id, username in student_data:
        if course_id in course_dict:
            course_name = course_dict[course_id]
            valid_students.append((username, course_name))
        else:
            invalid_students.append(username)

    # Sort valid students
    valid_students.sort(key=lambda x: x[0])

    # Output
    result = []
    for username, course_name in valid_students:
        result.append(
            f"*** A student with the username {username} has successfully finished the course {course_name}!"
        )

    if invalid_students:
        invalid_students_str = ", ".join(sorted(invalid_students))
        result.append(f"!!! Invalid course students: {invalid_students_str}")

    return "\n".join(result)


# Examples
print(softuni_students(("id_1", "Kaloyan9905"), id_1="Python Web Framework"))

print(
    softuni_students(
        ("id_7", "Silvester1"),
        ("id_32", "Katq21"),
        ("id_7", "The programmer"),
        id_76="Spring Fundamentals",
        id_7="Spring Advanced",
    )
)

print(
    softuni_students(
        ("id_22", "Programmingkitten"),
        ("id_11", "MitkoTheDark"),
        ("id_321", "Bobosa253"),
        ("id_08", "KrasimirAtanasov"),
        ("id_32", "DaniBG"),
        id_321="HTML & CSS",
        id_22="Machine Learning",
        id_08="JS Advanced",
    )
)
