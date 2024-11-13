import janken_judge
import player
import computer

def janken_main():
    count = 0
    for i in range(0, 3):
        player_hand = player.pon()
        computer_hand = computer.pon()
        janken_list = ['グー', 'チョキ', 'パー']
        print(f'あなたの手:{janken_list[player_hand - 1]}')
        print(f'コンピュータの手:{janken_list[computer_hand - 1]}')
        win_or_lose = janken_judge.judge(computer_hand, player_hand)
        if win_or_lose == 1:
            print('プレイヤーの勝ちです！')
            count += 1
        elif win_or_lose == 2:
            print('コンピュータの勝ちです！')
        else:
            while win_or_lose == 3:
                print('あいこです！もう一度入力してください。')
                player_hand = player.pon()
                computer_hand = computer.pon()
                print(f'あなたの手:{janken_list[player_hand - 1]}')
                print(f'コンピュータの手:{janken_list[computer_hand - 1]}')
                win_or_lose = janken_judge.judge(computer_hand, player_hand)
            
            if win_or_lose == 1:
                print('プレイヤーの勝ちです！')
                count += 1
            else:
                print('コンピュータの勝ちです！')
    
    print('【最終結果】')
    print(f'あなた:{count}勝')
    print(f'コンピュータ:{3 - count}勝')    
    if count >= 2:
        print('あなたの総合勝利です！')
    else:
        print('コンピュータの総合勝利です！')
        
janken_main()

