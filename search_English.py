from JamoSplit import jamo_split, jamo_combine


"""
한글에서 영어로 바꾸기
"""



consonant_Korean = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ','ㄲ','ㄸ','ㅉ','ㅃ','ㅆ','ㄳ','ㄵ','ㄶ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅄ']
consonant_Alphabet=['r','s','e','f','a','q','t','d','w','c','z','x','v','g','R','E','W','Q','T','rt','sw','sg','fr','fa','fq','ft','fx','fv','fg','qt']
vowel_Korean=['ㅏ','ㅑ','ㅓ','ㅕ','ㅗ','ㅛ','ㅜ','ㅠ','ㅡ','ㅣ','ㅔ','ㅐ','ㅖ','ㅒ','ㅘ','ㅙ','ㅚ','ㅞ','ㅝ','ㅟ','ㅢ']
vowel_Alphabet=['k','i','j','u','h','y','n','b','m','l','p','o','P','O','hk','ho','hl','np','nj','nl','ml']

search=input('입력:')
finds=list(search)
finds=jamo_split(finds)
finds=list(finds)

'''
자음 바꾸기
'''
for i in range(len(finds)):
    for k in range(len(consonant_Korean)):
       if finds[i]==consonant_Korean[k]:
            finds[i] = consonant_Alphabet[k]
            #search=search.replace(search[i],consonant_Alphabet[k])
            pass

'''
모음 바꾸기 
'''
for i in range(len(finds)):
    for k in range(len(vowel_Korean)):
       if finds[i]==vowel_Korean[k]:
            finds[i] = vowel_Alphabet[k]
            #search=search.replace(search[i],vowel_Alphabet[k])
            pass

'''
Delete Underbar
'''

for i in range(len(finds)) :
    if finds[i] == '_' :
        finds[i] = ''
        pass

'''
Print
'''
print(jamo_combine(finds))






