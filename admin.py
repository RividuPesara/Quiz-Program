import json,textwrap

def input_int(prompt, max_value):     # Continuously prompts user for an integer input until a valid one is provided withen the range
    while True:
        try:
            num=int(input(prompt))
            if 1<=num<=max_value:
                return num
        except ValueError:
            continue

def input_something(prompt):     # Continuously prompts user for am input
    while True:
        parah=input(prompt).strip()
        if parah:
            return parah
        else:
            continue

def save_data(data):      # Saves the provided data to 'data.txt' in JSON format
    file=open('data.txt','w')
    json.dump(data,file,indent=4)
    file.close()

# Truncates the question text to fit within a 50 character limit
def truncate():  
    question = value["question"]
    shorten_question = textwrap.shorten(question, width=50, placeholder="...")
    print(f"{index+1}. {shorten_question}")

# Load existing data from 'data.txt' if it exists else  create an empty list
try:
    file=open('safasf.txt','r')
    data=json.load(file)
    file.close()
except(FileNotFoundError,json.JSONDecodeError):
    data=[]

print('Welcome to the Quiz Admin Program.')
correct=0
incorrect=0
while True:
    
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete, [b]reakdown or [q]uit.')
    choice = input('> ').lower()
    
    if choice == 'a':         # Add a new question
        question=input_something("Enter the question: ")
        answer_list=[]
        while True:
            answer=input_something('Enter a valid answer (enter "q" when done): ')
            if answer.lower()!='q':
                answer_list.append(answer.lower())
            elif answer_list and answer.lower()=='q':
                break
        difficulty=input_int("Enter question difficulty (1-3): ",3)

        question_add={
            "question": question,
            "answers": answer_list,
            "difficulty": difficulty,
            "correct": correct,
            "incorrect": incorrect
        }
        data.append(question_add)
        save_data(data)
    
    elif choice == 'l':         # List all questions
        print("Current questions: ")
        if not(data):
            print("No questions saved")
        else:
            for index,value in enumerate(data):
                truncate()
    elif choice == 's':         # Search for questions containing a specific word
        found=False
        if not data:
            print("No questions saved")
        else:
            search_term=input_something("Enter a search term: ")
            for index,value in enumerate(data):
                if search_term.lower() in value["question"]:
                    truncate()
                    found=True
            if not found:
                print("No results found")

    elif choice == 'v':         # View details of a specific question
        if not data:
            print("No questions saved")
        else:
            index_num=input_int("Question number to view: ",len(data))
            print(f"\n\nQuestion:\n  {data[index_num-1]["question"]}\n")
            answer_string=', '.join(data[index_num-1]["answers"])

            if len(data[index_num-1]["answers"])==1:
                print(f"Correct Answers:{answer_string}")
            else:
                print(f"Valid Answers:{answer_string}")

            if data[index_num-1]["difficulty"]==1:
                print(f"Difficulty:{data[index_num-1]["difficulty"]} [Easy]")
            elif data[index_num-1]["difficulty"]==2:
                print(f"Difficulty:{data[index_num-1]["difficulty"]} [Medium]")
            else:
                print(f"Difficulty:{data[index_num-1]["difficulty"]} [Hard]")
                
            total_answers=data[index_num-1]["correct"]+data[index_num-1]["incorrect"]

            print(f"Correctly answered {data[index_num-1]["correct"]} time(s)")
            print(f"Incorrectly answered {data[index_num-1]["incorrect"]} times(s)")

            if data[index_num-1]["correct"] and data[index_num-1]["incorrect"] !=0:
                percentage_correct = (data[index_num-1]["correct"] / total_answers) * 100
                percentage_incorrect=(data[index_num-1]["incorrect"] / total_answers) * 100
                print("Percentage of correct answers:", round(percentage_correct, 2), "%")  
                print("Percentage of incorrect answers:", round(percentage_incorrect, 2), "%")

    elif choice == 'd':         # Delete a specific question
        if not data:
            print("No questions saved")
        else:
            del_num=input_int("Question number to delete: ",len(data))
            data.pop(del_num-1)
            save_data(data)
            print("Question deleted")
            
    elif choice == 'q':         # Quit the program
        print("Goodbye!")
        break
        
    elif choice=='b':         # Display questions by difficulty
        count_difficulty_1 = 0
        count_difficulty_2 = 0
        count_difficulty_3 = 0
        for item in data:
            difficulty = item["difficulty"]
            if difficulty == 1:
                count_difficulty_1 += 1
            elif difficulty == 2:
                count_difficulty_2 += 1
            elif difficulty == 3:
                count_difficulty_3 += 1
        print("Number of questions with difficulty 1:", count_difficulty_1)
        print("Number of questions with difficulty 2:", count_difficulty_2)
        print("Number of questions with difficulty 3:", count_difficulty_3)


    else: 
        print("Invalid choice")
         



# If you have been paid to write this program, please delete this comment.
