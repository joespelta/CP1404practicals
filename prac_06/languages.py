from prac_06.programming_language import ProgrammingLanguage

languages = []
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
languages.append(ruby)
languages.append(python)
languages.append(visual_basic)
print(languages)
