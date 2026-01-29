user_word = input("Enter a word--> ")
word_length = len(user_word)

if word_length == 0:
    print("You didn’t enter a word. Exiting program.")
else:
    values = []
    total_value = 0

    for index in range(word_length):
        num = int(input(f"Enter a number {index + 1}: "))
        values.append(num)
        total_value += num

    avg = total_value / word_length

    print(values)
    print(f"The word contains {word_length} letters")
    print(f"The computed average is {avg}")

    if word_length < avg:
        print(f"The length of the word {user_word} is less than the average.")
    elif word_length > avg:
        print(f"The length of the word {user_word} is greater than the average.")
    else:
        print(f"The length of the word {user_word} is equal to the average.")
