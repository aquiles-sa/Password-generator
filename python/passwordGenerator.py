import random as rand

specialCharacters = ['!', '@', '#', '$', '%', '¨', '&', '*', '(', ')','Ç']
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
operators = ['+', '-', '/', '*']

upperLetters = list(letters)
lowerLetters = list(letters.lower())
upperLetters.extend(lowerLetters)

specialCharacters.extend(numbers)
specialCharacters.extend(operators)
specialCharacters.extend(upperLetters)

allCharacters = specialCharacters

def generatePassword(targetPasswordLength):
	password = ""

	for i in range(0, targetPasswordLength, 1):
		generatedCharacters = rand.choice(allCharacters)
		password += str(generatedCharacters)

	return password


print("-" * 10 + " Password generator " + "-" * 10)

personName = str(input("Enter your name: "))
print('\n')
print(f"Hello {personName.strip().capitalize()}!")

while True:
    passwordLength = int(input("How many characters do you want for your password? "))
    finalPassword = generatePassword(passwordLength)

    print('\n')

    print(f"Your password is: '{finalPassword}'")
    
    continueOperation = input("Would you like to generate another password? [Y/N]: ").lower()
    
    if continueOperation == 'y':
        continue
    elif continueOperation == 'n':
          print("-" * 10 + " Thanks for using! " + "-" * 10)
    
    while continueOperation != 'n':
        continueOperation = input("Would you like to generate another password? [Y/N]: ").lower()
        
        if continueOperation == 'n':
          print("-" * 10 + " Thanks for using! " + "-" * 10)
          break
    break