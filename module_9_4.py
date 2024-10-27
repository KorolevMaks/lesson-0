from  random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, z: x == z, first, second)))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, mode='w', encoding='UTF-8') as file:
            for i in data_set:
                file.write(str(i))
                file.write('\n')
    return write_everything
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, *word):
        self.words = word

    def __call__(self):
        word = choice(self.words)
        return word
first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Это не ко мне', 'Спроси еще раз','Ничего ты не знаешь, Джон Сноу', 'Я - Дейнерис Бурерожденная из дома Таргариенов, законная наследница Железного Трона, законная королева андалов и Первых Людей, защитница Семи Королевств, Матерь Драконов, кхалиси Великого травяного моря, неопалимая, Разрушительница Оков.')
print(first_ball())
print(first_ball())
print(first_ball())
