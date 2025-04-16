SENTENCE_START: str = "Code in Place is fun. I learned to program and used Python to make my "

def main():
    # Prompt user for adjective, noun, and verb
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")
    
    # Combine the sentence start with user inputs and print
    print(f"{SENTENCE_START}{adjective} {noun} {verb}!")

if __name__ == '__main__':
    main()