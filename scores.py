import sys

def calculate_stats(scores):
    total = sum(scores)
    average = total / len(scores) if len(scores) > 0 else 0
    return total, average
if __name__ == "__main__":
    scores = [float(x) for x in sys.argv[1:]]
    total, average = calculate_stats(scores)
    print("--- Local Branch Output ---")
    print(f"Scores entered: {scores}")
    print(f"Sum: {total}")
    print(f"Average: {average}")
    print(f"Maximum: {max(scores)}")
    print(f"Minimum: {min(scores)}")