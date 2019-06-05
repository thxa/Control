class Control:
    def __init__(self, obj):
        self.obj = obj
        self.length = obj.__len__()
        self.index = 0
        self.val = obj[self.index]

    def isEnd(self):
        return self.length - 1 <= self.index

    def isErl(self):
        return 0 >= self.index

    def next(self):
        result = "[!] I can't next this is last element"
        if not self.isEnd():
            self.index += 1
            result = self.updateVal(self.obj[self.index])
        # else:
        #     self.index = 0
        #     result = self.updateVal(self.obj[self.index])
        return result

    def prev(self):
        result = "[!] I can't previous this is first element"
        if not self.isErl():
            self.index -= 1
            result = self.updateVal(self.obj[self.index])
        # else:
        #     self.index = self.length - 1
        #     result = self.updateVal(self.obj[self.index])
        return result

    def updateVal(self, val):
        self.val = val
        return self.val


mylist = ["apple", "banana", "cherry"]
obj_c = Control(mylist)


def dump_next(obj):
    print("____next____")
    print("length:", obj.length)
    print("index:", obj.index + 1)
    print("value:", obj.val)
    print("next:", obj.next())


def dump_prev(obj):
    print("____prev____")
    print("length:", obj.length)
    print("index:", obj.index + 1)
    print("value:", obj.val)
    print("prev:", obj.prev())


print(obj_c.obj)
for i in range(3):
    dump_next(obj_c)


print(obj_c.obj)
for i in range(3):
    dump_prev(obj_c)


print(obj_c.val)
