# start_python_file.py
# Lab 03 – Python Collections Practice
# Covers: Lists, Tuples, Sets, Dictionaries

# ============================================================
# Question 1: Student Grades List
# ============================================================
print(">>> Lab03 is running <<<")

print("=" * 50)
print("Question 1: Student Grades List")
print("=" * 50)

print()
grades = [85, 92, 78, 95, 88]
grades.append(90)
grades.sort()

print("Sorted grades:", grades)
print("Highest grade:", grades[-1])
print("Lowest grade:", grades[0])
print("Total number of grades:", len(grades))

# ============================================================
# Question 2: Shopping Cart
# ============================================================
print("=" * 50)
print("Question 2: Shopping Cart")
print("=" * 50)

print()
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]

print("Number of apples:", cart.count("apple"))
print("Position of milk:", cart.index("milk"))

cart.remove("apple")
removed_item = cart.pop()
print("Removed item using pop:", removed_item)

print("Is banana in cart?", "banana" in cart)
print("Final cart:", cart)

# ============================================================
# Question 3: Coordinate System (Tuples)
# ============================================================
print("=" * 50)
print("Question 3: Coordinate System")
print("=" * 50)

print()
point1 = (3, 5)
point2 = (7, 2)

print("Point 1:", point1)
print("Point 2:", point2)

x1, y1 = point1
x2, y2 = point2

print(f"x1 = {x1}, y1 = {y1}")
print(f"x2 = {x2}, y2 = {y2}")

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Distance between points:", distance)

chars = tuple("PYTHON")
print("Characters tuple:", chars)

for ch in chars:
    print(ch)

# ============================================================
# Question 4: Class Attendance (Sets)
# ============================================================
print("=" * 50)
print("Question 4: Class Attendance")
print("=" * 50)

print()
monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

monday_class.add("Grace")

print("Monday class:", monday_class)
print("Wednesday class:", wednesday_class)

both = monday_class & wednesday_class
either = monday_class | wednesday_class
only_monday = monday_class - wednesday_class
only_one = monday_class ^ wednesday_class

print("Attended both classes:", both)
print("Attended either class:", either)
print("Only Monday:", only_monday)
print("Only one class (not both):", only_one)

print("Is Monday subset of all students?", monday_class <= either)

# ============================================================
# Question 5: Contact Book (Dictionaries)
# ============================================================
print("=" * 50)
print("Question 5: Contact Book")
print("=" * 50)


print()
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

print("Alice's number:", contacts["Alice"])

contacts["Diana"] = "555-4321"
print("Contacts after adding Diana:", contacts)

contacts["Bob"] = "555-0000"
print("Contacts after updating Bob:", contacts)

del contacts["Charlie"]
print("Contacts after deleting Charlie:", contacts)

print("All names:", contacts.keys())
print("All numbers:", contacts.values())
print("Total contacts:", len(contacts))
