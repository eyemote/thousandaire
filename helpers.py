def questionSelector(current: int, rng: int) -> tuple:
    if current == 0:
        return questions_100[rng]
    elif current == 100:
        return questions_250[rng]
    elif current == 250:
        return questions_500[rng]
    elif current == 500:
        return questions_750[rng]
    elif current == 750:
        return questions_1000[rng]


def questionFormatter(question: tuple, currentValue: int) -> str:
    import time
    print(f"Your next question for £{currentValue}...\n")
    time.sleep(2)
    print(question[0])
    time.sleep(4)
    abcd = "ABCD"
    for answer in enumerate(question[1]):
        print(f"{abcd[answer[0]]}. {answer[1]}")
        time.sleep(1)


def questionIsRight(question: tuple, answer: str) -> bool:
    return question[2].lower() == answer.lower()


def moneyVisualiser(currentValue: int, winnings: list[int]) -> str:
    visual = ""
    for amount in winnings[::-1]:
        visual += f"£{amount}"
        if amount == currentValue:
            visual += "  <--- You"
        visual += "\n"
    return visual
