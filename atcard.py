class ATCard:
    def __init__(self, kind: str):
        """
        kind: 本物の種類 ('A','B','C'など)
        """
        self.kind = kind          # 本物の種類
        self.phase = 0            # 0=未翻訳, 1=翻訳済, 2=理解済, 3=書き起こし済
        self.turn_counter = None  # 2フェーズ後の書き起こし用カウンター
        self.disguise_active = False
        self.fake_kind = None
        self.turns_left = 0       # 偽装残ターン数
        self.name = "ATカード"

    # --- フェーズ進行 ---
    def progress_phase(self, card, player_name):
        """
        card: 使用カード（翻訳や玄白カードなど）
        player_name: 使用者
        """
        # 翻訳カード
        if card.has_translate:
            if self.phase == 0:
                self.phase = 1
                print(f"{player_name} は {self.display_name()} を翻訳！(フェーズ1完了)")
            elif self.phase == 1:
                self.phase = 2
                self.turn_counter = 0
                print(f"{player_name} は {self.display_name()} を理解！(フェーズ2完了)")
            elif self.phase == 2:
                if card.genpaku == 1:
                    self.phase = 3
                    print(f"{player_name} は {self.display_name()} を書き起こした！(フェーズ3完了)")
                else:
                    print("このカードでは書き起こしできません。")
            else:
                print("ATカードはすでに完成しています。")
        
        # 翻訳なし玄白カード
        elif card.genpaku == 1:
            if self.phase == 2 and self.turn_counter is not None and self.turn_counter <= 2:
                self.phase = 3
                print(f"{player_name} は {self.display_name()} を書き起こした！（玄白カード効果）")
            else:
                print("書き起こし条件を満たしていません。")
        else:
            print("このカードではATカードを進められません。")

    # --- 偽装関連 ---
    def apply_disguise(self, fake_kind: str):
        self.disguise_active = True
        self.fake_kind = fake_kind
        self.turns_left = 3
        print(f"ATカードが偽装されました！偽装種類: {self.fake_kind}")

    def decrement_disguise(self):
        if self.disguise_active:
            self.turns_left -= 1
            if self.turns_left <= 0:
                self.disguise_active = False
                self.fake_kind = None
                print("偽装解除、本物の種類が表示されます！")

    def force_reveal(self):
        self.disguise_active = False
        self.fake_kind = None
        self.turns_left = 0
        print("精査によりATカードの本物の種類が強制表示！")

    # --- 表示 ---
    def display_name(self, viewer_disguised=False):
        # フェーズ1前は種類非表示
        if self.phase == 0:
            return self.name
        # 偽装中で対象プレイヤーにのみ偽装表示
        if viewer_disguised and self.disguise_active:
            return f"ATカード（{self.fake_kind}）"
        return f"ATカード（{self.kind}）"

    # --- ターン経過処理 ---
    def next_turn(self):
        if self.turn_counter is not None:
            self.turn_counter += 1
        self.decrement_disguise()


        