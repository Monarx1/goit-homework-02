sum = 0

while True:
    num = int(input("Enter integer (0 for output): ")) # Запитуємо ціле число
    if num == 0: # Якщо число 0 - вихід з першого циклу
        break

    for i in range(num + 1): # Знаходимо суму чисел від 0 до num включно
        sum += i 

    print("Current sum:", sum) # Виводимо поточну суму

print("Final sum:", sum) # Виводимо остаточну суму після виходу з першого циклу