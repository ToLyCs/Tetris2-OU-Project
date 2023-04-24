class Score:
    def __init__(self):
        pass

    # Simple function to write scores to score.txt, in format: score username \n
    def write_score(self, highscore, name):
        with open('score.txt', 'a') as file:
            file.write(f"{name} {highscore}\n")

    def remove_duplicates(self, filename):
        # Read in the lines from the file and store them in a set
        with open(filename, "r") as f:
            unique_lines = set(f.readlines())

        # Write the unique lines back to the file
        with open(filename, "w") as f:
            f.writelines(unique_lines)

    # Looks through score.txt, and organizes users in descending order
    def rank_scores(self):
        with open('score.txt', 'r') as file:
            lines = file.readlines()
            lines_scores = [(line.strip().split()[0], int(line.strip().split()[1])) for line in lines]
            lines_sorted = sorted(lines_scores, key=lambda x: x[1], reverse=True)
        with open('score.txt', 'w') as file:
            for i, line in enumerate(lines_sorted):
                file.write(f"{line[0]} {line[1]}\n")