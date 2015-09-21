import re
import csv
from collections import Counter

with open('python/faculty.csv', 'r') as file:
    faculty = file.read()
    
    
def count_degrees(string):
    """Counts the number of degrees in each case
    """
    degrees = re.findall('(?:\\n.*?,\s)(.*?)(?:,)', faculty)
    return Counter(degrees)

def count_titles(string):
    """Counts the number of titles"""
    titles = re.findall('(?:\\n.*,\s.*?,)(.*)(?:,)', string)
    return Counter(titles)

def show_emails(string):
    """parses data to show all emails """
    return re.findall('(?:\\n.*,\s.*?,.*,)(.*)(?:\\n)', string)

def show_domains(string):
    """Returns a list of the unique domains used in Python"""
    return set(re.findall('(?:\\n.*,\s.*?,.*,.*@)(.*)(?:\\n)', string))
