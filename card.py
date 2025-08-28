from typing import Callable

class Card:
  class Card:
    def __init__(self, card_id: int, name: str, card_type: str, effect: Callable = None, genpaku: int = 0):
        """
        :param card_id: 固有番号
        :param name: カードの名前
        :param card_type: "action", "trap" など
        :param effect: 発動効果
        :param genpaku: 1なら玄白カード扱い
        """
        # 初期状態
        self.card_id = card_id
        self.name = name
        self.card_type = card_type
        self.effect = effect
        self.genpaku = genpaku  # 0 or 1
        self.status = "deck"    # deck, hand, field, graveyard
        self.unique_mark = False   # デッキ内で使用済みかどうか
        self.failed = False        # トラップ等で効果無効化されたか
        self.disrupted = False      # 今ターン妨害されているか
        self.disrupted_turns = 0    # 妨害が何ターン続くか（例：1なら1ターンのみ無効）




    def set_trap(self):
        """トラップカードを伏せ表示"""
        if self.card_type == "trap":
            self.status = "set_trap"

    def activate_trap(self, target, effect_func):
        """トラップ発動処理"""
        if self.status == "set_trap":
            print(f"トラップ発動！ {self.name}")
            effect_func(self, target)
            self.status = "graveyard"   

    def use(self):
        """
        カードを使用する
        :param target: 効果の対象 (プレイヤーや相手など)
        """
        while True:
    confirm = input(f"{self.name} を使用しますか？ (y/n): ").lower()

    if confirm == "y":
        print(f"{self.name} を使用しました！")
        # ここにカード効果の処理
        if self.card_type == "trap" and self.status == "deck":
                    self.set_trap(self)
                    print(f"{self.name}を仕掛けた！")

                if self.card_type == "trap" and self.status == "myhand":
                    self.activate_trap(self)


                if self.failed:
                    print(f"{self.name} の効果はトラップで無効化された！")
                    self.move_to_graveyard()
                    return

  

                if self.remain_on_field:
                    self.status = "field"
                    print(f"{self.name} は場に残った。")
                else:
                    self.move_to_graveyard()
                break  # ループ終了

    elif confirm == "n":
        print(f"{self.name} の使用をキャンセルしました。")
        break  # ループ終了

    else:
        print("y または n を入力してください。")
 


                

        if confim.lower() == "n":
            print(f"{self.name} の使用をキャンセルしました。")

    def move_to_graveyard(self):
        """墓地へ送る"""
        self.status = "graveyard"
        print(f"{self.name} は墓地に送られた。")

    def default_effect(self, target=None):
        """効果が未定義の場合"""
        print(f"{self.name} は効果を発揮しなかった。")

    def __repr__(self):
        return f"[{self.card_id}] {self.name} ({self.status})"
    

    



# genpaku_card = Card(
#     card_id=,                 # No.
#     name="",            # カード名
#     effect_id="",     # 効果（effect.pyにある"translate"関数に対応）
#     flavor_text="",  # フレーバーテキスト
#     card_type="",        # カードタイプ（行動）
#     is_genpaku=           # 玄白カードか否か（正 → True）
# )




genpaku_card = Card(
    card_id=1,                 # No.
    name="杉田玄白",            # カード名
    effect_id="translate",     # 効果（effect.pyにある"translate"関数に対応）
    flavor_text="解体新書の編纂者、翻訳の第一人者。",  # フレーバーテキスト
    card_type="action",        # カードタイプ（行動）
    is_genpaku=True            # 玄白カードか否か（正 → True）
)

genpaku_card = Card(
    card_id=2,                 # No.
    name="スリの玄白",            # カード名
    effect_id="steal",     # 効果（effect.pyにある"translate"関数に対応）
    flavor_text="",  # フレーバーテキスト
    card_type="",        # カードタイプ（行動）
    is_genpaku= True          # 玄白カードか否か（正 → True）
)

genpaku_card = Card(
    card_id=3,                 # No.
    name="やり過ぎた玄白",            # カード名
    effect_id="interference",     # 効果（effect.pyにある"translate"関数に対応）
    flavor_text="",  # フレーバーテキスト
    card_type="action",        # カードタイプ（行動）
    is_genpaku= True          # 玄白カードか否か（正 → True）
)

genpaku_card = Card(
    card_id=4,                 # No.
    name="抑止玄白",            # カード名
    effect_id="suppression",     # 効果（effect.pyにある"translate"関数に対応）
    flavor_text="",  # フレーバーテキスト
    card_type="",        # カードタイプ（行動）
    is_genpaku=  True         # 玄白カードか否か（正 → True）
)

genpaku_card = Card(
    card_id=5,                 # No.
    name="初代玄白",            # カード名
    effect_id="translate",     # 効果（effect.pyにある"translate"関数に対応）
    flavor_text="",  # フレーバーテキスト
    card_type="",        # カードタイプ（行動）
    is_genpaku=  True         # 玄白カードか否か（正 → True）
)

genpaku_card = Card(
    card_id=6,                 # No.
    name="杉田翻訳",            # カード名
    effect_id="translatev2",     # 効果（effect.pyにある"translate"関数に対応）
    flavor_text="",  # フレーバーテキスト
    card_type="",        # カードタイプ（行動）
    is_genpaku=  True         # 玄白カードか否か（正 → True）
)

genpaku_card = Card(
    card_id=7,                 # No.
    name="無知田玄白",            # カード名
    effect_id="Ignorance",     # 効果（effect.pyにある"translate"関数に対応）
    flavor_text="",  # フレーバーテキスト
    card_type="",        # カードタイプ（行動）
    is_genpaku=  True         # 玄白カードか否か（正 → True）
)

genpaku_card = Card(
    card_id=8,                 # No.
    name="玄白の銅像",            # カード名
    effect_id="",     # 効果（effect.pyにある"translate"関数に対応）
    flavor_text="",  # フレーバーテキスト
    card_type="",        # カードタイプ（行動）
    is_genpaku=   False        # 玄白カードか否か（正 → True）
)

genpaku_card = Card(
    card_id=9,                 # No.
    name="甘え過ぎた玄白",            # カード名
    effect_id="",     # 効果（effect.pyにある"translate"関数に対応）
    flavor_text="",  # フレーバーテキスト
    card_type="",        # カードタイプ（行動）
    is_genpaku=  True         # 玄白カードか否か（正 → True）
)

genpaku_card = Card(
    card_id=10,                 # No.
    name="早過ぎた玄白",            # カード名
    effect_id="",     # 効果（effect.pyにある"translate"関数に対応）
    flavor_text="",  # フレーバーテキスト
    card_type="",        # カードタイプ（行動）
    is_genpaku=  True         # 玄白カードか否か（正 → True）
)

genpaku_card = Card(
    card_id=11,                 # No.
    name="杉田玄白(幼少期)",            # カード名
    effect_id="",     # 効果（effect.pyにある"translate"関数に対応）
    flavor_text="",  # フレーバーテキスト
    card_type="",        # カードタイプ（行動）
    is_genpaku=  False        # 玄白カードか否か（正 → True）
)

genpaku_card = Card(
    card_id=12,                 # No.
    name="杉田玄白の母",            # カード名
    effect_id="",     # 効果（effect.pyにある"translate"関数に対応）
    flavor_text="",  # フレーバーテキスト
    card_type="",        # カードタイプ（行動）
    is_genpaku=  False         # 玄白カードか否か（正 → True）
)

genpaku_card = Card(
    card_id=13,                 # No.
    name="杉田玄白の父",            # カード名
    effect_id="",     # 効果（effect.pyにある"translate"関数に対応）
    flavor_text="",  # フレーバーテキスト
    card_type="",        # カードタイプ（行動）
    is_genpaku=    False       # 玄白カードか否か（正 → True）
)

genpaku_card = Card(
    card_id=14,                 # No.
    name="ヌキた淫パク",            # カード名
    effect_id="",     # 効果（effect.pyにある"translate"関数に対応）
    flavor_text="",  # フレーバーテキスト
    card_type="",        # カードタイプ（行動）
    is_genpaku=   False        # 玄白カードか否か（正 → True）
)

genpaku_card = Card(
    card_id=15,                 # No.
    name="勃ったたんぱく",            # カード名
    effect_id="",     # 効果（effect.pyにある"translate"関数に対応）
    flavor_text="",  # フレーバーテキスト
    card_type="",        # カードタイプ（行動）
    is_genpaku=    False       # 玄白カードか否か（正 → True）
)

genpaku_card = Card(
    card_id=16,                 # No.
    name="似過ぎた玄白",            # カード名
    effect_id="substitute",     # 効果（effect.pyにある"translate"関数に対応）
    flavor_text="",  # フレーバーテキスト
    card_type="trap",        # カードタイプ（行動）
    is_genpaku=  False         # 玄白カードか否か（正 → True）
)