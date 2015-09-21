import pandas as pd
def csv_to_dict():
    """Takes a csv and makes it into a dict """
    faculty = pd.read_csv('python/faculty.csv')
    faculty['first_name'] = faculty.name.str.split(' ').str.get(0)
    faculty['last_name'] = faculty.name.str.split(' ').str.get(-1)
    faculty['b_title'] = faculty.title.str.replace('(of|is) Biostatistics', '')
    faculty = faculty.rename(columns={' degree': 'degree'})
    faculty.degree = faculty.degree.str.strip(' ')
    #faculty['b_title'] = faculty.title.str.replace('is Biostatistics', '')
    faculty_dict = {row[1].last_name: [row[1].degree, row[1].b_title, row[1].email] for row in faculty.iterrows()}
    faculty_dict


# Part 2
aculty_dict = {(row[1].last_name, row[1].first_name): [row[1].degree, row[1].b_title, 
        row[1].email] for row in faculty.iterrows()}
