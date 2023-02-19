from functools import wraps
def decor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return sum(func(*args, **kwargs))
    return wrapper

@decor
def get_list(s):
    return list(map(int, s.split()))
s = input()
print(get_list(s))



def dec_sort(func):
    def wr(*args):
        lst = func(*args)
        return sorted(lst)
    return wr
@dec_sort
def get_list(s):
    return [int(i) for i in s.split()]

s = input()
lst = get_list(s)
print(*lst)


def show_menu(func):
    def wrap(*args, **kwargs):
        m = func(*args, **kwargs)
        for id, val in enumerate(m):
            print(f'{id+1}. {val}')
    return wrap
@show_menu
def get_menu(s):
    return s.split()

s = input()
get_menu(s)


def func_show(func):
    def wrap(*args):
        res = func(*args)
        print(f'Площадь прямоугольника: {res}')
    return wrap

@func_show
def get_sq(width, height):
    return width * height

a, b = [int(i) for i in input().split()]
get_sq(a, b)