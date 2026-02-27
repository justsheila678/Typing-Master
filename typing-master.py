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
        word_progress_text.value = f"Progress: Word {current_word_index+1}/{len(selected_words)}"
        page.update()

    #function for word status text, mistakes text, and correct words text
    def change_word_status(e):
        nonlocal correct_words, mistakes
        if word_input.value.lower() == selected_words[current_word_index].lower():
            word_status_text.color = "#04871a"
            word_status_text.value = "Answer Status: Correct!"
            correct_words += 1
            word_progress_text.value = f"Progress: Word {current_word_index+1}/{len(selected_words)}"
            page.update()
        else:
            mistakes += 1
            mistakes_text.value = f"Total Mistakes: {mistakes}"
            word_status_text.color = "#9c0c11"
            word_status_text.value = "Answer Status: Incorrect!"
            page.update()

    #function that will actually affect the variables after the user submits their answer
    def check_word(e):
        nonlocal current_word_index
        change_word_status(e)
        current_word_index += 1
        if current_word_index < len(selected_words):
            change_current_word(e)
        else:
            current_word_text.value = "Game Over! Check Your Results Below."
            word_status_text.color = "#ffffff"
            word_status_text.value = "Answer Status: No words left to evaluate."
            word_progress_text.value = "Progress: All Words Completed!"
            accuracy = (correct_words/len(selected_words))* 100
            accuracy_text.value = f"Final Accuracy: {correct_words}/{len(selected_words)} / {accuracy:.2f}%"
        word_input.value = ""
        page.update()

    #UI Requirements
    current_word_text = ft.Text(value=f"Current Word: {selected_words[current_word_index]}", size=30)
    word_status_text = ft.Text(value="Answer Status: ", size=20)
    mistakes_text = ft.Text(value=f"Total Mistakes: {mistakes}", size=20)
    word_progress_text = ft.Text(value=f"Progress: Word {current_word_index+1}/{len(selected_words)}", size=20)
    word_input = ft.TextField(label="Type Word Here", on_submit=check_word)
    accuracy_text = ft.Text(value="")

    page.add(current_word_text, word_status_text, mistakes_text, word_progress_text, accuracy_text, word_input)

ft.app(target=main)