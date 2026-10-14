lang = input("Enter a language: ")

def is_available(language):
    languages = ["english", "uzbek", "russian"]
    for i in range(len(languages)):
        if language == languages[i]:
            return "Available"
    return "Not Available"

print(is_available(lang))