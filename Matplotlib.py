import matplotlib.pyplot as plt

students_names = ["Irfan", "Sana", "Hayyan", "Rayyan", "Fatima", "Areeb", "Ibrahim", "Musa"]
students_marks = [90, 95, 97, 85, 90, 87, 80, 82]
marks_perc = []
for x in students_marks:
    res = (x/50)*100
    marks_perc.append(res)
print(marks_perc)

import matplotlib.pyplot as plt

# Sample data
students_names = ["Hayyan", "Rayyan", "Fatima", "Maryam", "Sana", "Irfan"]
students_marks = [100, 82, 90, 92, 99, 95]
marks_perc = [100.0, 82.0, 85.0, 92.0, 95.0, 95.0 ]  # Assuming out of 100

# Line chart
def marks_line_chart():
    plt.plot(students_names, students_marks)
    plt.title("Students Marks Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Students Marks")
    plt.show()

marks_line_chart()

# Bar chart
def percentage_bar_chart():
    plt.bar(students_names, marks_perc)
    plt.title("Students Percentage Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Student Percentage")
    plt.show()

percentage_bar_chart()
