a = ['사과','감','감','배','사과','포도','딸기','사과','배']

def count_list(a_list):
    result={}
    for element in a_list:
        if element in result:
            result[element] += 1
        else:
            result[element] = 1
    return result


print(count_list(a))