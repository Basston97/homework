import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        return True
    else:
        return False

email = "boston1999997@gmail.com"
if is_valid_email(email):
    print(f"{email} - это допустимый адрес электронной почты.")
else:
    print(f"{email} - это недопустимый адрес электронной почты.")