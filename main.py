import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.player = "X"  # X always starts first
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_grid()

    def create_grid(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 40), height=2, width=5, 
                                   command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
        self.reset_button = tk.Button(self.root, text="Reset", font=("Arial", 20), command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3)

    def on_click(self, row, col):
        if self.buttons[row][col]["text"] == "" and self.check_winner() is False:
            self.buttons[row][col]["text"] = self.player
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.player} wins!")
            elif self.check_draw():
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            else:
                self.player = "O" if self.player == "X" else "X"

    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True
        return False

    def check_draw(self):
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]["text"] == "":
                    return False
        return True

    def reset_game(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = ""
        self.player = "X"

# Set up the window
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
