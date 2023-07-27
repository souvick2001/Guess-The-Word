word_list = ["mango", "banana", "camel", "umbrala"]   # As your choice or import randomly
import random
chose_word = random.choice(word_list)

print(f'pssst, the solution is {chose_word}')

display = []
word_length = len(chose_word)
for _ in range(word_length):
  display+= "_"
print(display)

end_of_game = False
while not end_of_game:
  guess = input("Guess the letter: ").lower()
  
  
  for position in range(word_length):
    letter = chose_word[position]
    if letter == guess:
      display[position] = letter
  
  
  print(display)

  if "_" not in display:
    end_of_game =True
    print("You Win .🎊")
