# Homework – Dictionaries and Functions

Solve **at least one question**
It is recommended to solve **more than one**
All solutions must be written in **Python**

## Question 1 – Digital Business Card

<img src="card.jpg" style="width:50%"/>

Write a program that asks the user to enter the following information:

* name
* email
* phone number
* job title

After receiving the input:

1. Create a **dictionary** that stores this information
2. Print the dictionary
3. Print a formatted **business card**

Example input:

```
Enter name: Dana Levi
Enter email: dana@gmail.com
Enter phone: 0501234567
Enter job title: Data Analyst
```

Possible output:

```
{'name': 'Dana Levi', 'email': 'dana@gmail.com', 'phone': '0501234567', 'job_title': 'Data Analyst'}

--- Business Card ---
Name: Dana Levi
Email: dana@gmail.com
Phone: 0501234567
Job Title: Data Analyst
```

## Question 2 – Statistics Function

<img src="stats.jpg" style="width:50%"/>

Create a function called:

```
get_statistics
```

The function receives a **list of numbers** and returns a **dictionary** with the following statistics:

* sum
* average
* minimum
* maximum
* length of the list

Function structure:

```python
def get_statistics(numbers):
    pass
```

Demo code:

```python
nums = [4, 8, 2, 10, 6]

result = get_statistics(nums)

print(result)
```

Possible output:

```
{
    'sum': 30,
    'avg': 6.0,
    'min': 2,
    'max': 10,
    'length': 5
}
```

## Question 3 – Merge Two Dictionaries

Create a function that receives **two dictionaries**.

Each dictionary has:

* `key` → string
* `value` → string

The function should create and return a **third dictionary** that combines both dictionaries.

Rules:

* If a key appears in **only one dictionary**, add it normally
* If the same key appears in **both dictionaries**, choose the value with the **longer string**
* If both strings have the **same length**, keep the value from the **first dictionary**

Example:

```python
dict1 = {
    "name": "Dan",
    "city": "Tel Aviv",
    "job": "Dev"
}

dict2 = {
    "name": "Daniel",
    "city": "TA",
    "country": "Israel"
}
```

Possible result:

```
{
    "name": "Daniel",
    "city": "Tel Aviv",
    "job": "Dev",
    "country": "Israel"
}
```

**Submission email:** [pythonai211225+python17dict@gmail.com](mailto:pythonai211225+python17dict@gmail.com)

country -> Israel
```
