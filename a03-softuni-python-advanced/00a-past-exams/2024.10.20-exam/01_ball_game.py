def football_game(strengths, accuracies):
    goals_scored = 0

    while strengths and accuracies:
        strength = strengths[-1]
        accuracy = accuracies[0]
        
        if strength + accuracy == 100:
            # Goal scored
            goals_scored += 1
            strengths.pop()
            accuracies.pop(0)
        elif strength + accuracy < 100:
            # Remove the smaller value or handle equal case
            if strength < accuracy:
                strengths.pop()
            elif strength > accuracy:
                accuracies.pop(0)
            else:
                strengths[-1] = strength + accuracy
                accuracies.pop(0)
        else:
            # Sum greater than 100
            strengths[-1] -= 10
            accuracies.append(accuracies.pop(0))

    # Output Results
    if goals_scored == 3:
        print("Paul scored a hat-trick!")
    elif goals_scored > 3:
        print("Paul performed remarkably well!")
    elif goals_scored > 0:
        print("Paul failed to make a hat-trick.")
    else:
        print("Paul failed to score a single goal.")

    if goals_scored > 0:
        print(f"Goals scored: {goals_scored}")

    if strengths:
        print("Strength values left:", ", ".join(map(str, strengths)))
    if accuracies:
        print("Accuracy values left:", ", ".join(map(str, accuracies)))

# Input handling
strengths = list(map(int, input().split()))
accuracies = list(map(int, input().split()))

# Run the game
football_game(strengths, accuracies)
