def pon():
    while (True):
        user = input('じゃんけんゲーム！\n1.グー\n2.チョキ\n3.パー\nあなたの手を選択してね！>>>')
        if user.isdigit() == False:
            print('数字で入力してください。')
        elif user < 1 or 3 < user:
            print('異常な値です。確認してください。')
        else:
            user = int(user)
            break
    return user
