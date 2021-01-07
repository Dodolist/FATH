

"""
한글에서 영어로 바꾸기

"""


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

if finds[i] in consonant_Alphabet or finds[i] in vowel_Alphabet:
    print(jamo_combine(search))

elif finds[i] in consonant_Korean or finds[i] in vowel_Korean:
    print(finds)
