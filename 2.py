import random

class RandomNumberIterator:
    def __init__(self, count, min_num, max_num):
        self.count = count
        self.min_num = min_num
        self.max_num = max_num
        self.current_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_count < self.count:
            self.current_count += 1
            return random.randint(self.min_num, self.max_num)
        else:
            raise StopIteration


iterator = RandomNumberIterator(5, 1, 100)  
for num in iterator:
    print(num)

    import random

class RandomNumberIterator:
    def __init__(self, count, min_num, max_num):
        self.count = count
        self.min_num = min_num
        self.max_num = max_num
        self.current_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_count < self.count:
            self.current_count += 1
            return random.randint(self.min_num, self.max_num)
        else:
            raise StopIteration

iterator = RandomNumberIterator(5, 1, 100)  
for num in iterator:
    print(num)

    import random

class rand():
    def __init__ (self, count, minn, maxx):
        self.count = count
        self.min = minn
        self.max = maxx
        
    def generator(self):
        while self.count > 0:
            yield random.randint(self.min, self.max)
            self.count -= 1
a = rand(5,1,100)
for num in a.generator():
    print (num)

    import random 

class Data:
    def __init__(self, *info):
        self.info = list(info)
 
    def __getitem__(self, i):
        return self.info[i]
 
 
class Teacher:
    def __init__(self):
        self.work = 0
 
    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)
            self.work += 1
 
 
class Pupil:
    def __init__(self):
        self.knowledge = []
 
    def take(self, info):
        self.knowledge.append(info)
        
    def forgot(self):
        self.knowledge.remove(random.choice(self.knowledge))
        
    def print(self):
        print(self.knowledge)
        
lesson = Data('class', 'object', 
'inheritance', 'polymorphism', 
'encapsulation')
pety = Pupil()
pety.print()
pety.take(lesson[3])
pety.take(lesson[1])
pety.take(lesson[2])
pety.print()
pety.forgot()
pety.print()