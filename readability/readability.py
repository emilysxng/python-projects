def main():
    text = input("Input Text Here: ")

    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    print(f"Letters: {letters}")
    print(f"Words: {words}")
    print(f"Sentences: {sentences}")

    avg_letters = (letters / words) * 100
    avg_sentences = (sentences / words) * 100

    grade_level = 0.0588 * avg_letters - 0.296 * avg_sentences - 15.8
    rounded_grade_level = round(grade_level)
 
    if rounded_grade_level < 1:
        print("Grade level: Below grade 1")

    elif rounded_grade_level >= 1 and rounded_grade_level <= 12:
        print(f"Grade level: {rounded_grade_level}")

    elif rounded_grade_level == 13:
        print("Grade Level: First year university")

    elif rounded_grade_level == 14:
        print("Grade Level: Second year university")

    elif rounded_grade_level == 15:
        print("Grade Level: Third year university")

    else:
        print("Grade Level: Fourth year university +")

def count_letters(text):
    letters = 0
    for char in text:
        char = ord(char)
        if (char >= 48 and char <= 57) or (char >= 65 and char <= 90) or (char >= 97 and char <= 122):
            letters += 1
    return letters

def count_words(text):
    words = 1
    for char in text:
        char = ord(char)
        if char == 32:
            words += 1
    return words

def count_sentences(text):
    sentences = 0
    for char in text:
        char = ord(char)
        if char == 33 or char == 46 or char == 63:
            sentences += 1
    return sentences

if __name__ == "__main__":
    main()
