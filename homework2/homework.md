# Homework - Lab

## Exercise 1

Implement a Book class.

You should have a counter attribute that keeps track of how many books have been instanciated in your program.

## Exercise 2

Create a class called Student.

The class should have the following class attributes:

```
school_name = "Vanier College"
student_count = 0
```

Each student object should have the following instance attributes:

```
name
program
grade
```

Every time a new Student object is created, student_count should increase by 1.

Add a method called `display_info()` that prints something like:

```
Alice studies Web Development at Vanier College. Grade: 88
```

Create at least three students and call display_info() for each one.

## Exercise 3

Create a class called Product.

It should have these class attributes:

```
category = "Electronics"
tax_rate = 0.15
```

Each product should have these instance attributes:

```
name
price
```

Add a method called `price_with_tax()` that returns the price after tax.

Formula:
`price + (price * tax_rate)`

Create at least three products and print their prices with tax.

Then change the class attribute:

`Product.tax_rate = 0.20`

Print the prices with tax again.

## Exercise 4

Create a class called Employee.

The class should have:

```
company_name = "TechNova"
bonus_rate = 0.10
employee_count = 0
```

Each employee should have:

```
name
salary
```

Every time an employee is created, employee_count should increase by 1.

Add a method called `calculate_bonus()`.

It should return:

`salary * bonus_rate`

Add another method called `display_employee()` that prints:

```
John works at TechNova. Salary: 50000. Bonus: 5000.0
```

Create three employees.

Then:

- Display all employees.
- Change Employee.bonus_rate to 0.20.
- Display all employees again.
- Give only one employee a custom bonus rate:

  `employee1.bonus_rate = 0.50`

- Display all employees again.
- Change Employee.bonus_rate to 0.05.
- Display all employees again.

At the end, write a comment explaining which employee has a shadowed bonus_rate
