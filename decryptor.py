# Style the entire project
import pyfiglet as fig
print("\033[32m","="*100,"\033[m")
title = "Decryption Tool"
print("\033[32m",fig.figlet_format(title),"\033[m")
print(fig.figlet_format("Made by: Leoj M. Suaverdez",font="bubble"))
# User Types the Encrypted Text to Decrypt
encrypted_text = str(input("Enter the encrypted text: "))
# Decrypt the input text by replacing each encrypted character with its original vowel
# Replace "*" with "a"
decrypted_text = encrypted_text.replace("*","a")
# Replace "&" with "e"
decrypted_text = decrypted_text.replace("&","e")
# Replace "#" with "i"
decrypted_text = decrypted_text.replace("&","e")
# Replace "+" with "o"
decrypted_text = decrypted_text.replace("&","e")
# Replace "!" with "u"
decrypted_text = decrypted_text.replace("&","e")
# Print the decrypted text
print("\033[32m",decrypted_text,"\033[m")
print("\033[32m","="*100,"\033[m")
# Put it in a loop so the user can try to Decrypt again