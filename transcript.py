import search

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
            search[i]=consonantKorean[k]
            k+=1
            pass
     i+=1


print(search)
     
