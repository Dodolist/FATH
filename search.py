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
            consonant_arr[i] = 0
            pass
        else:
            consonant_arr[i-1] += 1
            consonant_arr[i+1] += 1
            consonant_arr[i] = 0
    elif search[i] == ' ':
        consonant_arr[i] = 4

print(vowel_arr)

print(consonant_arr)


i=0

while i<length2:
    if consonant_arr[i]==0:
        i+=1
        
    elif consonant_arr[i]==1:
        consonant_arr.insert(i+1,5)
        i+=1
        
    elif consonant_arr[i]==2:
       if consonant_arr[i+1]==2:
          if consonant_arr[i+2]==2:
              consonant_arr.insert(i+2,5)
              i+=2
            
            elif consonant_arr[i+2]==1:
                consonant_arr.insert(i+3,5)
                i+=3
                
    elif consonant_arr[i]==3:
        consonant_arr.insert(i-1,5)
        i+=1

    input_length2=len(consonant_arr)
    

print(consonant_arr)

            
    
