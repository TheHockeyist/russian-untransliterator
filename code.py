import re

# Ask user for string to be transliterated to Cyrillic, including soft and hard signs.

latin_string = input("What is the Latin text you want transliterated to Cyrillic? Include hard and soft signs by using apostrophes and quotation marks respectively. >")

# Mechanism to search the string and replace letters with Cyrillic equivalents, e.g. d to д. For unclear situations (e.g. deciding between и and й), it will either make an educated guess based on the context or ask the user what Cyrillic letter was actually meant.

if re.search("j", latin_string):
    uses_j = True # Sign that i = и only
else:
    uses_j = False # Sign that i probably also = й
    
cyrillic_string = latin_string
cyrillic_string = cyrillic_string.replace("a", "а")
cyrillic_string = cyrillic_string.replace("b", "б")
cyrillic_string = cyrillic_string.replace("c", "ц")
cyrillic_string = cyrillic_string.replace("č", "ч")
cyrillic_string = cyrillic_string.replace("d", "д")
cyrillic_string = cyrillic_string.replace("е", "е")
cyrillic_string = cyrillic_string.replace("f", "ф")
cyrillic_string = cyrillic_string.replace("g", "г")
cyrillic_string = cyrillic_string.replace("h", "х")
cyrillic_string = cyrillic_string.replace("i", "и")
cyrillic_string = cyrillic_string.replace("j", "й")
cyrillic_string = cyrillic_string.replace("k", "к")
cyrillic_string = cyrillic_string.replace("l", "л")
cyrillic_string = cyrillic_string.replace("m", "м")
cyrillic_string = cyrillic_string.replace("n", "н")
cyrillic_string = cyrillic_string.replace("o", "о")
cyrillic_string = cyrillic_string.replace("p", "п")
cyrillic_string = cyrillic_string.replace("q", "я")
cyrillic_string = cyrillic_string.replace("r", "р")
cyrillic_string = cyrillic_string.replace("s", "с")
cyrillic_string = cyrillic_string.replace("š", "ш")
cyrillic_string = cyrillic_string.replace("t", "т")
cyrillic_string = cyrillic_string.replace("u", "у")
cyrillic_string = cyrillic_string.replace("v", "в")
cyrillic_string = cyrillic_string.replace("w", "в")
cyrillic_string = cyrillic_string.replace("x", "х")
cyrillic_string = cyrillic_string.replace("y", "ы")
cyrillic_string = cyrillic_string.replace("z", "з")
cyrillic_string = cyrillic_string.replace("ž", "ж")
cyrillic_string = cyrillic_string.replace("\'", "ь")
cyrillic_string = cyrillic_string.replace("\"", "ъ")

# Check the Cyrillic transliteration for errors that break Russian orthography rules and fix them, e.g. цх ---> ч or йу ---> ю.

cyrillic_string = cyrillic_string.replace("аы", "ай")
cyrillic_string = cyrillic_string.replace("еы", "ей")
cyrillic_string = cyrillic_string.replace("иы", "ий")
cyrillic_string = cyrillic_string.replace("оы", "ой")
cyrillic_string = cyrillic_string.replace("уы", "уй")
cyrillic_string = cyrillic_string.replace("ыы", "ый") # Rather safe as -ыы never occurs at the end of words.
cyrillic_string = cyrillic_string.replace("йу", "ю")
cyrillic_string = cyrillic_string.replace("йа", "я")
cyrillic_string = cyrillic_string.replace("ыу", "ю")
cyrillic_string = cyrillic_string.replace("ыа", "я")

# йо actually occurs at the start a few words, e.g. йогурт, and in a few words like район or майор so that needs to be accounted for.

cyrillic_string = cyrillic_string.replace("ые", "е") # Only needs to activate at the beginning of words. -ые is actually quite a common grammatical ending. Here, it could be easily messed up by accident.

cyrillic_string = cyrillic_string.replace("йе", "е")

# Corrects spelling of words like Йемен and Йеллоунайф, and others with йе.

cyrillic_string = cyrillic_string.replace("егер", "йегер") # Name.
cyrillic_string = cyrillic_string.replace("ейтелес", "йейтелес") # Name.
cyrillic_string = cyrillic_string.replace("ейтс", "йейтс") # Name.
cyrillic_string = cyrillic_string.replace("ейттелес", "йейттелес") # Name.
cyrillic_string = cyrillic_string.replace("еллоу", "йеллоу")
cyrillic_string = cyrillic_string.replace("емен", "йемен")
cyrillic_string = cyrillic_string.replace("ен", "йен") # Alone, as a name.
cyrillic_string = cyrillic_string.replace("енни", "йенни") # Name.
cyrillic_string = cyrillic_string.replace("енс", "йенс") # Name.
cyrillic_string = cyrillic_string.replace("еспер", "йеспер") # Name.
cyrillic_string = cyrillic_string.replace("есс", "йесс") # As part of a name.

cyrillic_string = cyrillic_string.replace("ыо", "йо")
cyrillic_string = cyrillic_string.replace("йо", "ё")

# Corrects spelling of words when э should be used instead of е.

cyrillic_string = cyrillic_string.replace("ето", "это") # What about words like лето?
cyrillic_string = cyrillic_string.replace("ети", "эти")

# Corrects spelling of words like район, майор, and cases with йо.

cyrillic_string = cyrillic_string.replace("аёва", "айова") # Geographical name.
cyrillic_string = cyrillic_string.replace("баёнет", "байонет")
cyrillic_string = cyrillic_string.replace("ваёминг", "вайоминг") # Geographical name.
cyrillic_string = cyrillic_string.replace("ваёл", "вайол") # E.g. вайола
cyrillic_string = cyrillic_string.replace("заён", "зайон")
cyrillic_string = cyrillic_string.replace("коёт", "койот")
cyrillic_string = cyrillic_string.replace("маёнез", "майонез")
cyrillic_string = cyrillic_string.replace("маёр", "майор")
cyrillic_string = cyrillic_string.replace("маётта", "майотта") # Geographical name.
cyrillic_string = cyrillic_string.replace("огаё", "огайо") # Geographical name.
cyrillic_string = cyrillic_string.replace("ораён", "орайон")
cyrillic_string = cyrillic_string.replace("паёл", "пайол")
cyrillic_string = cyrillic_string.replace("раён", "район")
cyrillic_string = cyrillic_string.replace("тоёта", "тойота")

# More instances of -йо- in a word here

cyrillic_string = cyrillic_string.replace("ёг", "йог") # At the beginning of words, e.g. йогa, йогурт. The only exceptions are minor geographical names.
cyrillic_string = cyrillic_string.replace("ёд", "йод") # As a word, not as a part of a word. мёд is an actual word, for example.
cyrillic_string = cyrillic_string.replace("ёжеф", "йожеф") # Name.
cyrillic_string = cyrillic_string.replace("ёзеф", "йозеф") # Name.
cyrillic_string = cyrillic_string.replace("ёрг", "йорг") # Part of some common names. Some words start with ёрг, but they are all minor geographical names.
cyrillic_string = cyrillic_string.replace("ёрдан", "йордан") # Name.
cyrillic_string = cyrillic_string.replace("ёрк", "йорк") # Alone, e.g. Нью Йорк. Used in a lot of words, e.g. шестёрка.
cyrillic_string = cyrillic_string.replace("ёсеф", "йосеф") # Name.
cyrillic_string = cyrillic_string.replace("ёсиф", "йосиф") # Name.
cyrillic_string = cyrillic_string.replace("ёта", "йота") # Name of the Greek letter iota. Also common in words.
cyrillic_string = cyrillic_string.replace("ёун", "йоун") # Name.
cyrillic_string = cyrillic_string.replace("ёхан", "йохан") # Name.
cyrillic_string = cyrillic_string.replace("ёшкар", "йошкар") # Part of a name of a city in Russia, Йошкар-Ола.
cyrillic_string = cyrillic_string.replace("ёшуа", "йошуа") # Name.
cyrillic_string = cyrillic_string.replace("ёэ", "йоэ") # Probably part of a name, since ёэ can never occur.

cyrillic_string = cyrillic_string.replace("цх", "ч")
cyrillic_string = cyrillic_string.replace("сх", "ш")
cyrillic_string = cyrillic_string.replace("зх", "ж")
cyrillic_string = cyrillic_string.replace("шч", "щ") # Шч cannot occur in Russian orthography.

print("\"{}\" would be transliterated as:\n{}".format(latin_string, cyrillic_string))
