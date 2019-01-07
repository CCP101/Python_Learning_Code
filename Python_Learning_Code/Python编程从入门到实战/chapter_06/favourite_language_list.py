favorite_languages = {
    'jen': ['python', 'c'],
    'sarah': ['c'],
    'edward': ['ruby', 'sql'],
    'phil': ['python'],
    'baka': ['R', 'c'],
    'ehn': ['Lua', 'java'],
    'CCP101': ['C++', 'python']
}
for name,language in favorite_languages.items():
    print("\n"+name.title()+"`s favourite language are:")
    for i in language:
        print("\t"+i.title())