import tkinter as tk
import random
from tkinter import messagebox

# Snakes and Ladders
SNAKES = {99: 54, 70: 55, 52: 42, 25: 2, 95: 72}
LADDERS = {6: 25, 11: 40, 60: 85, 46: 90, 17: 69}
WINNING_POSITION = 100
CELL_SIZE = 60


class Player:
    def __init__(self, name, color):
        self.name = name
        self.position = 0
        self.color = color
        self.token = None


class SnakeLadderGame:
    def __init__(self, root, num_players):
        self.root = root
        self.root.title("Snake & Ladder Game")

        self.canvas = tk.Canvas(root, width=600, height=600)
        self.canvas.pack()

        self.players = []
        colors = ["red", "blue", "green", "purple"]

        for i in range(num_players):
            name = f"Player {i+1}"
            self.players.append(Player(name, colors[i]))

        self.current_player_index = 0

        self.draw_board()
        self.draw_snakes_and_ladders()  # Draw visuals
        self.create_tokens()

        self.roll_button = tk.Button(root, text="Roll Dice 🎲", command=self.roll_dice)
        self.roll_button.pack(pady=10)

        self.status_label = tk.Label(root, text="Player 1's Turn")
        self.status_label.pack()

    # ---------------- BOARD ----------------

    def draw_board(self):
        for row in range(10):
            for col in range(10):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                color = "#f0d9b5" if (row + col) % 2 == 0 else "#b58863"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

                cell_number = self.get_cell_number(row, col)
                self.canvas.create_text(
                    x1 + 5, y1 + 5,
                    text=str(cell_number),
                    anchor="nw",
                    font=("Arial", 8)
                )

    def get_cell_number(self, row, col):
        row_from_bottom = 9 - row
        if row_from_bottom % 2 == 0:
            return row_from_bottom * 10 + col + 1
        else:
            return row_from_bottom * 10 + (10 - col)

    # ---------------- DRAW SNAKES & LADDERS ----------------

    def draw_snakes_and_ladders(self):

        # 🟢 Draw Ladders
        for start, end in LADDERS.items():
            x1, y1 = self.get_coordinates(start)
            x2, y2 = self.get_coordinates(end)

            # Move to center of cells
            x1 += CELL_SIZE // 2
            y1 += CELL_SIZE // 2
            x2 += CELL_SIZE // 2
            y2 += CELL_SIZE // 2

            offset = 8  # distance between ladder rails

            # Ladder rails
            self.canvas.create_line(x1-offset, y1-offset, x2-offset, y2-offset,
                                    width=6, fill="green")

            self.canvas.create_line(x1+offset, y1+offset, x2+offset, y2+offset,
                                    width=6, fill="green")

            # Ladder steps
            steps = 6
            for i in range(1, steps):
                t = i / steps
                sx = x1 + (x2 - x1) * t
                sy = y1 + (y2 - y1) * t

                self.canvas.create_line(
                    sx-offset, sy-offset,
                    sx+offset, sy+offset,
                    width=4,
                    fill="darkgreen"
                )

        # 🔴 Draw Snakes
        for start, end in SNAKES.items():
            x1, y1 = self.get_coordinates(start)
            x2, y2 = self.get_coordinates(end)

            x1 += CELL_SIZE // 2
            y1 += CELL_SIZE // 2
            x2 += CELL_SIZE // 2
            y2 += CELL_SIZE // 2

            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2 - 40  # curve height

            self.canvas.create_line(
                x1, y1,
                mid_x, mid_y,
                x2, y2,
                smooth=True,
                width=8,
                fill="red"
            )

            # Snake head
            self.canvas.create_oval(
                x1-8, y1-8, x1+8, y1+8,
                fill="darkred", outline=""
            )

            # Snake tail
            self.canvas.create_oval(
                x2-6, y2-6, x2+6, y2+6,
                fill="red", outline=""
            )

    # ---------------- TOKENS ----------------

    def create_tokens(self):
        for player in self.players:
            x, y = self.get_coordinates(1)
            player.token = self.canvas.create_oval(
                x+20, y+20, x+40, y+40,
                fill=player.color
            )

    def get_coordinates(self, position):
        if position == 0:
            position = 1

        row = (position - 1) // 10
        col = (position - 1) % 10

        if row % 2 == 1:
            col = 9 - col

        x = col * CELL_SIZE
        y = (9 - row) * CELL_SIZE
        return x, y

    # ---------------- GAME LOGIC ----------------

    def roll_dice(self):
        player = self.players[self.current_player_index]
        dice = random.randint(1, 6)

        messagebox.showinfo("Dice Roll", f"{player.name} rolled {dice}")

        if player.position + dice <= WINNING_POSITION:
            player.position += dice

            if player.position in LADDERS:
                messagebox.showinfo("Ladder!", f"{player.name} climbed a ladder!")
                player.position = LADDERS[player.position]

            elif player.position in SNAKES:
                messagebox.showinfo("Snake!", f"{player.name} got bitten!")
                player.position = SNAKES[player.position]

            x, y = self.get_coordinates(player.position)
            self.canvas.coords(player.token, x+20, y+20, x+40, y+40)

        if player.position == WINNING_POSITION:
            messagebox.showinfo("Winner", f"{player.name} Wins!")
            self.roll_button.config(state="disabled")
            return

        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.status_label.config(text=f"{self.players[self.current_player_index].name}'s Turn")


# ---------------- RUN GAME ----------------

if __name__ == "__main__":
    root = tk.Tk()
    num_players = int(input("Enter number of players (2-4): "))
    game = SnakeLadderGame(root, num_players)
    root.mainloop()