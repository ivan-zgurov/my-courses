def gather_credits(needed_credits, *courses):
    enrolled_courses = {}
    gathered_credits = 0

    for course_name, course_credits in courses:
        if course_name not in enrolled_courses and gathered_credits < needed_credits:
            enrolled_courses[course_name] = course_credits
            gathered_credits += course_credits

        if gathered_credits >= needed_credits:
            break

    # Output
    if gathered_credits >= needed_credits:
        sorted_courses = sorted(enrolled_courses.keys())
        return f"Enrollment finished! Maximum credits: {gathered_credits}.\nCourses: {', '.join(sorted_courses)}"
    else:
        credits_shortage = needed_credits - gathered_credits
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."


# Example usage
print(
    gather_credits(
        80,
        ("Basics", 27),
    )
)

print(
    gather_credits(
        80,
        ("Advanced", 30),
        ("Basics", 27),
        ("Fundamentals", 27),
    )
)

print(
    gather_credits(
        60, ("Basics", 27), ("Fundamentals", 27), ("Advanced", 30), ("Web", 30)
    )
)
