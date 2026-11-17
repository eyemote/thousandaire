# main stages
# ask question
# allow user to take the money and go home
# assess if right
# move up if right, with visual
# if not, go down to next winning amount
import helpers as h
import time
import random

winnings = [0, 100, 250, 500, 750, 1000]
i = 0
current = winnings[i]
END_FLAG = False

questions_100 = [("In which city would you find the Louvre art museum?", ["Paris", "London", "Berlin", "New York City"], "A"),
                 ("How many apostles followed Jesus?",
                  ["9", "10", "11", "12"], "D"),
                 ("What is the name of Ant McPartlin's TV partner?", ["Sep", "Oct", "Nov", "Dec"], "D")]
questions_250 = [("What is the capital of Kenya?", [
                  "Addis Ababa", "Nairobi", "Mombasa", "Juba"], "B"), ("The death of Henry Dashwood opens which author's debut novel Sense and Sensibility?", ["Charles Dickens", "Jane Austen", "Emily Brontë", "Robert Louis Stevenson"], "B")]
questions_500 = [("The Rhythm Heaven video game series inspired which artist's music video for her 2025 song 'Girl Like Me'?", [
                  "Tinashe", "Slayyyter", "PinkPantheress", "Charli XCX"], "C")]
questions_750 = [("George Stubbs' Whistlejacket, a painting which sits in London's National Gallery, is a painting of what animal?", [
                  "Dog", "Cat", "Horse", "Deer"], "C")]
questions_1000 = [("The author of Don Quixote, Miguel de Cervantes, fought at which battle of 1571?", [
                   "Lützen", "Lepanto", "Flodden", "Chaldiran"], "B"),
                  ("")]

# print(questions_100[0][0])

while END_FLAG == False:
    # define correct question set for the level
    rng = random.randint(0, 2)
    question = h.questionSelector(current, rng)
    # --------------------#
    h.questionFormatter(question, winnings[i+1])
    answer = str(input(
        "\nEnter A, B, C or D to answer, or L to leave with the current money.\nAnswer: "))
    if answer.lower() == "l":
        print(f"Congratulations! You go home with £{current}!")
        time.sleep(1)
        print(f"The answer to the question would have been {question[2]}.")
        END_FLAG = True
        break
    correct_flag = h.questionIsRight(question, answer)
    print("...")
    time.sleep(2)
    if correct_flag == True:
        i += 1
        current = winnings[i]
        print(f"That is correct! You are now on £{current}.")
        time.sleep(5)
        if current == winnings[-1]:
            print(
                f"Congratulations! You have won the maximum prize of £{current}!")
            END_FLAG = True
    else:
        print(f"That was incorrect, the answer was {question[2]}.")
        print(f"You go home with £{current}!")
        END_FLAG = True
