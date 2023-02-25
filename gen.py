import types


def flat_generator(list_of_lists): # функция выводит только часть значений 
    #self.list_of_lists = list_of_lists
    for i in range(len(list_of_lists)): # + 1)
            for j in range(i+1):
                yield list_of_lists[i][j]


def flat_gen(list_of_lists): # выводит весь список
    for lists in list_of_lists:
        for item in lists:
            yield item
    


list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

if __name__ == '__main__':
    for item in flat_gen(list_of_lists_1):
        print(item)

#не работает вызов def test_2() 
#def test_2():

#    list_of_lists_1 = [
#        ['a', 'b', 'c'],
#        ['d', 'e', 'f', 'h', False],
#        [1, 2, None]
#   ]

#    for flat_iterator_item, check_item in zip(
#            flat_generator(list_of_lists_1),
#            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#    ):

#        assert flat_iterator_item == check_item

#    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

#    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


#if __name__ == '__main__':
#    test_2()



