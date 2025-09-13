import matplotlib.pyplot as plt
# Data
grades = ["A", "B", "C", "D"]
counts = [2, 5, 3, 1]


plt.bar(grades, counts, color="skyblue", edgecolor="black")


plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.title("Grade Distribution")

# Show chart
plt.show()
