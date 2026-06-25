name = "John"
age = 20
language = "Python"
hours = 3

# John is 20years old.
print(name, "is", age, "years old.")

# John is 20 years old. He studies Python 3 hours a day.
print(name, "is", age, "years old. He studies", language, hours, "hours a day.")

# Using f-string
print(f"{name} is {age} years old. He studies {language} {hours} hours a day.")

sub1 = 78
sub2 = 87
sub3 = 83

# John scored {} marks in total
print(f"{name} scored {sub1 + sub2 + sub3} marks in total.")
print(name, "scored", sub1 + sub2 + sub3, "marks in total.")

# Average marks of John
avg = (sub1 + sub2 + sub3) / 3
print(f"{name} got {round(avg, 1)} average marks.")

# Print the percentage(%) of John
# for % we need to add total marks of all subjects
# Let's say each sub marks is 100 so total is 300
obtained_marks = sub1 + sub2 + sub3
total_marks = 300
percent = (obtained_marks / total_marks) * 100
print(f"{name} got {round(percent, 2)}%")
