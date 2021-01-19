from JamoSplit import jamo_split, jamo_combine

"""
영어에서 한글로 바꾸기
"""



consonant_Korean = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ','ㄲ','ㄸ','ㅉ','ㅃ','ㅆ','ㄳ','ㄵ','ㄶ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅄ']
consonant_Alphabet=['r','s','e','f','a','q','t','d','w','c','z','x','v','g','R','E','W','Q','T','rt','sw','sg','fr','fa','fq','ft','fx','fv','fg','qt']
vowel_Korean=['ㅏ','ㅑ','ㅓ','ㅕ','ㅗ','ㅛ','ㅜ','ㅠ','ㅡ','ㅣ','ㅔ','ㅐ','ㅖ','ㅒ','ㅘ','ㅙ','ㅚ','ㅞ','ㅝ','ㅟ','ㅢ']
vowel_Alphabet=['k','i','j','u','h','y','n','b','m','l','p','o','P','O','hk','ho','hl','np','nj','nl','ml']

search = input("입력: ")
search=list(search)
#print('출력: '+search)
search_length = len(search)

vowel_arr = [0 for i in range(search_length)]
consonant_arr = [1 for i in range(search_length)]


consonant_arr_length=len(consonant_arr)



'''

이중모음 확인
in consonant_arr, 

'''

for k in range(search_length-2, -1, -1):
    if search[k] == 'h':
        if search[k+1] == 'k':
            search[k]='hk'
            del search[k+1]
            del consonant_arr[k]
            pass
        elif search[k+1] == 'o':
            search[k]='ho'
            del search[k+1]
            del consonant_arr[k]
            pass
        elif search[k+1] == 'l':
            search[k]='hl'
            del search[k+1]
            del consonant_arr[k]
            pass
    elif search[k] == 'n':
        if search[k+1] == 'p':
            search[k]='np'
            del search[k+1]
            del consonant_arr[k]
            pass
        elif search[k+1] == 'j':
            search[k]='nj'
            del search[k+1]
            del consonant_arr[k]
            pass
        elif search[k+1] == 'l':
            search[k]='nl'
            del search[k+1]
            del consonant_arr[k]
            pass
    elif search[k] == 'm':
        if search[k+1] == 'l':
            search[k]='ml'
            del search[k+1]
            del consonant_arr[k]
            search[k]
            pass

print(search)
'''
한글인지 아닌지?
'''

str_consonant_Alphabet = str(consonant_Alphabet)
str_vowel_Alphabet = str(vowel_Alphabet)

if len(search) > 6:
    for i in range(0,6,1):
        if str_consonant_Alphabet.find(search[i]) != -1 and str_consonant_Alphabet.find(search[i+1]) != -1:
            print("영어로 검색합니다.")
            break
        elif str_vowel_Alphabet.find(search[i]) != -1 and str_vowel_Alphabet.find(search[i+1]) != -1:
            print("영어로 검색합니다.")
            break
else :
    for i in range(0,len(search)-1,1):
        if str_consonant_Alphabet.find(search[i]) != -1 and str_consonant_Alphabet.find(search[i+1]) != -1:
            print("영어로 검색합니다.")
            break
        elif str_vowel_Alphabet.find(search[i]) != -1 and str_vowel_Alphabet.find(search[i+1]) != -1:
            print("영어로 검색합니다.")
            break

          

'''

in vowel_arr, 모음 자리에 1 대입

'''

search_length = len(search)
for i in range(search_length):
    if search[i] in vowel_Alphabet:
        vowel_arr[i] = 1
    pass



'''

이중받침 확인
in consonant_arr, 

'''

k=0
while k<search_length-1:
    if k+2 == search_length:
        if search[k] == 'r':
            if search[k+1] == 't':
                search[k]='rt'
                del search[k+1]
                del consonant_arr[k]
                del vowel_arr[k]
                pass
            
        elif search[k] == 's':
            if search[k+1] == 'w':
                search[k]='sw'
                del search[k+1]
                del consonant_arr[k]
                del vowel_arr[k]
                pass
            
            elif search[k+1] == 'g' :
                search[k]='sg'
                del search[k+1]
                del consonant_arr[k]
                del vowel_arr[k]
                pass
            
        elif search[k] == 'q' :
            if search[k+1] == 't':
                search[k]='qt'
                del search[k+1]
                del consonant_arr[k]
                del vowel_arr[k]
                pass

        elif search[k] == 'f':
            if search[k+1] == 'r':
                search[k]='fr'
                del search[k+1]
                del consonant_arr[k]
                del vowel_arr[k]
                pass
            
            elif search[k+1] == 'a' :
                search[k]='fa'
                del search[k+1]
                del consonant_arr[k]
                del vowel_arr[k]
                pass
            
            elif search[k+1] == 'q':
                search[k]='fq'
                del search[k+1]
                del consonant_arr[k]
                del vowel_arr[k]
                pass
            
            elif search[k+1] == 't' :
                search[k]='ft'
                del search[k+1]
                del consonant_arr[k]
                del vowel_arr[k]
                pass

            elif search[k+1] == 'x' :
                search[k]='fx'
                del search[k+1]
                del consonant_arr[k]
                del vowel_arr[k]
                pass        

            elif search[k+1] == 'v' :
                search[k]='fv'
                del search[k+1]
                del consonant_arr[k]
                del vowel_arr[k]
                pass

            elif search[k+1] == 'g' :
                search[k]='fg'
                del search[k+1]
                del consonant_arr[k]
                del vowel_arr[k]
                pass

    else:
        if vowel_arr[k+2] != 1:
            if search[k] == 'r':
                if search[k+1] == 't':
                    search[k]='rt'
                    del search[k+1]
                    del consonant_arr[k]
                    del vowel_arr[k]
                    pass
                
            elif search[k] == 's':
                if search[k+1] == 'w':
                    search[k]='sw'
                    del search[k+1]
                    del consonant_arr[k]
                    del vowel_arr[k]
                    pass
                
                elif search[k+1] == 'g' :
                    search[k]='sg'
                    del search[k+1]
                    del consonant_arr[k]
                    del vowel_arr[k]
                    pass
                
            elif search[k] == 'q' :
                if search[k+1] == 't':
                    search[k]='qt'
                    del search[k+1]
                    del consonant_arr[k]
                    del vowel_arr[k]
                    pass

            elif search[k] == 'f':
                if search[k+1] == 'r':
                    search[k]='fr'
                    del search[k+1]
                    del consonant_arr[k]
                    del vowel_arr[k]
                    pass
                
                elif search[k+1] == 'a' :
                    search[k]='fa'
                    del search[k+1]
                    del consonant_arr[k]
                    del vowel_arr[k]
                    pass
                
                elif search[k+1] == 'q':
                    search[k]='fq'
                    del search[k+1]
                    del consonant_arr[k]
                    del vowel_arr[k]
                    pass
                
                elif search[k+1] == 't' :
                    search[k]='ft'
                    del search[k+1]
                    del consonant_arr[k]
                    del vowel_arr[k]
                    pass

                elif search[k+1] == 'x' :
                    search[k]='fx'
                    del search[k+1]
                    del consonant_arr[k]
                    del vowel_arr[k]
                    pass        

                elif search[k+1] == 'v' :
                    search[k]='fv'
                    del search[k+1]
                    del consonant_arr[k]
                    del vowel_arr[k]
                    pass

                elif search[k+1] == 'g' :
                    search[k]='fg'
                    del search[k+1]
                    del consonant_arr[k]
                    del vowel_arr[k]
                    pass

    k+=1
    search_length = len(search)


search_length = len(search)


'''

in consonant_arr, 모음 기준으로 앞뒤에 +1, 띄어쓰기는 4 대입

'''

for i in range(search_length):
    if vowel_arr[i] == 1:
        if i==search_length-1:
            consonant_arr[i-1] += 1
            pass
        else:
            consonant_arr[i-1] += 1
            consonant_arr[i+1] += 1
    elif search[i] == ' ':
        consonant_arr[i] = 4

'''

in consonant_arr, 모음 자리에 0 대입

'''

for i in range(search_length):
    if vowel_arr[i] == 1:
        consonant_arr[i] = 0


'''

in consonant_arr, 글자 끊어지는 부분마다 5 대입

'''

i=0
consonant_arr_length=len(consonant_arr)
search_length = len(search)

while i < consonant_arr_length:
    if consonant_arr[i] == 2:
        if i+2 != consonant_arr_length:
            if consonant_arr[i+2] == 2:
                if i+3 != consonant_arr_length:
##                    if consonant_arr[i+3] == 1:
##                        #consonant_arr.insert(i+4,5)
##                        i+=4
##                        pass
                    if consonant_arr[i+3] == 2:
                        #consonant_arr.insert(i+3,5)
                        i+=3
                        pass
                    elif consonant_arr[i+3] == 3:
                        #consonant_arr.insert(i+3,5)
                        i+=3
                        pass
                    elif consonant_arr[i+3] == 4:
                        i+=3
                        pass
                    pass
                else:
                    #consonant_arr.insert(i+3,5)
                    i+=3
                    pass
            elif consonant_arr[i+2] == 3:
                consonant_arr.insert(i+2,5)
                i+=3
                pass
            elif consonant_arr[i+2] == 4:
                consonant_arr.insert(i+2,5)
                i+=2
                pass
        else:
            consonant_arr.insert(i+2,5)
            i+=3
    elif consonant_arr[i] == 3:
        if i+2 != consonant_arr_length:
            if consonant_arr[i+2] == 2:
                if i+3 != consonant_arr_length:
##                    if consonant_arr[i+3] == 1:
##                        #consonant_arr.insert(i+4,5)
##                        i+=4
##                        pass
                    if consonant_arr[i+3] == 2:
                        #consonant_arr.insert(i+3,5)
                        i+=3
                    elif consonant_arr[i+3] == 3:
                        #consonant_arr.insert(i+3,5)
                        i+=3
                        pass
                    elif consonant_arr[i+3] == 4:
                        i+=3
                        pass
                else:
                    #consonant_arr.insert(i+3,5)
                    i+=3
                    pass
            elif consonant_arr[i+2] == 3:
                consonant_arr.insert(i+2,5)
                i+=3
                pass
            elif consonant_arr[i+2] == 4:
                consonant_arr.insert(i+2,5)
                i+=3
                pass
        else:
            consonant_arr.insert(i+2,5)
            i+=3
    elif consonant_arr[i] == 0:
        #consonant_arr.insert(i+1,5)
        i+=2
        pass
    elif consonant_arr[i] == 4:
        i+=1
        pass
    else:
        i+=1
        
    consonant_arr_length=len(consonant_arr)

##    print(consonant_arr)
##    print(consonant_arr_length)
##    print(i)


'''

자음 바꾸기

'''
for i in range(search_length):
     for k in range(len(consonant_Alphabet)):
        if search[i]==consonant_Alphabet[k]:
            search[i] = consonant_Korean[k]
            #search=search.replace(search[i],consonant_Korean[k])
            pass



'''

모음 바꾸기 

'''
for i in range(search_length):
    for k in range(len(vowel_Alphabet)):
        if search[i]==vowel_Alphabet[k]:
            search[i] = vowel_Korean[k]
            #search=search.replace(search[i],vowel_Korean[k])
            pass

'''

underbar 추가

'''

for i in range(consonant_arr_length):
    if consonant_arr[i] == 5:
        search.insert(i,'_')


'''
print

'''

print(jamo_combine(search))

