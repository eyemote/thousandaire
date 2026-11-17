import helpers as h
import time
import random

winnings = [0, 100, 250, 500, 750, 1000]
i = 0
current = winnings[i]
END_FLAG = False

# ---- QUESTIONS ----
questions_100 = [("In which city would you find the Louvre art museum?", ["Paris", "London", "Berlin", "New York City"], "A"),
                 ("How many apostles followed Jesus?",
                  ["9", "10", "11", "12"], "D"),
                 ("What is the name of Ant McPartlin's TV partner?", ["Sep", "Oct", "Nov", "Dec"], "D")]
questions_250 = [("What is the capital of Kenya?", [
                  "Addis Ababa", "Nairobi", "Mombasa", "Juba"], "B"),
                 ("The death of Henry Dashwood opens which author's debut novel Sense and Sensibility?", [
                  "Charles Dickens", "Jane Austen", "Emily Brontë", "Robert Louis Stevenson"], "B"),
                 ("Which ingredient is used in BOTH tiramisu and affogato?", ["Coffee", "Ice cream", "Cinnamon", "Chocolate"], "A")]
questions_500 = [("The Rhythm Heaven video game series inspired which artist's music video for her 2025 song 'Girl Like Me'?", [
                  "Tinashe", "Slayyyter", "PinkPantheress", "Charli XCX"], "C"), ("Which country defeated England in the 'Game of the Century'?", ["France", "Czechoslovakia", "Soviet Union", "Hungary"], "D"),
                 ("Which actress played Sophie in the sitcom 'Peep Show'?", ["Olivia Colman", "Dawn French", "Isy Suttie", "Sophie Winkleman"], "A")]
questions_750 = [("George Stubbs' Whistlejacket, a painting which sits in London's National Gallery, is a painting of what animal?", [
                  "Dog", "Cat", "Horse", "Deer"], "C"),
                 ("Which anthropologist, who passed away in 2025, was known for extensively studying chimpanzee populations?", [
                  "Margaret Mead", "Franz Boas", "Jane Goodall", "Marija Gimbutas"], "C"),
                 ("Which phenomenon causes aurorae to appear near Earth's poles?", ["Orbital resonance", "Solar wind", "Tidal forces", "Interplanetary dust"])]
questions_1000 = [("The author of Don Quixote, Miguel de Cervantes, fought at which battle of 1571?", [
                   "Lützen", "Lepanto", "Flodden", "Chaldiran"], "B"),
                  ("In which city is the smallest National Park by area in the United States?", [
                   "Chicago", "St. Louis", "New Orleans", "Wichita"], "B"),
                  ("Which of these Formula One drivers has won four or more drivers' championships?", ["Ayrton Senna", "Nelson Piquet", "Niki Lauda", "Juan Manuel Fangio"], "D")]

# ---- OPENING SEQUENCE ----
strtoprint = "Welcome to: Who Wants To Be A Thousandaire?"
for j in range(0, 5):
    print((len(strtoprint)+10) * "-")
    time.sleep(0.5)
print(" " * 5, strtoprint, " " * 5)
for j in range(0, 5):
    time.sleep(0.5)
    print((len(strtoprint)+10) * "-")
dummyinput = input("Press enter to start playing.\n")
time.sleep(2)

# ---- GAME LOOP ----
while END_FLAG == False:
    # define correct question set for the level
    rng = random.randint(0, 2)
    question = h.questionSelector(
        current, rng, questions_100, questions_250, questions_500, questions_750, questions_1000)
    # -------------------- #
    print(h.moneyVisualiser(current, winnings))
    time.sleep(2)
    h.questionFormatter(question, winnings[i+1])
    answer = str(input(
        f"\nEnter A, B, C or D to answer, or L to leave with the current money (£{current}).\nAnswer: "))
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
        time.sleep(1)
        print(f"Unfortunately, you leave with £0.")
        END_FLAG = True
