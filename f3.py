#3.TYPING MASTER

import time
import difflib

def typing_master():
    text_to_type = (
        "The quick brown fox jumps over the lazy dog. "
        "Typing tests are a great way to improve your typing skills and accuracy. "
        "Let's see how well you can type this text!"
    )
    
    print("Welcome to Typing Master!")
    print("Your challenge is to type the following text as accurately and quickly as possible:")
    print("\n" + text_to_type + "\n")
    
    input("Press Enter when you are ready to start...")
    
    start_time = time.time()
    user_input = input("\nStart typing: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    elapsed_time_str = f"{elapsed_time:.2f} seconds"
    
    accuracy = difflib.SequenceMatcher(None, text_to_type, user_input).ratio()
    accuracy_percentage = f"{accuracy * 100:.2f}%"
    
    print("\nTyping Complete!")
    print(f"Time taken: {elapsed_time_str}")
    print(f"Accuracy: {accuracy_percentage}")
    
    if accuracy == 1.0:
        print("Perfect typing! Well done!")
    elif accuracy >= 0.8:
        print("Great job! A little more practice and you'll be perfect!")
    else:
        print("Keep practicing to improve your typing accuracy!")

if __name__ == "__main__":
    typing_master()
