from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

#example 
birth_date = (1995, 2, 4)   # year, month , day
age = calculate_age(birth_date) 
print ("Age:", age)
