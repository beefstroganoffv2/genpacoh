import random
from atcard import ATCard
from card import Card

# --- プレイヤークラス ---
class Player:
    def __init__(self, name):
        self.name = name
        self.deck = []
        self.hand = []
        self.used_cards = []
        self.written_AT = set()  # 書き起こし済みATカード種類

    def draw_card(self):
        if self.deck:
            card = self.deck.pop(0)
            self.hand.append(card)
            return card
        return None

    def show_hand(self):
        print(f"\n{self.name} の手札:")
        for c in self.hand:
            print(f"- {c.card_id}: {c.name} ({c.card_type})")



# --- デッキ作成 ---
def create_deck():
    # カードIDとタイプだけ仮で生成
    deck = []
    for i in range(1, 21):  # 仮に20枚
        card = Card(i, f"カード{i}", "行動")
        deck.append(card)
    random.shuffle(deck)
    return deck

def create_at_deck():
    kinds = ["A", "B", "C"]
    deck = [ATCard(k) for k in kinds for _ in range(2)]  # 合計6枚
    random.shuffle(deck)
    return deck



# --- プレイヤーターン ---
def player_turn(player, opponent, at_deck):
    print(f"\n=== {player.name} のターン ===")
    # デッキから1枚ドロー
    player.draw_card()
    print(f"{player.name} はデッキからカードを1枚ドローしました。")

    # ATデッキから1枚ドロー
    at_card = at_deck.pop(0) if at_deck else None
    if at_card:
        print(f"ATカードをドロー: {at_card.display_name(viewer_disguised=False)}")

    # 手札表示
    player.show_hand()

    # カード使用フェーズ
    used_translation = False
    while True:
        action = input("カード番号を入力して使用 / End で終了: ")
        if action.lower() == "end":
            break

        found = [c for c in player.hand if str(c.card_id) == action]
        if not found:
            print("手札にそのカードはありません。")
            continue

        card = found[0]

        # 翻訳カード効果チェック
        if card.effect == "翻訳":
            if used_translation:
                print("このターンはすでに翻訳を使用済みです。")
                continue
            if at_card:
                at_card.advance_phase()
                print(f"ATカード {at_card.kind} はフェーズ {at_card.phase + 1} に進行しました。")
            used_translation = True

        card.use(player.name, opponent.name)
        player.hand.remove(card)
        player.used_cards.append(card)

    # フェーズ3書き起こし
    if at_card and at_card.phase == 2:
        player.written_AT.add(at_card.kind)
        print(f"{player.name} は ATカード {at_card.kind} を書き起こしました！")

    return at_card

def check_victory(player):
    if {"A","B","C"} <= player.written_AT:
        print(f"\n=== {player.name} が解体新書を完成させました！勝利！ ===")
        return True
    return False

def player_turn(player, opponent, at_deck):
    while True:
        print("\n--- メニュー ---")
        print("1. Action（カードを使用）")
        print("2. Confirmation（カード効果を確認）")
        print("3. End（ターン終了）")

        choice = input("選択してください (1/2/3): ")

        if choice == "1":  # Action
            while True:
                print("\n--- 手札 ---")
                if not player.hand:
                    print("手札がありません。")
                    break

                for idx, card in enumerate(player.hand):
                    print(f"{idx+1}. {card.name}")
                print("b. 戻る")

                act_choice = input("使用するカードを選んでください: ")

                if act_choice.lower() == "b":
                    break  # メニューに戻る
                elif act_choice.isdigit() and 1 <= int(act_choice) <= len(player.hand):
                    card = player.hand[int(act_choice) - 1]
                    confirm = input(f"{card.name} を使用しますか？ (y/n): ")
                    if confirm.lower() == "y":
                        card.use(opponent)  # 効果を発動（Cardクラスに実装済みの想定）
                        player.hand.remove(card)  # 手札から取り除く
                        print(f"{card.name} を使用しました！")
                    else:
                        print(f"{card.name} の使用をキャンセルしました。")
                else:
                    print("無効な入力です。")

        elif choice == "2":  # Confirmation
            while True:
                print("\n--- 手札 ---")
                if not player.hand:
                    print("手札がありません。")
                    break

                for idx, card in enumerate(player.hand):
                    print(f"{idx+1}. {card.name}")
                print("b. 戻る")

                conf_choice = input("確認するカードを選んでください: ")

                if conf_choice.lower() == "b":
                    break
                elif conf_choice.isdigit() and 1 <= int(conf_choice) <= len(player.hand):
                    card = player.hand[int(conf_choice) - 1]
                    print(f"\nカード名: {card.name}")
                    print(f"効果ID: {card.effect_id}")
                    print(f"説明: {card.flavor_text}")
                else:
                    print("無効な入力です。")

        elif choice == "3":  # End
            print(f"{player.name} のターンを終了します。")
            break

        else:
            print("無効な選択です。")

import random

def enemy_turn(enemy, player, at_deck):
    """
    NPC（敵）のターン処理
    """
    print(f"\n--- {enemy.name} のターン ---")

    # 手札がなければターン終了
    if not enemy.hand:
        print(f"{enemy.name} の手札がありません。ターンを終了します。")
        return

    # 行動の候補を選択（例: 50%の確率でカードを使用、50%は何もしない）
    action_choice = random.choice(["use", "skip"])

    if action_choice == "skip":
        print(f"{enemy.name} は様子を見ている…")
        return

    # 手札からランダムにカードを選択
    selected_card = random.choice(enemy.hand)
    print(f"{enemy.name} は {selected_card.name} を使用した！")

    # 行動カード・トラップカードの処理
    if selected_card.card_type == "action":
        # 効果を発動（例: effect.pyにある関数を呼ぶ）
        effect_func = at_deck.get(selected_card.effect_id)
        if effect_func:
            effect_func(selected_card, player)
        else:
            print(f"{selected_card.name} の効果は未実装です。")

        # 使用済みカードは墓地へ
        selected_card.status = "graveyard"
        enemy.hand.remove(selected_card)
        enemy.graveyard.append(selected_card)

    elif selected_card.card_type == "trap":
        # トラップは場に伏せる
        enemy.set_trap(selected_card)
        print(f"{enemy.name} はトラップカードを伏せた。")

    else:
        print(f"{selected_card.name} は不明なカードタイプです。")

    print(f"{enemy.name} のターン終了。")