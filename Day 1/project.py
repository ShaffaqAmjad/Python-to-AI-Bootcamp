
def analyze(marks):
    total = sum(marks)
    avg = total / len(marks)

    if avg > 90:
        print("Excellent")
    elif avg > 70:
        print("Normal")
    elif avg > 50:
        print("Needs improvement")
    else:
        print("Bad Result")

    for mark in marks:
        print(mark)

    print("Total:", total)
    print("Avg:", round(avg, 2))


student_marks = [40, 80, 90, 100, 50]
analyze(student_marks)
