# Hint:  use Google to find python function

import arrow
def day_difference(d1, d2, style='MM-DD-YYYY'):
    """Calculates the differences between dates d1 and d2 assuming American date system.


    params
    ---
    d1: string of format style
    d2: string of format style
    style: string dictating how 
    """
    d1 = arrow.get(d1, style)
    d2 = arrow.get(d2, style)
    return abs((d1- d2).days)



####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

day_difference(date_start, date_stop, 'MM-DD-YYYY')


####b)  
date_start = '12312013'  
date_stop = '05282015'  

day_difference(date_start, date_stop, 'MMDDYYYY')

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

day_difference(date_start, date_stop, style='DD-MMM-YYYY')