def test_fuction():



    def inner_fuction():
        #nonlocal list_
        print('Я в области видимости функции test_function')

    inner_fuction()

test_fuction()
