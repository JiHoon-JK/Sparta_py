a = 'spartacodingclub@gmail.com'

def check_email(email):
    return email.find('@') > -1
print(check_email(a))
