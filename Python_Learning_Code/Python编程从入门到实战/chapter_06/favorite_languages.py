favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'baka': 'R',
    'ehn': 'Lua',
    'CCP101': 'C++'
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

if 'erin' not in favorite_languages.keys():
    print('ERROW!')

for lan in set(favorite_languages.values()):
    print(lan.title())
