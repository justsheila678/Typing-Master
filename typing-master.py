import flet as ft
import random as rand

def main(page: ft.Page):
    page.title = "Typing Master"

    words = ["Apocalypse", "Sunsets", "Headphones", "Hoodie", "Moon", "Cycle", "Pecan", "Candle", "Tomato", "Cinnamon", "Bounce", 
             "Medicine", "Crab", "Project", "Voucher", "Wrist", "Fountain", "Manifesting", "Hamper", "Helicopter", "Prosper", "Lebanese", "Wednesday"]
    
    #Variables
    selected_words = rand.sample(words, 15)
    current_word_index = 0
    mistakes = 0
    correct_words = 0

    #function to change the current word text
    def change_current_word(e):
        nonlocal current_word_index
        current_word_text.value = f"Current Word: {selected_words[current_word_index]}"
        word_progress_text.value = f"{correct_words}/{len(selected_words)} Words"
        page.update()

    #function for word status text, mistakes text, and correct words text
    def change_word_status(e):
        nonlocal correct_words, mistakes
        if word_input.value == selected_words[current_word_index]:
            word_status_text.color = "#04871a"
            word_status_text.value = "Answer Status: Correct!"
            correct_words += 1
            word_progress_text.value = f"{correct_words}/{len(selected_words)} Words"
            page.update()
        else:
            mistakes += 1
            mistakes_text.value = f"Total Mistakes: {mistakes}"
            word_status_text.color = "#9c0c11"
            word_status_text.value = "Answer Status: Incorrect!"
            page.update()

    #function that will actually affect the variables after the user submits their answer
    def check_word(e):
        change_word_status(e)
        change_word_status(e)
        current_word_index += 1
        page.update()

    #UI Requirements
    current_word_text = ft.Text(value=f"Current Word: {selected_words[current_word_index]}", size=30)
    word_status_text = ft.Text(value="Answer Status: ", size=20)
    mistakes_text = ft.Text(value=f"Total Mistakes: {mistakes}", size=20)
    word_progress_text = ft.Text(value=f"{correct_words}/{len(selected_words)}", size=20)
    
    word_input = ft.TextField(label="Type Word Here", on_submit=check_word)

    page.add(current_word_text, word_status_text, mistakes_text, word_progress_text, word_input)

ft.app(target=main)