'''(Analyze scores) Write a program that reads an unspecified number of scores and
determines how many scores are above or equal to the average and how many
scores are below the average. Assume the input numbers are separated by one
space in one line.'''

def analyzeScores():
    scores_str = input("Enter scores separated by spaces:")
    scores = [float(score) for score in scores_str.split()]

    if not scores:
        print("No scores entered.")
        return

    total_sum = sum(scores)
    average = total_sum / len(scores)

    above_or_equal_average = 0
    below_average = 0

    for score in scores:
        if score >= average:
            above_or_equal_average += 1
        else:
            below_average += 1

        print(f"\nAverage score: {average:2f}")
        print(f"Number of scores above or equal to average: {above_or_equal_average}")
        print(f"Number of scores below average: {below_average}")

analyzeScores()
