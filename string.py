# Вывести последнюю букву в слове
word = 'Архангельск'
for i in word[-1]:
    print(i)
print()


# Вывести количество букв "а" в слове
word = 'Архангельск'
num = 0
num2 = 0
for i in word:
    if i == 'А':
        num += 1
    elif i == 'а':
        num += 1
print(num + num2)
print()


# Вывести количество гласных букв в слове
word = 'Архангельск'
sr = 'Аае'
s = 0
for i in word:
    if i in sr:
        s += 1
print(s)
print()


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))
print()


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for i in sentence.split():
    print(i[0])
print()


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
print(sum(map(len, words)) / len(words))


