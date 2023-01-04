name = "Denys"
name = name + " Trohymetz"

age = 13
birth_date = "18.03"

print("Hello " + name)
print("My age is " + str(age))
print("My age is %s, I was born at %s" % (age, birth_date))

print("After 30 years I will be %s years old" % (age + 30))
print("After 30 years I will be " + str(age + 30) + " years old")

age = 17
is_instructor_near_your = True  # False

print(age >= 18)

if age >= 18 or is_instructor_near_your:
    print("You can drive")
else:
    print("You can't drive")