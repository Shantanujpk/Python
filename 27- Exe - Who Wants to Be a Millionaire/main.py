# Create a progarm Who Wants to Be a Millionaire? 
# use list 
# append amount each time person wins 

# Prerequisits: 
# 1 question : 4 oprions , one correct answer
# if correct answeer loop again with next qiestion, if not the exit loop and print final amount

# Create a program: Who Wants to Be a Millionaire?

# Labels for each question (e.g., First, Second, etc.)
question_string_list = ["First", "Second", "Third", "Fourth", "Fifth"] 

# List of questions
list_of_questions = ["1+1", "Is Python Hard?", "4+4", "Capital of India?", "Sun rises from?"]

# Options for each question (as list of 4 options each)
list_of_options = [
    [2, 4, 65, 8],            # For question 1
    [1, 0, -1, 2],            # For question 2 (0 = No)
    [3, 8, 2, 7],             # For question 3
    ["Delhi", "Mumbai", "Kolkata", "Chennai"],   # For question 4
    ["East", "West", "North", "South"]           # For question 5
]

# Correct answers, must match one of the above options
correct_answers = [2, 0, 8, "Delhi", "East"]

# Prize money corresponding to each correct answer
list_of_Price = [1000, 20000, 300000, 1000000, 5000000]

# Variable to store the final amount won
Final_Price = 0

# Loop through all questions one by one
for i in range(len(list_of_questions)):
    
    # Print which question (e.g., First, Second) and show the question with options
    print(question_string_list[i], "Question Is:", list_of_questions[i], "And your options are:", list_of_options[i])
    
    # Take input from the user
    option = input("Enter your Option: ")
    
    # If the correct answer is of type int, convert input to int before comparing
    if isinstance(correct_answers[i], int):
        option = int(option)
    
    # Check if entered option matches the correct answer
    if option == correct_answers[i]:
        Final_Price = list_of_Price[i]  # Update the prize amount
        print("✅ Correct! You won:", Final_Price)
    else:
        print("❌ Wrong Answer! You won:", Final_Price)
        break  # End game on wrong answer

# After game loop ends
print("🏁 Out of loop")


        

