# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Python lists and tuples both store items. They are capable of storing any objects. Historically, tuples are used for heterogenous items and lists are used for homogenous items. Tuples are immutable whereas lists are mutable BUT the members of a tuple can be modified. Only tuples will work for dictionary keys.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets can only contain unique items. They also cannot contain unhashable objects. Checking for memberships in a set is extremey fast because all objects are hashable. A list takes O(n) time in the worst case. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda functions are anonymous functions. They allow us to manipulate data structures very quickly. These lambda functions first normalize and then sort the values by how extreme they are. 

```python

import numpy as np
arr = list(np.random.normal(5,10,24)) # mean 5 sd 10, 24 samples

normalized = lambda x: (x - np.mean(x)) / np.std(x)
normal_array = normalized(arr)
normal_array.sort(key=lambda x: x**(2))
normal_array
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions create a list and are often used as an alternative to for loops or the map function. After creating the list comprehension, we can use filter to refine the list. In the example below, I only keep the items that have a vlue greater than 10


```python
l = [i**2 for i in range(20)]
list(map(lambda x: x ** 2, range(20)))
list(filter(lambda x: x > 10, l))
``` 
---

###Complete the following problems by editing the files below:

###Q5. Datetime

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





