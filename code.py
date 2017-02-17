# Ask user for string to be transliterated to Cyrillic, including soft and hard signs.

latin_string = raw_input("What is the Latin text you want transliterated to Cyrillic? Include hard and soft signs by using apostrophes and quotation marks respectively.")
cyrillic_string = raw_input

# Mechanism to search the string and replace letters with Cyrillic equivalents, e.g. d to д. For unclear situations (e.g. deciding between и and й), it will either make an educated guess based on the context or ask the user what Cyrillic letter was actually meant.

str.replace("a", "а")
str.replace("b", "б")
str.replace("c", "ц")
str.replace("č", "ч")
str.replace("d", "д")
str.replace("е", "е")
str.replace("f", "ф")
str.replace("g", "г")
str.replace("h", "х")
str.replace("i", "и")
str.replace("j", "й")
str.replace("k", "к")
str.replace("l", "л")
str.replace("m", "м")
str.replace("n", "н")
str.replace("o", "о")
str.replace("p", "п")
str.replace("q", "я")
str.replace("r", "р")
str.replace("s", "с")
str.replace("š", "ш")
str.replace("t", "т")
str.replace("u", "у")
str.replace("v", "в")
str.replace("w", "в")
str.replace("x", "х")
str.replace("y", "ы")
str.replace("z", "з")
str.replace("ž", "ж")
str.replace("\'", "ь")
str.replace("\"", "ъ")

# Check the Cyrillic transliteration for errors that break Russian orthography rules and fix them, e.g. цх ---> ч or йу ---> ю.

str.replace("аы", "ай")
str.replace("еы", "ей")
str.replace("иы", "ий")
str.replace("оы", "ой")
str.replace("уы", "уй")
str.replace("ыы", "ый") # Rather safe as -ыы never occurs at the end of words.
str.replace("йу", "ю")
str.replace("йа", "я")
str.replace("ыу", "ю")
str.replace("ыа", "я")

# йо actually occurs at the start a few words, e.g. йогурт, and in a few words like район or майор so that needs to be accounted for.

str.replace("ые", "е") # Only needs to activate at the beginning of words. -ые is actually quite a common grammatical ending. Here, it could be easily messed up by accident.

str.replace("йе", "е")

# Corrects spelling of words like Йемен and Йеллоунайф.

str.replace("емен", "йемен")
str.replace("еллоу", "йеллоу")

str.replace("ыо", "йо")
str.replace("йо", "ё")

# Corrects spelling of words when э should be used instead of е.

# Corrects spelling of words like район, майор, and cases with й as the first letter.

str.replace("раён", "район")
str.replace("маёр", "майор")
# More instances of -йо- in a word here

str.replace("ёa", "йоa") # At the beginning of words.
str.replace("ёг", "йог") # At the beginning of words, e.g. йогa, йогурт. The only exceptions are minor geographical names.
str.replace("ёд", "йод") # As a word, not as a part of a word. мёд is an actual word, for example.
str.replace("ёжеф", "йожеф") # Name.
str.replace("ёзеф", "йозеф") # Name.
str.replace("ёрг", "йорг") # Part of some common names. Some words start with ёрг, but they are all minor geographical names.
str.replace("ёрдан", "йордан") # Name.
str.replace("ёрк", "йорк") # Alone, e.g. Нью Йорк. Used in a lot of words, e.g. шестёрка.
str.replace("ёсеф", "йосеф") # Name.
str.replace("ёсил", "йосил") # Name. Might be used as a suffix in a few words, but I'm not sure.
str.replace("ёта", "йота") # Name of the Greek letter iota. Also common in words.
str.replace("ёун", "йоун") # Name.
str.replace("ёхан", "йохан") # Name.
str.replace("ёшкар", "йошкар") # Part of a name of a city in Russia, Йошкар-Ола.
str.replace("ёшуа", "йошуа") # Name.
str.replace("ёэ", "йоэ") # Probably part of a name, since ёэ can never occur.

str.replace("цх", "ч")
str.replace("сх", "ш")
str.replace("зх", "ж")
str.replace("шч", "щ")
# Шч cannot occur in Russian orthography.
str.replace("ъйо", "ъё")
str.replace("ьйо", "ьё")

# Print final result in copy-pasteable format.
