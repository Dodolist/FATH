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

        
