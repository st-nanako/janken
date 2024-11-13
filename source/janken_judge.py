import computer
import player

# 1が勝ち,2が負け,3があいこ
def judge(computer, player):
    judge = -1
    if computer == player:
        judge = 3
    elif computer == 1 and player == 3 or computer == 2 and player == 1 or computer == 3 and player == 2:
        judge = 1
    else:
        judge = 2
    return judge