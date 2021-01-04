from JamoSplit import jamo_split, jamo_combine

vowelAlphabet=['k','i','j','u','h','y','n','b','m','l','p','o','P','O']

search = input("검색창: ")

print('출력: '+search)

input_length = len(search)

vowel_arr = [0 for i in range(input_length)]
consonant_arr = [1 for i in range(input_length)]

for i in range(input_length):
    if search[i] in vowelAlphabet:
        vowel_arr[i] = 1
    pass

for i in range(input_length):
    if vowel_arr[i] == 1:
        if i==input_length-1:
            consonant_arr[i-1] += 1
            pass
        else:
            consonant_arr[i-1] += 1
            consonant_arr[i+1] += 1
    elif search[i] == ' ':
        consonant_arr[i] = 4

for i in range(input_length):
    if vowel_arr[i] == 1:
        consonant_arr[i] = 0

print(vowel_arr)
print(consonant_arr)

i=0
input_length2=len(consonant_arr)

while i<input_length2:
    if consonant_arr[i] == 2:
        if i+2 != input_length2:
            if consonant_arr[i+2] == 0:
                consonant_arr.insert(i+3,5)
                i+=3
            elif consonant_arr[i+2] == 2:
                if i+3 != input_length2:
                    if consonant_arr[i+3] == 1:
                        #consonant_arr.insert(i+4,5)
                        i+=4
                        pass
                    elif consonant_arr[i+3] == 2:
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
                i+=3
                pass
        else:
            consonant_arr.insert(i+2,5)
            i+=3
            
    elif consonant_arr[i] == 3:
        if i+2 != input_length2:
            if consonant_arr[i+2] == 2:
                if i+3 != input_length2:
                    if consonant_arr[i+3] == 1:
                        #consonant_arr.insert(i+4,5)
                        i+=4
                        pass
                    elif consonant_arr[i+3] == 2:
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
        consonant_arr.insert(i+1,5)
        i+=2
        pass
    elif consonant_arr[i] == 4:
        i+=2
        pass
    else:
        i+=1
    input_length2=len(consonant_arr)

    print(consonant_arr)




















q='ㅂ'
w='ㅈ'
e='ㄷ'
r='ㄱ'
t='ㅅ'
y='ㅛ'
u='ㅕ'
i='ㅑ'
o='ㅐ'
p='ㅔ'

a='ㅁ'
s='ㄴ'
d='ㅇ'
f='ㄹ'
g='ㅎ'
h='ㅗ'
j='ㅓ'
k='ㅏ'
l='ㅣ'
z='ㅋ'
x='ㅌ'
c='ㅊ'
v='ㅍ'
b='ㅠ'
n='ㅜ'
m='ㅡ'

consonantKorean = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ','ㄲ','ㄸ','ㅉ','ㅃ','ㅆ']
consonantAlphabet=['r','s','e','f','a','q','t','d','w','c','z','x','v','g','R','E','W','Q','T']


vowelKorean=['ㅏ','ㅑ','ㅓ','ㅕ','ㅗ','ㅛ','ㅜ','ㅠ','ㅡ','ㅣ','ㅔ','ㅐ','ㅖ','ㅒ']

vowelAlphabet=['k','i','j','u','h','y','n','b','m','l','p','o','P','O']

i=0
k=0
input_length3=len(consonantAlphabet)


for i in range(input_length):
     for k in range(input_length3):
        if search[i]==consonantAlphabet[k]:
            search=search.replace(search[i],consonantKorean[k])
            pass


input_length4=len(vowelAlphabet)

for i in range(input_length):
    for k in range(input_length4):
        if search[i]==vowelAlphabet[k]:
            search=search.replace(search[i],vowelKorean[k])
            pass

search=list(search)

for i in range(input_length2):
    if consonant_arr[i] == 5:   
        search.insert(i,'_')



print(search)
print(jamo_combine(search))

