class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.new_list = []

    def __iter__(self):
        #self.new_list = iter([])
        self.iter_list = iter(self.list_of_list)
        self.cursor = -1
        return self

    def __next__(self):
        
        self.cursor += 1
        if len(self.new_list) == self.cursor:  
            self.new_list = None
            self.cursor = 0
            while not self.new_list:  
                self.new_list = next(self.iter_list) 
        return self.new_list[self.cursor]



       # if self.list_of_list is None: 
            #raise StopIteration
        
       #try:
            #res = next(self.new_list)
        #except StopIteration:

        #self.cursor += 1
        #self.next = next(iter(self.list_of_list.pop()))
        #self.new_list.append(self.next)
        #return iter(self.new_list)


list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

if __name__ == '__main__': #так выводит результат
    for item in FlatIterator(list_of_lists_1):
        print(item)
    

def test_1(): #не работает, не могу понять где ошибка 

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()