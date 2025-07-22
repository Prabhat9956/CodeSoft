import tkinter as tk
from tkinter import messagebox
import random

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Cool Blue Rock Paper Scissors 🎮")
        self.root.geometry("600x520")
        self.root.configure(bg="#1A2B3C")
        self.root.resizable(False, False)

        self.choices = ['Rock', 'Paper', 'Scissors']
        self.icons = {'Rock': '🪨', 'Paper': '📄', 'Scissors': '✂️'}

        self.user_score = 0
        self.computer_score = 0
        self.round = 1
        self.total_rounds = 5
        self.game_active = True

        self.build_ui()

    def build_ui(self):
        tk.Label(
            self.root,
            text="Rock • Paper • Scissors",
            font=('Segoe UI', 24, 'bold'),
            bg="#1A2B3C",
            fg="#00E0FF"
        ).pack(pady=20)

        self.round_label = tk.Label(
            self.root,
            text=f"Round {self.round}/{self.total_rounds}",
            font=('Segoe UI', 14, 'bold'),
            bg="#1A2B3C",
            fg="#E0E0E0"
        )
        self.round_label.pack()

        btn_frame = tk.Frame(self.root, bg="#1A2B3C")
        btn_frame.pack(pady=25)

        self.buttons = {}
        colors = {'Rock': '#1ABC9C', 'Paper': '#3498DB', 'Scissors': '#9B59B6'}

        for idx, choice in enumerate(self.choices):
            btn = tk.Button(
                btn_frame,
                text=f"{self.icons[choice]}\n{choice}",
                font=('Segoe UI', 14, 'bold'),
                width=10,
                height=3,
                bg=colors[choice],
                fg="white",
                bd=0,
                activebackground="#00E0FF",
                command=lambda c=choice: self.play_round(c),
                cursor="hand2"
            )
            btn.grid(row=0, column=idx, padx=15)
            self.buttons[choice] = btn

        self.result_text = tk.Label(
            self.root,
            text="",
            font=('Segoe UI', 18, 'bold'),
            bg="#1A2B3C",
            fg="#00FFB0"
        )
        self.result_text.pack(pady=20)

        self.user_choice_label = tk.Label(
            self.root,
            text="You: ",
            font=('Segoe UI', 13),
            bg="#1A2B3C",
            fg="#FFFFFF"
        )
        self.user_choice_label.pack()

        self.computer_choice_label = tk.Label(
            self.root,
            text="Computer: ",
            font=('Segoe UI', 13),
            bg="#1A2B3C",
            fg="#FFFFFF"
        )
        self.computer_choice_label.pack()

        self.score_label = tk.Label(
            self.root,
            text="Score - You: 0 | Computer: 0",
            font=('Segoe UI', 13, 'bold'),
            bg="#1A2B3C",
            fg="#FFD700"
        )
        self.score_label.pack(pady=15)

        self.reset_btn = tk.Button(
            self.root,
            text="🔁 Restart Game",
            font=('Segoe UI', 12, 'bold'),
            bg="#34495E",
            fg="white",
            command=self.reset_game,
            width=20,
            height=2,
            bd=0,
            activebackground="#00E0FF",
            cursor="hand2"
        )
        self.reset_btn.pack(pady=10)

    def play_round(self, user_choice):
        if not self.game_active:
            return

        self.disable_buttons()
        comp_choice = random.choice(self.choices)
        result = self.get_result(user_choice, comp_choice)

        self.user_choice_label.config(text=f"You: {self.icons[user_choice]} {user_choice}")
        self.computer_choice_label.config(text=f"Computer: {self.icons[comp_choice]} {comp_choice}")
        self.result_text.config(text=result)

        if result == "You Win!":
            self.user_score += 1
        elif result == "You Lose!":
            self.computer_score += 1

        self.score_label.config(
            text=f"Score - You: {self.user_score} | Computer: {self.computer_score}"
        )

        self.round += 1
        self.update_round()
        self.root.after(1500, self.check_game_over)

    def get_result(self, user, comp):
        if user == comp:
            return "It's a Tie!"
        elif (user == 'Rock' and comp == 'Scissors') or \
             (user == 'Scissors' and comp == 'Paper') or \
             (user == 'Paper' and comp == 'Rock'):
            return "You Win!"
        else:
            return "You Lose!"

    def update_round(self):
        if self.round <= self.total_rounds:
            self.round_label.config(text=f"Round {self.round}/{self.total_rounds}")
        else:
            self.round_label.config(text="Final Round!")

    def check_game_over(self):
        if self.round > self.total_rounds:
            self.game_active = False
            if self.user_score > self.computer_score:
                final = "🎉 You Won the Match!"
            elif self.user_score < self.computer_score:
                final = "😞 You Lost the Match!"
            else:
                final = "🤝 It's a Draw!"

            messagebox.showinfo("Game Over", f"{final}\nFinal Score:\nYou: {self.user_score} | Computer: {self.computer_score}")
        else:
            self.enable_buttons()

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.round = 1
        self.game_active = True

        self.user_choice_label.config(text="You: ")
        self.computer_choice_label.config(text="Computer: ")
        self.result_text.config(text="")
        self.score_label.config(text="Score - You: 0 | Computer: 0")
        self.round_label.config(text=f"Round {self.round}/{self.total_rounds}")
        self.enable_buttons()

    def disable_buttons(self):
        for btn in self.buttons.values():
            btn.config(state='disabled')

    def enable_buttons(self):
        for btn in self.buttons.values():
            btn.config(state='normal')

# Launch the game
root = tk.Tk()
game = RPSGame(root)
root.mainloop()
