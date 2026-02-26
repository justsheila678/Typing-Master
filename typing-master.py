import flet as ft
import random as rand

def main(page: ft.Page):
    page.title = "Typing Master"

    words = ["Apocalypse", "Sunsets", "Headphones", "Hoodie", "Moon", "Cycle", "Pecan", "Candle", "Tomato", "Cinnamon", "Bounce", 
             "Medicine", "Crab", "Project", "Voucher", "Wrist", "Fountain", "Manifesting", "Hamper", "Helicopter", "Prosper", "Lebanese", "Wednesday"]
    
    current_word_text = ft.Text(value="Current Word: ", size=30)
    word_status_text = ft.Text(value="Answer Status: ", size=20)
    mistakes_text = ft.Text(value="Total Mistakes: ", size=20)
    word_progress_text = ft.Text(value="X/Y Words", size=20)
    word_input = ft.TextField(label="Type Word Here", on_submit=None)

    page.add(current_word_text, word_status_text, mistakes_text, word_progress_text, word_input)

ft.app(target=main)