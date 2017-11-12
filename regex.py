import re
print(re.search(r'e', 'eucaliptoeucalicto'))

pattern_number = re.compile('\d\d')
print(pattern_number.search('affafafa22fafaf33'))

pattern_uppercase = re.compile('[A-Z]\d')
print(pattern_uppercase.search('afafafafaAFAFFA4'))

t = re.search('[A-Z][0-9].*$', 'afafaf AF1afa afafa')
if (t):
    print('Se encontró [A-Z][0-9].*$', t)

print(re.sub(r'\d', '-', 'la2notica3de6hoy#@LR'))
