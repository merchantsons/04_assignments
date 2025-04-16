# 09_sentence_generator.py by merchantsons

def make_sentence(word: str, part_of_speech: int):
    """
    Prints a sentence using the given word and part of speech.
    """
    if part_of_speech == 0:
        # noun
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        # verb
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        # adjective
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        # part_of_speech is invalid (not 0, 1, or 2)
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

def main():
    word = input("Please type a noun, verb, or adjective: ")  # Prompt the user to enter a word
    print("Is this a noun, verb, or adjective?")
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))  # Prompt the user to enter the part of speech
    make_sentence(word, part_of_speech)  # Call the make_sentence function with the user's input

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
