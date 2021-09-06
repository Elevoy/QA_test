#Создать переменную типа String
user_email = 'qa_tester@gmail.com'
print('- user_email:', user_email, type(user_email))
#Создать переменную типа Integer(суммировать, умножить, разделить, разделить без остатка), Float
x=15
y=4
z_1 = x+y
z_2 = x / y
z_3 = x * y
z_4 = int (x / y)
print('- z_1 =', z_1, type(z_1))
print('- z_2 =', z_2, type(z_2))
print('- z_3 =', z_3, type(z_3))
print('- z_4 =', z_4, type(z_4))

#Создать переменную типа Bytes
name = b'50,100,60'
print('-', name, type(name))
#Создать переменную типа List, Tuple
name = list('tel.:4443322')
print('-', name, type(name))
name = tuple('Переменная')
print('-', name, type(name))
#Создать переменную типа Set, Frozen set
name = set('User')
print('-', name, type(name))
name = frozenset('User')
print('-', name, type(name))
#Создать переменную типа Dict
name = dict(первый = 'first', второй = 'second')
print('-', name, type(name))
