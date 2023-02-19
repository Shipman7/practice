from random import *

def is_valid(n, x, y):
    return n.isdigit() and x <= int(n) <= y and float(n) - int(float(n)) == 0


def num_true(down_num = 0, up_num = 10**20):
    while True:
        guess = input(f"Введите число от {down_num} до {up_num}: ")
        if is_valid(guess, down_num, up_num):
            return int(guess)
        else:    
            print(f'А может быть все-таки введем целое число от {down_num} до {up_num}?')

def srav_dig(down_num, up_num):
    n = randint(down_num, up_num)
    total = 0
    while True:
        m = num_true(down_num, up_num)
        total += 1
        if m < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif m > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            print("Количество попыток: ", total)
            break 

def cont_game():
    qn = input('Хотите продолжить ("д"/"н")?\n')
    while True:
        if qn not in ('y', 'д', 'n', 'н'):
            input('Вроде взрослый человек, а на вопрос нормально ответить не может...\nПродолжим ("д"/"н")?\n')
            continue
        elif qn == "д":
            return True
        elif qn == "н":
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            return False
        
def igra():
    print("Добро пожаловать в числовую угадайку")
    while True:
        print('Укажите, в каком диапазоне Вы готовы угадывать числа:\n')
        x, y = num_true(), num_true()
        if x > y:
            x, y = y, x
        print('Введите число от', x, 'до', y, '\n')
        srav_dig(x, y)
        if cont_game():
            continue
        else:
            break

igra()           
                    
            

   