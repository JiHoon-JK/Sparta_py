a = 'spartacodingclub@naver.com'

def find_email(e):
    return e.split('@')[1].split('.')[0]

print(find_email(a))
