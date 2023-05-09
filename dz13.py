message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""

for ch in message:
    if ch.isalpha():
        if ch.isupper():
            encoded_message += chr((ord(ch) - ord('A') + offset) % 26 + ord('A'))
        else:
            encoded_message += chr((ord(ch) - ord('a') + offset) % 26 + ord('a'))
    else:
        encoded_message += ch

print("Encoded message:", encoded_message)