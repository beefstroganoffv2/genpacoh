from func import Player, create_deck, create_at_deck, player_turn, check_victory
import random

def start_match():
    you = Player("あなた")
    enemy = Player("敵")

    you.deck = create_deck()
    enemy.deck = create_deck()
    at_deck = create_at_deck()

    # 初期ドロー5枚
    for _ in range(5):
        you.draw_card()
        enemy.draw_card()

    # 先攻後攻決定
    turn_order = [you, enemy] if random.choice([True, False]) else [enemy, you]
    print(f"先攻は {turn_order[0].name} です")

    turn_count = 1
    while True:
        print(f"\n=== ターン {turn_count} ===")
        for p_idx, player in enumerate(turn_order):
            opponent = turn_order[1 - p_idx]
            player_turn(player, opponent, at_deck)
            if check_victory(player):
                return
        turn_count += 1
        if turn_count > 50:
            print("\nターン制限に達しました。引き分けです。")
            return

def create_deck_menu():
    print("\n=== デッキ作成 ===")
    print("デッキ作成機能は func.py の create_deck() を編集してください。")

def main():
    while True:
        print("\n===== 玄白王 =====")
        print("1: 対戦")
        print("2: デッキ作成")
        print("3: 終了")
        choice = input("番号を入力してください: ")

        if choice == "1":
            start_match()
        elif choice == "2":
            create_deck_menu()
        elif choice == "3":
            print("終了します。")
            break
        else:
            print("正しい番号を入力してください。")

if __name__ == "__main__":
    main()