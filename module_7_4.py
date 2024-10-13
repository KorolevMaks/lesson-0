team_1 = 'Мастера кода'
team_2 = 'Волшебники данных'


def num(team1_num, team2_num):
    print('В команде %s участников: %s ' % (team_1, team1_num))
    print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))


def score(team_name, score_, team_time):
    if team_name == team_1:
        print("Команда {} решила задач: {} !".format(team_1, score_))
        print(" {} решили задачи за {} !".format(team_1, team_time))
    else:
        print("Команда {} решила задач: {} !".format(team_2, score_))
        print(" {} решили задачи за {} !".format(team_2, team_time))


def challenge_result(score_1, score_2, team1_time, team2_time):
    print(f"Команды решили {score_1} и {score_2} задач.")
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = "Победа команды Мастера кода!"
    elif score_1 <= score_2 and team1_time < team2_time:
        result = "Победа команды Волшебники Данных!"
    else:
        result = "Ничья!"
    return result


num(5, 6)
score("Мастера кода", 40, 1552.512)
score("Волшебники Данных", 42, 2153.31451)
print(challenge_result(40, 42, 1552.512, 2153.31451))
