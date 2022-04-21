# My own option.
import CaesarArt
print(CaesarArt.logo)
again = ""
while again == "yes" or again == "":
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  # Single function.
  if shift > 25:
    shift = shift % 26

  def caesar(text, shift):
      word = []
      for letter in text:
          if letter not in alphabet:
              word.append(letter)
              continue
          letter_position = alphabet.index(letter)
          if direction == "encode":
              word.append(alphabet[letter_position + shift])
          elif direction == "decode":
              word.append(alphabet[letter_position - shift])
      final_word = "".join(word)
      print(f"Your {direction }d word is '{final_word}'")

  caesar(text, shift)
  again = input("Do you want to try again? Type 'yes' to go again or 'no' to stop the Cipher.\n")
print(CaesarArt.end)