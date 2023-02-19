import random as r
variants = ['камень', 'ножницы', 'бумага']

def game():
    while True:
        comp_choice = r.choice(variants)
        user_choice = input('Выбери свой предмет!\n').lower()
        if user_choice in variants:
            if comp_choice == user_choice:
                print('Ничья, попробуйте снова\n')
                start()
                break
            elif user_choice == 'камень':
                if comp_choice == 'ножницы':
                    print('Вы победили, камень разбивает ножницы!\n')
                    start()
                    break
                else:
                    print('Вы проиграли, бумага накрывает камень!\n')
                    start()
                    break
            elif user_choice == 'ножницы':
                if comp_choice == 'бумага':
                    print('Вы победили, ножницы режут бумагу!\n')
                    start()
                    break
                else:
                    print('Вы проиграли, камень разбивает ножницы!\n')
                    start()
                    break
            else:
                if comp_choice == 'камень':
                    print('Вы победили, бумага накрывает камень!')
                    start()
                    break
                else:
                    print('Вы проиграли, ножницы режут бумагу!')
                    start()
                    break
        else:
            print('Неверный ввод, напишите одно из слов: камень, ножницы, бумага')

def start():
    while True:
        ans = input('Желаешь начать игру "Камень-ножницы-бумага"? Д - Да, Н - Нет\n').lower()
        if ans == 'д':
            print('Давай приступим к игре "Камень-ножницы-бумага"!\n')
            return game()
            break
        elif ans == 'н':
            print('В другой раз, так в другой раз(( Пока...\n')
            break
        else:
            print('Введи корректный ответ!')

start()