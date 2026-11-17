def questionSelector(current: int, rng: int, q100: list[tuple],
                     q250: list[tuple], q500: list[tuple],
                     q750: list[tuple], q1000: list[tuple]) -> tuple:
    if current == 0:
        return q100[rng]
    elif current == 100:
        return q250[rng]
    elif current == 250:
        return q500[rng]
    elif current == 500:
        return q750[rng]
    elif current == 750:
        return q1000[rng]


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
    visual = "MONEY LADDER\n------------\n"
    for amount in winnings[::-1]:
        num_space = (10 - len(str(amount))) * "-"
        visual += f"{num_space} £{amount}"
        if amount == currentValue:
            visual += "  <--- You"
        visual += "\n"
    visual += "------------\n"
    return visual
