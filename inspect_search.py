consonant_Korean = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ','ㄲ','ㄸ','ㅉ','ㅃ','ㅆ','ㄳ','ㄵ','ㄶ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅄ']
consonant_Alphabet=['r','s','e','f','a','q','t','d','w','c','z','x','v','g','R','E','W','Q','T','rt','sw','sg','fr','fa','fq','ft','fx','fv','fg','qt']
vowel_Korean=['ㅏ','ㅑ','ㅓ','ㅕ','ㅗ','ㅛ','ㅜ','ㅠ','ㅡ','ㅣ','ㅔ','ㅐ','ㅖ','ㅒ','ㅘ','ㅙ','ㅚ','ㅞ','ㅝ','ㅟ','ㅢ']
vowel_Alphabet=['k','i','j','u','h','y','n','b','m','l','p','o','P','O','hk','ho','hl','np','nj','nl','ml']


def inspect_search_function(list):
    
    str_consonant_Alphabet = str(consonant_Alphabet)
    str_vowel_Alphabet = str(vowel_Alphabet)


    if len(list) == 1 or len(list) == 0:
        return 0

    else :
        if str_vowel_Alphabet.find(list[0]) != -1 :
            #print("영어로 검색합니다.")
            return 0
        elif str_consonant_Alphabet.find(list[0]) != -1 and str_consonant_Alphabet.find(list[1]) != -1:
            #print("영어로 검색합니다.")
            return 0
        for i in range(0,len(list)-1,1):
            if  (list[i] != ' ' and list[i+1] != ' ') and str_vowel_Alphabet.find(list[i]) != -1 and str_vowel_Alphabet.find(list[i+1]) != -1:
                #print("영어로 검색합니다.")
                return 0
            
    return 1
