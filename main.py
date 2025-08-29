import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup


class TicTacToe(GridLayout):
    def __init__(self, player_symbol="X", **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.player_symbol = player_symbol
        self.computer_symbol = "O" if player_symbol == "X" else "X"
        self.board = [""] * 9

        # إنشاء الأزرار
        self.buttons = []
        for i in range(9):
            btn = Button(
                text="",
                font_size=40,
                background_color=(0.2, 0.6, 0.8, 1),  # أزرار ملونة
                color=(1, 1, 1, 1)  # خط أبيض
            )
            btn.bind(on_press=self.make_move)
            self.add_widget(btn)
            self.buttons.append(btn)

    def make_move(self, instance):
        idx = self.buttons.index(instance)

        if self.board[idx] == "":
            # حركة اللاعب
            self.board[idx] = self.player_symbol
            instance.text = self.player_symbol
            if self.check_winner(self.player_symbol):
                self.show_popup("You Win! 🎉")
                return
            if "" not in self.board:
                self.show_popup("Draw 🤝")
                return

            # حركة الكمبيوتر (عشوائية)
            self.computer_move()

    def computer_move(self):
        empty_cells = [i for i, x in enumerate(self.board) if x == ""]
        if empty_cells:
            idx = random.choice(empty_cells)
            self.board[idx] = self.computer_symbol
            self.buttons[idx].text = self.computer_symbol

            if self.check_winner(self.computer_symbol):
                self.show_popup("Computer Wins 🤖")
            elif "" not in self.board:
                self.show_popup("Draw 🤝")

    def check_winner(self, symbol):
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # صفوف
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # أعمدة
            [0, 4, 8], [2, 4, 6]              # أقطار
        ]
        return any(all(self.board[i] == symbol for i in pattern) for pattern in win_patterns)

    def show_popup(self, message):
        content = BoxLayout(orientation="vertical", padding=10, spacing=10)
        content.add_widget(Label(text=message, font_size=24, color=(0,0,0,1)))
        restart_btn = Button(text="Play Again", size_hint=(1, 0.5), background_color=(0.8, 0.2, 0.2, 1))
        content.add_widget(restart_btn)

        popup = Popup(title="Game Over", content=content, size_hint=(0.7, 0.5))
        restart_btn.bind(on_press=lambda *args: (popup.dismiss(), self.reset_game()))
        popup.open()

    def reset_game(self):
        self.board = [""] * 9
        for btn in self.buttons:
            btn.text = ""


class TicTacToeApp(App):
    def build(self):
        return TicTacToe(player_symbol="X")  # يمكن تغييره لـ "O"


if __name__ == "__main__":
    TicTacToeApp().run()
