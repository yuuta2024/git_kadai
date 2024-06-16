import random

def number_guessing_game():
    # ランダムに3桁の正解の数字を決定
    correct_number = random.randint(100, 999)
    
    attempts = 10

    print("3桁の数字を当ててください。")
    print(f"挑戦回数は{attempts}回までです。")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"{attempt}回目の挑戦: "))

        if guess == correct_number:
            print("正解です！")
            break
        elif guess < correct_number:
            print("不正解です。正解の数字はもっと大きいです。")
        else:
            print("不正解です。正解の数字はもっと小さいです。")

        if attempt == attempts:
            print(f"ゲームオーバー！正解の数字は {correct_number} でした。")

# ゲームを開始
number_guessing_game()
