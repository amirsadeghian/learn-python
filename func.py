def hello(lang, name):
    if lang == 'EN' or lang == 'en':
        out = 'Hello ' + name
    elif lang == 'ES' or lang == 'es':
        out = 'Ola ' + name
    else:
        out = 'Hello ' + name
    return out
output = hello('EN','Amir')
print(output)
quit()