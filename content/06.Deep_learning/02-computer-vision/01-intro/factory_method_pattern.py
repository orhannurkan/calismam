class A(object):
    def print(self):
        print("A")


class B(object):
    def print(self):
        print("B")


def get(obj=""):
    objs = dict(a=A(), b=B())
    return objs[obj]


a = get("a")
print(a)
a.print()
b = get("b")
print(b)
b.print()
