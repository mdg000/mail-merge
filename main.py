# 100 Days of Code
# File IO Operations
# Creating Invitation Letters from a Letter Template and List of Names

PLACEHOLDER = "[name]"

# open and read invited names
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# open and read starting letter
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        # create and write file output to ReadyToSend
        with open(f"Output/ReadyToSend/Letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)
