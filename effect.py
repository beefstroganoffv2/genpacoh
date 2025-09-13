def interference(trap_card, target_card):
    """やり過ぎた玄白：対象の翻訳を1ターン無効にする"""
    target_card.failed = True
    print(f"{target_card.name} の効果は1ターン無効化された！")

def substitute(trap_card, target_card):
    """似過ぎた玄白：相手の場のスロットを5ターン封じる"""
    target_card.block_slot = 5
    print(f"相手の行動カード置き場が5ターン封じられた！")

def translate(action_card, target_atcard):
    target_atcard.phase = +1

def steal(action_card, target_card):
    target_card.status = 3