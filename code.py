# Ask user for string to be transliterated to Cyrillic, including soft and hard signs.

latin_string = raw_input("Ask user for something.")
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
# йе and йо actually occur at the start a few words, e.g. Йемен, йогурт, and in a few words like район or майор so that needs to be accounted for.

str.replace("йе", "е")
# Code to check for words like Йемен, Йеллоунайф, etc. and correct them.
str.replace("ые", "е") # Only needs to activate at the beginning of words. -ые is actually quite a common grammatical ending. Here, it could be easily messed up by accident.

str.replace("цх", "ч")
str.replace("сх", "ш")
str.replace("зх", "ж")
str.replace("шч", "щ")
# Шч cannot occur in Russian orthography.
str.replace("ъйо", "ъё")
str.replace("ьйо", "ьё")
str.replace("ъйе", "ъе")
str.replace("ьйе", "ье")

# Print final result in copy-pasteable format.
