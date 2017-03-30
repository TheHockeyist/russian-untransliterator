import re

# Ask user for string to be transliterated to Cyrillic, including soft and hard signs.

latin_string = input("What is the Latin text you want transliterated to Cyrillic? Include hard and soft signs by using apostrophes and quotation marks respectively.\n> ")

latin_string = latin_string.lower() # If the Latin string has any capitals, conver them to lowercase

# Mechanism to search the string and replace letters with Cyrillic equivalents, e.g. d to д. For unclear situations (e.g. deciding between и and й), it will either make an educated guess based on the context or ask the user what Cyrillic letter was actually meant.

if re.search("j", latin_string):
    uses_j = True # Sign that i = и only
else:
    uses_j = False # Sign that i probably also = й
    
cyrillic_string = latin_string

substitutions = [
    ("a", "а"),
    ("b", "б"),
    ("c", "ц"),
    ("č", "ч"),
    ("d", "д"),
    ("е", "е"),
    ("f", "ф"),
    ("g", "г"),
    ("h", "х"),
    ("i", "и"),
    ("k", "к"),
    ("l", "л"),
    ("m", "м"),
    ("n", "н"),
    ("o", "о"),
    ("p", "п"),
    ("q", "я"),
    ("r", "р"),
    ("s", "с"),
    ("š", "ш"),
    ("t", "т"),
    ("u", "у"),
    ("v", "в"),
    ("w", "в"),
    ("x", "х"),
    ("y", "ы"),
    ("z", "з"),
    ("ž", "ж"),
    ("\'", "ь"),
    ("\"", "ъ"),
]

for find, replace in substitutions:
    cyrillic_string = re.sub(find, replace, cyrillic_string)
    
# Properly replace J
if uses_j == True:
    cyrillic_string = re.sub("j", "й", cyrillic_string)
else:
    # Ask user in vowel + и combinations which ones are really й.
    pass # Placeholder
    
corrections = [
    ("тс", "ц"), # Fix ц.
    ("цк", "тск"), # Fix some common -тс- problems.
    ("цх", "ч"),
    ("кх", "х"),
    ("сх", "ш"),
    ("зх", "ж"),
    ("шч", "щ"), # Шч cannot occur in Russian orthography.
    ("([аеиоуы])ы", "\\1й"), # Rather safe as -ыы never occurs at the end of words.
    ("[ый]у", "ю"),
    ("[ый]а", "я"),
    ("гаян", "гайан"), # E.g. Гайана
    ("(^| )ые", "\\1е"), # Only needs to activate at the beginning of words. -ые is actually quite a common grammatical ending.
    ("йе", "е"),
# Corrects spelling of words like Йемен and Йеллоунайф, and others with йе.
    ("егер", "йегер"), # Name.
    ("ейтелес", "йейтелес"), # Name.
    ("ейтс", "йейтс"), # Name.
    ("ейттелес", "йейттелес"), # Name.
    ("еллоу", "йеллоу"),
    ("емен", "йемен"),
    ("(^| )ен", "\\1йен"), # Alone, as a name.
    ("енни", "йенни"), # Name.
    ("енс", "йенс"), # Name.
    ("(^| )ети", "\\1йети"), # Monster from Nepal.
    ("еспер", "йеспер"), # Name.
    ("есс", "йесс"), # As part of a name.
    ("[ый]о", "ё"),
# Corrects spelling of words when э should be used instead of е.
    ("(^| )ето", "\\1это"), # Words like лето mess this up, so it's only changed at the beginning.
    ("(^| )ети", "\\1эти"), # Same thing here.
    ("едмонтон", "эдмонтон"), # Geographical name.
    ("ейнштейн", "эйнштейн"), # Name.
    ("еква", "эква"), # e.g. экватор
    ("експ", "эксп"), # e.g. эксперт
    ("(^| )екст", "\\1экст"), # e.g. экстремизм
    ("екзамен", "экзамен"),
    ("елаёпласт", "элайопласт"),
    ("електр", "электр"), # e.g. электричество
    ("елемент", "элемент"),
    ("енерг", "энерг"), # E.g. энергия
    ("ентроп", "энтроп"), # E.g. энтропия
    ("ерик", "эрик"), # Name.
    ("аеро", "аэро"), # Prefix.
    ("естони", "эстони"), # E.g. Эстония
    ("ефиопи", "эфиопи"), # E.g. Эфиопия
    ("етаж", "этаж"),
    ("економи", "экономи"), # E.g. экономия
    ("(^| )ерби", "\\1эрби"), # e.g. эрбий.
    ("еритр", "эритр"), # e.g. Эритрея
    ("етимологи", "этимологи"), # e.g. этимология
    ("едуард", "эдуард"), # Name.
    ("емили", "эмили"), # Name, e.g. Эмлиля
    ("реп", "рэп"),
# э will never appear after ь/ъ. The correct letter is "e".
    ("([ьъ])э", "\\1e"),
# Corrects spelling of words like район, майор, and cases with йо.
    ("аёва", "айова"), # Geographical name.
    ("баёнет", "байонет"),
    ("ваёминг", "вайоминг"), # Geographical name.
    ("ваёл", "вайол"), # E.g. вайола
    ("заён", "зайон"),
    ("коёт", "койот"),
    ("маёнез", "майонез"),
    ("маёр", "майор"),
    ("маётта", "майотта"), # Geographical name.
    ("огаё", "огайо"), # Geographical name.
    ("ораён", "орайон"),
    ("паёл", "пайол"),
    ("раён", "район"),
    ("тоёта", "тойота"),
# More instances of -йо- in a word here
    ("(^| )ёг", "\\1йог"), # At the beginning of words, e.g. йогa, йогурт. The only exceptions are minor geographical names.
    ("(^| )ёд", "\\1йод"), # As a word, not as a part of a word. мёд is an actual word, for example.
    ("ёжеф", "йожеф"), # Name.
    ("ёзеф", "йозеф"), # Name.
    ("ёрг", "йорг"), # Part of some common names. Some words start with ёрг, but they are all minor geographical names.
    ("ёрдан", "йордан"), # Name.
    ("(^| )ёрк", "\\1йорк"), # Alone, e.g. Нью Йорк. Used in a lot of words, e.g. шестёрка.
    ("ёсеф", "йосеф"), # Name.
    ("ёсиф", "йосиф"), # Name.
    ("ёта", "йота"), # Name of the Greek letter iota. Also common in words.
    ("ёун", "йоун"), # Name.
    ("ёхан", "йохан"), # Name.
    ("ёшкар", "йошкар"), # Part of a name of a city in Russia, Йошкар-Ола.
    ("ёшуа", "йошуа"), # Name.
    ("ёэ", "йоэ"), # Probably part of a name, since ёэ can never occur.
    ("([еo])во( |$)", "\\1го\\2"), # Only needs to activate at the end of words.
    ]

for find, replace in corrections:
    cyrillic_string = re.sub(find, replace, cyrillic_string)

# TODO: Check if any i/j conflicts need to be resolved
# I know that a common one is moi, which can go either way if there are no j's...

print("\"{}\" would be transliterated as:\n{}".format(latin_string, cyrillic_string))
