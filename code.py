import re

# Ask user for string to be transliterated to Cyrillic, including soft and hard signs.

latin_string = input("What is the Latin text you want transliterated to Cyrillic? Include hard and soft signs by using apostrophes and quotation marks respectively. >")

latin_string = latin_string.lower() # If the Latin string has any capitals, conver them to lowercase

# Mechanism to search the string and replace letters with Cyrillic equivalents, e.g. d to д. For unclear situations (e.g. deciding between и and й), it will either make an educated guess based on the context or ask the user what Cyrillic letter was actually meant.

if re.search("j", latin_string):
    uses_j = True # Sign that i = и only
else:
    uses_j = False # Sign that i probably also = й
    
cyrillic_string = latin_string
cyrillic_string = re.sub("a", "а", cyrillic_string)
cyrillic_string = re.sub("b", "б", cyrillic_string)
cyrillic_string = re.sub("c", "ц", cyrillic_string)
cyrillic_string = re.sub("č", "ч", cyrillic_string)
cyrillic_string = re.sub("d", "д", cyrillic_string)
cyrillic_string = re.sub("е", "е", cyrillic_string)
cyrillic_string = re.sub("f", "ф", cyrillic_string)
cyrillic_string = re.sub("g", "г", cyrillic_string)
cyrillic_string = re.sub("h", "х", cyrillic_string)
cyrillic_string = re.sub("k", "к", cyrillic_string)
cyrillic_string = re.sub("l", "л", cyrillic_string)
cyrillic_string = re.sub("m", "м", cyrillic_string)
cyrillic_string = re.sub("n", "н", cyrillic_string)
cyrillic_string = re.sub("o", "о", cyrillic_string)
cyrillic_string = re.sub("p", "п", cyrillic_string)
cyrillic_string = re.sub("q", "я", cyrillic_string)
cyrillic_string = re.sub("r", "р", cyrillic_string)
cyrillic_string = re.sub("s", "с", cyrillic_string)
cyrillic_string = re.sub("š", "ш", cyrillic_string)
cyrillic_string = re.sub("t", "т", cyrillic_string)
cyrillic_string = re.sub("u", "у", cyrillic_string)
cyrillic_string = re.sub("v", "в", cyrillic_string)
cyrillic_string = re.sub("w", "в", cyrillic_string)
cyrillic_string = re.sub("x", "х", cyrillic_string)
cyrillic_string = re.sub("y", "ы", cyrillic_string)
cyrillic_string = re.sub("z", "з", cyrillic_string)
cyrillic_string = re.sub("ž", "ж", cyrillic_string)
cyrillic_string = re.sub("\'", "ь", cyrillic_string)
cyrillic_string = re.sub("\"", "ъ", cyrillic_string)

# Properly replace J
if uses_j == True:
    cyrillic_string = re.sub("i", "и", cyrillic_string)
    cyrillic_string = re.sub("j", "й", cyrillic_string)
else:
    # For now, just replace it with и until we get the proper code in
    cyrillic_string = re.sub("i", "и", cyrillic_string)
    

# Check the Cyrillic transliteration for errors that break Russian orthography rules and fix them, e.g. цх ---> ч or йу ---> ю.

cyrillic_string = re.sub("аы", "ай", cyrillic_string)
cyrillic_string = re.sub("еы", "ей", cyrillic_string)
cyrillic_string = re.sub("иы", "ий", cyrillic_string)
cyrillic_string = re.sub("оы", "ой", cyrillic_string)
cyrillic_string = re.sub("уы", "уй", cyrillic_string)
cyrillic_string = re.sub("ыы", "ый", cyrillic_string) # Rather safe as -ыы never occurs at the end of words.
cyrillic_string = re.sub("йу", "ю", cyrillic_string)
cyrillic_string = re.sub("йа", "я", cyrillic_string)
cyrillic_string = re.sub("ыу", "ю", cyrillic_string)
cyrillic_string = re.sub("ыа", "я", cyrillic_string)

# йо actually occurs at the start a few words, e.g. йогурт, and in a few words like район or майор so that needs to be accounted for.

cyrillic_string = re.sub("^ые", "е", cyrillic_string) # Only needs to activate at the beginning of words. -ые is actually quite a common grammatical ending.

cyrillic_string = re.sub("йе", "е", cyrillic_string)

# Corrects spelling of words like Йемен and Йеллоунайф, and others with йе.

cyrillic_string = re.sub("егер", "йегер", cyrillic_string) # Name.
cyrillic_string = re.sub("ейтелес", "йейтелес", cyrillic_string) # Name.
cyrillic_string = re.sub("ейтс", "йейтс", cyrillic_string) # Name.
cyrillic_string = re.sub("ейттелес", "йейттелес", cyrillic_string) # Name.
cyrillic_string = re.sub("еллоу", "йеллоу", cyrillic_string)
cyrillic_string = re.sub("емен", "йемен", cyrillic_string)
cyrillic_string = re.sub("ен", "йен", cyrillic_string) # Alone, as a name.
cyrillic_string = re.sub("енни", "йенни", cyrillic_string) # Name.
cyrillic_string = re.sub("енс", "йенс", cyrillic_string) # Name.
cyrillic_string = re.sub("еспер", "йеспер", cyrillic_string) # Name.
cyrillic_string = re.sub("есс", "йесс", cyrillic_string) # As part of a name.

cyrillic_string = re.sub("ыо", "йо", cyrillic_string)
cyrillic_string = re.sub("йо", "ё", cyrillic_string)

# Corrects spelling of words when э should be used instead of е.

cyrillic_string = re.sub("(^| )ето", "это", cyrillic_string) # Words like лето mess this up, so it's only changed at the beginning.
cyrillic_string = re.sub("(^| )ети", "эти", cyrillic_string) # Same thing here.
cyrillic_string = re.sub("експерт", "эксперт", cyrillic_string)
cyrillic_string = re.sub("електричест", "электричест", cyrillic_string)


# Corrects spelling of words like район, майор, and cases with йо.

cyrillic_string = re.sub("аёва", "айова", cyrillic_string) # Geographical name.
cyrillic_string = re.sub("баёнет", "байонет", cyrillic_string)
cyrillic_string = re.sub("ваёминг", "вайоминг", cyrillic_string) # Geographical name.
cyrillic_string = re.sub("ваёл", "вайол", cyrillic_string) # E.g. вайола
cyrillic_string = re.sub("заён", "зайон", cyrillic_string)
cyrillic_string = re.sub("коёт", "койот", cyrillic_string)
cyrillic_string = re.sub("маёнез", "майонез", cyrillic_string)
cyrillic_string = re.sub("маёр", "майор", cyrillic_string)
cyrillic_string = re.sub("маётта", "майотта", cyrillic_string) # Geographical name.
cyrillic_string = re.sub("огаё", "огайо", cyrillic_string) # Geographical name.
cyrillic_string = re.sub("ораён", "орайон", cyrillic_string)
cyrillic_string = re.sub("паёл", "пайол", cyrillic_string)
cyrillic_string = re.sub("раён", "район", cyrillic_string)
cyrillic_string = re.sub("тоёта", "тойота", cyrillic_string)

# More instances of -йо- in a word here

cyrillic_string = re.sub("ёг", "йог", cyrillic_string) # At the beginning of words, e.g. йогa, йогурт. The only exceptions are minor geographical names.
cyrillic_string = re.sub("ёд", "йод", cyrillic_string) # As a word, not as a part of a word. мёд is an actual word, for example.
cyrillic_string = re.sub("ёжеф", "йожеф", cyrillic_string) # Name.
cyrillic_string = re.sub("ёзеф", "йозеф", cyrillic_string) # Name.
cyrillic_string = re.sub("ёрг", "йорг", cyrillic_string) # Part of some common names. Some words start with ёрг, but they are all minor geographical names.
cyrillic_string = re.sub("ёрдан", "йордан", cyrillic_string) # Name.
cyrillic_string = re.sub("ёрк", "йорк", cyrillic_string) # Alone, e.g. Нью Йорк. Used in a lot of words, e.g. шестёрка.
cyrillic_string = re.sub("ёсеф", "йосеф", cyrillic_string) # Name.
cyrillic_string = re.sub("ёсиф", "йосиф", cyrillic_string) # Name.
cyrillic_string = re.sub("ёта", "йота", cyrillic_string) # Name of the Greek letter iota. Also common in words.
cyrillic_string = re.sub("ёун", "йоун", cyrillic_string) # Name.
cyrillic_string = re.sub("ёхан", "йохан", cyrillic_string) # Name.
cyrillic_string = re.sub("ёшкар", "йошкар", cyrillic_string) # Part of a name of a city in Russia, Йошкар-Ола.
cyrillic_string = re.sub("ёшуа", "йошуа", cyrillic_string) # Name.
cyrillic_string = re.sub("ёэ", "йоэ", cyrillic_string) # Probably part of a name, since ёэ can never occur.

cyrillic_string = re.sub("цх", "ч", cyrillic_string)
cyrillic_string = re.sub("сх", "ш", cyrillic_string)
cyrillic_string = re.sub("зх", "ж", cyrillic_string)
cyrillic_string = re.sub("шч", "щ", cyrillic_string) # Шч cannot occur in Russian orthography.

if uses_j == False:
    # Ask user in vowel + и combinations which ones are really й.
    pass # Placeholder

print("\"{}\" would be transliterated as:\n{}".format(latin_string, cyrillic_string))
