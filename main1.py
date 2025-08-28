from func import draw_card

# --- 初期設定 ---
yourpoint = 0
enemypoint = 0
yourdeck = list(range(1, 31))
enemydeck = list(range(1, 31))
yourused_cards = []
enemyused_cards = []
yourhand = []
enemyhand = []

# --- 互いに5枚ずつドロー ---
yourdeck, yourhand, yourused_cards = draw_card(yourdeck, yourhand, yourused_cards, num=5)
enemydeck, enemyhand, enemyused_cards = draw_card(enemydeck, enemyhand, enemyused_cards, num=5)

# --- 結果表示 ---
print("あなたの手札:", yourhand)
print("相手の手札:", enemyhand)
print("残りデッキ枚数 あなた:", len(yourdeck), " 相手:", len(enemydeck))
print("使用済みカード あなた:", yourused_cards)
print("使用済みカード 相手:", enemyused_cards)