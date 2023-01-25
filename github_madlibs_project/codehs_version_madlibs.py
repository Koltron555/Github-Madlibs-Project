"""
This program will let the user choose a mad libs prompt.
It will then ask the user to fill in the blanks,
repeating the prompt if they enter an incorrect value.
It will then print out the finished mad libs.
"""

quotes = open("madlibs.txt", "r")
quotes = quotes.readlines()


#continuously ask the user for a valid choice of mad libs
def get_quote_choice():
    while True:
        user_quote_choice = input("What kind of mad libs would you like? (Star Wars, Skyrim, Halo): ")
        user_quote_choice = user_quote_choice.lower()
        print(user_quote_choice)
        
        #only return the user's choice if they enter a valid option
        for i in range(len(quotes)):
            if user_quote_choice in quotes[i]:
                if i % 2 == 0:
                    print("You chose: " + quotes[i])
                    
                    return user_quote_choice
                
        #if the user didn't enter a valid response, tell them and continue looping
        print("Enter a valid mad libs.")
            


#turn the mad libs quote the user chose into a list
def get_quote_prompt():
    for i in range(len(quotes)):
        if quote_choice in quotes[i]:
            quote = quotes[i + 1].split()
            
            return quote
            


#ask the user to fill in the blank words from the prompt they chose
def get_quote_words():
    #check each word from the prompt for a blank
    for i in range(len(quote_prompt)):
        #ask for a noun if it found a blank noun
        if quote_prompt[i] == "<noun>":
            quote_prompt[i] = input("Enter a noun: ")
            print(quote_prompt[i])
            
        #ask for an adjective if it found a blank adjective
        elif quote_prompt[i] == "<adjective>":
            quote_prompt[i] = input("Enter an adjective: ")
            print(quote_prompt[i])
            
        #ask for a proper noun if it found a blank proper noun
        elif quote_prompt[i] == "<proper_noun>":
            quote_prompt[i] = input("Enter a proper noun: ")
            print(quote_prompt[i])
            
        #ask for a verb if it found a blank verb
        elif quote_prompt[i] == "<verb>":
            quote_prompt[i] = input("Enter a verb: ")
            print(quote_prompt[i])
            
    #return the mab libs as one whole string
    return " ".join(quote_prompt)
    


#The game will keep repeating until the user tells it to stop
while True:
    round_choice = input("Do you want to play a round of madlibs? (yes/no): ")
    print(round_choice)
    if round_choice.lower() == "yes":
        quote_choice = get_quote_choice()
        quote_prompt = get_quote_prompt()
        quote_words = get_quote_words()
        print(quote_words)
        
    elif round_choice.lower() == "no":
        break
    
    else:
        print("Invalid input!")
        