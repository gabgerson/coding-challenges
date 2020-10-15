def strip_punct(sen):
    new_s = ''
    p = {'!','@','#','$','%','^','&','*','(',')', '/',':', '[', ']'}
    for char in sen:
        if char not in p:
            new_s += char
    sen = new_s
    return sen

def LongestWord(sen):
    sen = strip_punct(sen) 
    
    sen_ls = sen.split()
    max_word = sen_ls[0]
    for word in sen_ls:

      if len(max_word) < len(word):
          max_word = word

  
  # code goes here
    return max_word

# keep this function call here 
print(LongestWord(input()))