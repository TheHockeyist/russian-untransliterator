# Ask user for string to be transliterated to Cyrillic, including soft and hard signs.

latin_string = input("What is the Latin text you want transliterated to Cyrillic? Include hard and soft signs by using apostrophes and quotation marks respectively. >")

# Mechanism to search the string and replace letters with Cyrillic equivalents, e.g. d to д. For unclear situations (e.g. deciding between и and й), it will either make an educated guess based on the context or ask the user what Cyrillic letter was actually meant.

latin_string.replace("a", "а")
latin_string.replace("b", "б")
latin_string.replace("c", "ц")
latin_string.replace("č", "ч")
latin_string.replace("d", "д")
latin_string.replace("е", "е")
latin_string.replace("f", "ф")
latin_string.replace("g", "г")
latin_string.replace("h", "х")
latin_string.replace("i", "и")
latin_string.replace("j", "й")
latin_string.replace("k", "к")
latin_string.replace("l", "л")
latin_string.replace("m", "м")
latin_string.replace("n", "н")
latin_string.replace("o", "о")
latin_string.replace("p", "п")
latin_string.replace("q", "я")
latin_string.replace("r", "р")
latin_string.replace("s", "с")
latin_string.replace("š", "ш")
latin_string.replace("t", "т")
latin_string.replace("u", "у")
latin_string.replace("v", "в")
latin_string.replace("w", "в")
latin_string.replace("x", "х")
latin_string.replace("y", "ы")
latin_string.replace("z", "з")
latin_string.replace("ž", "ж")
latin_string.replace("\'", "ь")
latin_string.replace("\"", "ъ")

# Check the Cyrillic transliteration for errors that break Russian orthography rules and fix them, e.g. цх ---> ч or йу ---> ю.

latin_string.replace("аы", "ай")
latin_string.replace("еы", "ей")
latin_string.replace("иы", "ий")
latin_string.replace("оы", "ой")
latin_string.replace("уы", "уй")
latin_string.replace("ыы", "ый") # Rather safe as -ыы never occurs at the end of words.
latin_string.replace("йу", "ю")
latin_string.replace("йа", "я")
latin_string.replace("ыу", "ю")
latin_string.replace("ыа", "я")

# йо actually occurs at the start a few words, e.g. йогурт, and in a few words like район or майор so that needs to be accounted for.

latin_string.replace("ые", "е") # Only needs to activate at the beginning of words. -ые is actually quite a common grammatical ending. Here, it could be easily messed up by accident.

latin_string.replace("йе", "е")

# Corrects spelling of words like Йемен and Йеллоунайф, and others with йе.

latin_string.replace("егер", "йегер") # Name.
latin_string.replace("ейтелес", "йейтелес") # Name.
latin_string.replace("ейтс", "йейтс") # Name.
latin_string.replace("ейттелес", "йейттелес") # Name.
latin_string.replace("еллоу", "йеллоу")
latin_string.replace("емен", "йемен")
latin_string.replace("ен", "йен") # Alone, as a name.
latin_string.replace("енни", "йенни") # Name.
latin_string.replace("енс", "йенс") # Name.
latin_string.replace("еспер", "йеспер") # Name.
latin_string.replace("есс", "йесс") # As part of a name.

latin_string.replace("ыо", "йо")
latin_string.replace("йо", "ё")

# Corrects spelling of words when э should be used instead of е.

# Corrects spelling of words like район, майор, and cases with йо as the first letter.

latin_string.replace("раён", "район")
latin_string.replace("маёр", "майор")
# More instances of -йо- in a word here

latin_string.replace("ёг", "йог") # At the beginning of words, e.g. йогa, йогурт. The only exceptions are minor geographical names.
latin_string.replace("ёд", "йод") # As a word, not as a part of a word. мёд is an actual word, for example.
latin_string.replace("ёжеф", "йожеф") # Name.
latin_string.replace("ёзеф", "йозеф") # Name.
latin_string.replace("ёрг", "йорг") # Part of some common names. Some words start with ёрг, but they are all minor geographical names.
latin_string.replace("ёрдан", "йордан") # Name.
latin_string.replace("ёрк", "йорк") # Alone, e.g. Нью Йорк. Used in a lot of words, e.g. шестёрка.
latin_string.replace("ёсеф", "йосеф") # Name.
latin_string.replace("ёсиф", "йосиф") # Name.
latin_string.replace("ёта", "йота") # Name of the Greek letter iota. Also common in words.
latin_string.replace("ёун", "йоун") # Name.
latin_string.replace("ёхан", "йохан") # Name.
latin_string.replace("ёшкар", "йошкар") # Part of a name of a city in Russia, Йошкар-Ола.
latin_string.replace("ёшуа", "йошуа") # Name.
latin_string.replace("ёэ", "йоэ") # Probably part of a name, since ёэ can never occur.

latin_string.replace("цх", "ч")
latin_string.replace("сх", "ш")
latin_string.replace("зх", "ж")
latin_string.replace("шч", "щ") # Шч cannot occur in Russian orthography.
