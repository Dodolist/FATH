from JamoSplit import jamo_split, jamo_combine
from inspect_search import consonant_Alphabet, consonant_Korean, vowel_Alphabet, vowel_Korean


"""
한글에서 영어로 바꾸기
"""

def From_Hangul_To_Alphabet(list):
    finds=jamo_split(list)
    
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

    for i in finds :
        if i == '_' :
            finds.remove('_')
            pass

    '''
    Print
    '''
    print(jamo_combine(finds))






