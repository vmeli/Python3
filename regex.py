import re
#print(re.search(r'e', 'eucaliptoeucalicto'))
pattern_number = re.compile('\d\d')
#print(pattern.search('affafafa22fafaf33'))

pattern_uppercase = re.compile('[A-Z]\d')
print(pattern_uppercase.search('afafafafaAFAFFA4'))