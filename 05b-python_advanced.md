## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

###Part I - Regular Expressions  

Use regular expressions to:

####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>> ' Sc.D.', 'Ph.D.', ' PhD', ' Ph.D.', ' Ph.D', ' MD MPH Ph.D',
       ' B.S.Ed. M.S. Ph.D.', ' JD MA MPH MS PhD', ' PhD ScD', '0', ' ScD'
>So we have 11 different permutations but we have BSEd, Sc.D Ph.D, MD, MPH, 0 (probably nothing or unknown), and B.S.ED  

> ```
 Ph.D.                 15
 PhD                    7
 Sc.D.                  4
 Ph.D                   4
 ScD                    1
 B.S.Ed. M.S. Ph.D.     1
Ph.D.                   1
 JD MA MPH MS PhD       1
 MD MPH Ph.D            1
 PhD ScD                1
0                       1```



####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>> ```Professor of Biostatistics              13
Associate Professor of Biostatistics    12
Assistant Professor of Biostatistics    11
Assistant Professor is Biostatistics     1```
The is instead of of is obviously a typo. 


####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>> ['bellamys@mail.med.upenn.edu',
 'bryanma@upenn.edu',
 'sellenbe@upenn.edu',
 'ruifeng@upenn.edu',
 'pgimotty@upenn.edu',
 'hsu9@mail.med.upenn.edu',
 'whwang@mail.med.upenn.edu',
 'jrlandis@mail.med.upenn.edu',
 'mingyao@mail.med.upenn.edu',
 'rlocalio@upenn.edu',
 'knashawn@mail.med.upenn.edu',
 'mputt@mail.med.upenn.edu',
 'michross@upenn.edu',
 'msammel@cceb.med.upenn.edu',
 'hshou@mail.med.upenn.edu',
 'alisaste@mail.med.upenn.edu',
 'rxiao@mail.med.upenn.edu',
 'dxie@upenn.edu']


####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>> {'cceb.med.upenn.edu', 'mail.med.upenn.edu', 'upenn.edu'}

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [\
              ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
              ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
                            ],
              'Li': [\
              ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
              ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
              ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
                            ]
            }
```
Print the first 3 key and value pairs of the dictionary:

>> Pandas is better suited for this problem than pure python

>> 'Bellamy': ['Sc.D.', 'Associate Professor ', 'bellamys@mail.med.upenn.edu'],
 'Bilker': ['Ph.D.', 'Professor ', 'warren@upenn.edu'],
 'Bryan': ['PhD', 'Assistant Professor ', 'bryanma@upenn.edu']

####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
                ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],\
                ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
                ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
                ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
            }
```

Print the first 3 key and value pairs of the dictionary:

>>('Bellamy', 'Scarlett'): ['Sc.D.',
  'Associate Professor ',
  'bellamys@mail.med.upenn.edu'],
 ('Bilker', 'Warren'): ['Ph.D.', 'Professor ', 'warren@upenn.edu'],
 ('Bryan', 'Matthew'): ['PhD', 'Assistant Professor ', 'bryanma@upenn.edu'],

####Q8.  It looks like the current dictionary is sorted by first name.  Sort by last name and print the first 3 key and value pairs.  

>> I just made the order in `last_name`, `first_name` order to begin with to avoid this problem. 

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

