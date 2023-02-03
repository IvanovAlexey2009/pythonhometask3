class Iter:
    def __iter__(self):
        values = [1, 2, 3, 4, 5]
        index = 0
        while index < 5:
            yield 2 * values[index]
            index += 1


itr = Iter()

for i in itr:
    print(i)