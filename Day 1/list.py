
# List practice
skills = ["ML", "Python", "Java"]

print(skills[2])

skills[2] = "Pandas"
print(skills[2])

print(len(skills))
print("maths" not in skills)

skills.append("Maths")
print(skills)

skills.extend(["Calculus", "Stats", "Prob"])
print(skills)

# Sorting numbers
num = [10, 30, 20]
sorted_num = sorted(num)
print(sorted_num)

# Dictionary practice
student = {
    "name": "Shaffaq",
    "age": 19,
    "gpa": 3.94
}

print(student.get("age"))
print(student.keys())
print(student.values())
