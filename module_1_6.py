my_dict = {"Nikita" : 2000, "Zhenya" : 2001}
print("Словарь:" , my_dict)
print("Существующее:" , my_dict["Nikita"])
print("Отсутствующее:" , my_dict.get("natasha"))
my_dict ["Nastya"] = 2002
my_dict ["Stas"] = 1992
print("Удаленное значение:" , my_dict["Zhenya"])
del my_dict["Zhenya"]
print('Новый словарь:' ,  my_dict)
print('____________________________________')
my_set = { 't' , 1 , 1 , 't' , 2 , 3 , 4 , 't'}
print("стандартное:" , my_set)
my_set.add(5)
my_set.add('Urban')
my_set.discard('t')
print('новое:' , my_set)
