class Player:
    def __init__(self, name):
        self.name = name
        self.deck = []
        self.hand = []
        self.field = []
        self.trap_zone = []   # 伏せカード
        self.graveyard = []
        self.block_turns = 0  # 行動カード置き場のブロック残りターン数

    def can_play_action(self):
        """行動カードを出せるかどうか"""
        return self.block_turns == 0

    def end_turn(self):
        """ターン終了時に状態を更新"""
        if self.block_turns > 0:
            self.block_turns -= 1