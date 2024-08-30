def test_function (a = 0):
    def inner_function (b = 0):
        print('Я в области видимости функции test_function')

    inner_function(1)
    return a

c = test_function()
d = inner_function() #питон не видит подфункцию inner_function т.к. она существует только внутри функции test_function
print(c , d)
