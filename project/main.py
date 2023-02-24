import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class kpoGUI:

    def __init__(self, master):
        self.master = master
        self.master.title("Kő, Papír, Olló")
        self.master.minsize(400, 300)

        # Label az instrukciókhoz.
        instructions_label = ttk.Label(master, text="Válasszon egyet!:")
        instructions_label.pack(pady=10)

        # Radio button-ök létrehozása a játékos lépésének kiválasztásához!
        self.player_choice_var = tk.StringVar(value="Kő")
        player_choice_frame = ttk.Frame(master)
        player_choice_frame.pack(pady=10)
        ko_button = ttk.Radiobutton(player_choice_frame, text="Kő", variable=self.player_choice_var, value="kő")
        papir_button = ttk.Radiobutton(player_choice_frame, text="Papír", variable=self.player_choice_var, value="papír")
        ollo_button = ttk.Radiobutton(player_choice_frame, text="Olló", variable=self.player_choice_var, value="olló")
        ko_button.pack(side="left")
        papir_button.pack(side="left", padx=10)
        ollo_button.pack(side="left")

        # Játék gomb léthrehozása
        play_button = ttk.Button(master, text="Játék", command=self.play_game)
        play_button.pack(pady=10)

        # Win streak label létrehozása
        self.result_label = ttk.Label(master, text="")
        self.result_label.pack(pady=10)
        self.win_streak = 0
        self.win_streak_label = ttk.Label(master, text=f"Win streak: {self.win_streak}")
        self.win_streak_label.pack(pady=10)

        # Játék leírás label létrehozása
        description_button = ttk.Button(master, text="Játék leírás!", command=self.show_game_description)
        description_button.pack(pady=10)

    def play_game(self):
        player_choice = self.player_choice_var.get()

        # Játékos választásának meghatározása
        player_choice_letter = ""
        if player_choice == "kő":
            player_choice_letter = "k"
        elif player_choice == "papír":
            player_choice_letter = "p"
        elif player_choice == "olló":
            player_choice_letter = "o"

        # Random szám generálás a számítógépnek
        computer_choice_letter = random.choice(['k', 'p', 'o'])

        # Játék kimenetélen megállapítása
        if player_choice_letter == computer_choice_letter:
            result_text = "Döntetlen"
            self.win_streak = 0
        elif (player_choice_letter == 'k' and computer_choice_letter == 'o') or \
             (player_choice_letter == 'p' and computer_choice_letter == 'k') or \
             (player_choice_letter == 'o' and computer_choice_letter == 'p'):
            result_text = "Gratulálok! Nyertél!"
            self.win_streak += 1
        else:
            result_text = "A számítógép nyert!"
            self.win_streak = 0

        # Label frissitése a nyert/nem nyert játékok után!
        self.result_label.config(text=f"A számítógép választása: {computer_choice_letter}. {result_text}")
        self.win_streak_label.config(text=f"Win streak: {self.win_streak}")

    # Játék leírás meghatározása
    def show_game_description(self):
        message = "Nem hinném, hogy kéne ide leírás.."
        messagebox.showinfo("Game desc.", message)


root = tk.Tk()
rps = kpoGUI(root)
root.mainloop()