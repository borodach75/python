trans = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text_4.txt', 'r', encoding='utf-8') as my_read:
    with open('text_4_out.txt', 'w', encoding='utf-8') as my_write:
        for line in my_read:
            for word in line.split():
                word = trans.get(word, word)
                print(word, file=my_write, end=' ')
            print(file=my_write)