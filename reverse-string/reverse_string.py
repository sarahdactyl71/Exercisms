def reverse(text):
    string = ''
    count = -1
    for letter in text:
        letter = text[count]
        string += letter
        count += -1
        return string
