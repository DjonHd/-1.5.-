immutable_var = (1,2,'a','b')
print(immutable_var)
print(immutable_var[3])
#кортеж не поддерживает обращение по элементам,
# не возможно заменить один элемент на другой,
# кортеж являеться неизменяемой коллекцией
print('Immutable var: '+ str(immutable_var))
mutable_list = [1,2,'a','b','apple']
print(mutable_list)
mutable_list[4]='Modified'
print('Mutable list: ' + str(mutable_list))



