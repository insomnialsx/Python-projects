with open("data", "r", encoding="utf-8") as file:
    text=file.read()
print("Текст из файла:")
print(text)
words=text.split()
count=len(words)
print("Количество слов в тексте:", count)
