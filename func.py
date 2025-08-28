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