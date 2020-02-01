people = [{'name':'bob','age':20},{'name':'mark','age':17}]

for person in people:
    print(person['name'],person['age'])

def get_age(myname):
    for person in people:
        if person['name'] == myname:
            return person['age']
    return "해당하는 이름이 없습니다."

print(get_age('bob'))
print(get_age('mark'))