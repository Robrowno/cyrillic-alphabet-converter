
### CYRILLIC TO LATIN PHONETIC CONVERTER

def cyrillic_latin():

    """
    For converting cyrillic text into phonetic latin text.
    """

    cyrillic_alpha_dict = {
        "А": "A", "а": "a",
        "Б": "B", "б": "b",
        "В": "V", "в": "v",
        "Г": "G", "г": "g",
        "Д": "D", "д": "d",
        "Е": "E", "е": "e",
        "Ж": "Zh", "ж": "zh",
        "З": "Z", "з": "z",
        "И": "I", "и": "i",
        "Й": "Y", "й": "y",
        "К": "K", "к": "k",
        "Л": "L", "л": "l",
        "М": "M", "м": "m",
        "Н": "N", "н": "n",
        "О": "O", "о": "o",
        "П": "P", "п": "p",
        "Р": "R", "р": "r",
        "С": "S", "с": "s",
        "Т": "T", "т": "t",
        "У": "U", "у": "u",
        "Ф": "F", "ф": "f",
        "Х": "H", "х": "h",
        "Ц": "Ts", "ц": "ts",
        "Ч": "Ch", "ч": "ch",
        "Ш": "Sh", "ш": "sh",
        "Щ": "Sht", "щ": "sht",
        "Ъ": "A", "ъ": "a",
        "Ь": "", "ь": "",
        "Ю": "Yu", "ю": "yu",
        "Я": "Ya", "я": "ya"
    }


    # enter cyrillic text
    text = input("Enter your text: ")

    # convert the text
    
    # text_as_list = [cyrillic_alpha_dict[char] if char in cyrillic_alpha_dict else char for char in text]

    text_as_list = []
    for char in text:
        if char in cyrillic_alpha_dict:
            text_as_list.append(cyrillic_alpha_dict[char])
        else:
            text_as_list.append(char)

    # join the list elements to form a string

    # latin_text = ''.join(text_as_list)

    latin_text = ""
    for char in text_as_list:
        latin_text += char

    print(latin_text)
    


cyrillic_latin()