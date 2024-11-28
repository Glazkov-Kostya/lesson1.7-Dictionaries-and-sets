# phone_book = {'Denis'(ключ): 88005553535(значение),}
# {} - словарь это неупорядоченная коллекция (изменяемый тип данных) -
#  - (при обращении к несуществующему объекту, добавит его в словарь). -
# - ключ - неизменяемый об. (не может быть списком и т.д).
# del - операция удаления
# .update({}) - обновить несколько пар сразу, в {} пишем нужные ключи
# .pop метод .pop удаляет ключ и возвращает соответствующее ему значение
# .keys() позволит получить коллекцию из ключей в словаре
# .values() позволит получить коллекцию из значений в словаре
# .items() позволит получить коллекцию из пар(ключ+значение) в словаре
# set(множество) хранит в себе только уникальные значения, а так же хранит в себе -
# - разные типы данных
# .discard - удаление и при этом не будет выдавать ошибку, если элемент не был найден во множестве
# .remove - удаление
# .add - добавление элемента
phone_book = {'Denis': [88005553535, 204324], 'Max': 88005553534,}
print(phone_book)
print(phone_book['Denis'])
phone_book['Denis'] = 1513489346
print(phone_book)
phone_book['Anton'] = 85993473472
print(phone_book)
del phone_book['Max']
print(phone_book)
phone_book.update({'Sahsa': 15889237549,
                   'Alex': 12490842029})
print(phone_book.get('Denis'))
print(phone_book.get('Kamila', 'Такого ключа нет'))
print(phone_book)
a = phone_book.pop('Anton')
print(phone_book)
print(a)
list_ = [1,2,3]
list_.pop(0)
print(list_)
print(phone_book.keys())
print(phone_book.values())
print(phone_book.items())
set_ = {1,2,3,4,5,1,2,3,4, 'String', True, (1,2,3)}
print(set_)
list_ = [1,1,1,1,2,3,2,2]
# print(set(list_))
list_ = set(list_)
print(list_)
#print(list_.discard(1))
print(list_.remove(1))
print(list_)
print(list_.add(1))
print(list_)
print(list_.add(5))
print(list_)