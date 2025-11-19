file = open('data.txt')#default mode is read
word_list = file.read().lower().split()
word_list_cleaned = [item.replace('.', '').replace(',', '') for item in word_list]

# for item in word_list:
#   cleaned_item = item.replace('.','').replace(',','') 
#   word_list_cleaned.append(cleaned_item)
#reading the file
freq_dict = {}
for word in word_list_cleaned:
  if word in freq_dict:
    freq_dict[word] += 1
  else:
    freq_dict[word] = 1

sorted_words = sorted(freq_dict.items(),key=lambda x:x[1],reverse=True)
print(sorted_words)

