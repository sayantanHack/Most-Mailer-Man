'''
f_handle=raw_input("File name.format")   #use input for python 3 
file_read = f_handle.open()
'''

file_read = open('Info.txt')
count = {}        #making an empty dictionary
word_list =[]

for line in file_read:
    if not line.startswith("From") or line.startswith('From:'):continue
    words = line.split()
    word_list.append(words[1])
for word in word_list:
    count[word] = count.get(word , 0) + 1    #selecting the common mails & counting the numbers.
    
#selecting the most used mail id.
    
bigkey = None
bigvalue = 0
for keyword , valueword in count.items():
    if bigkey is None or bigvalue < valueword:
        bigkey = keyword
        bigvalue = valueword


print 'The mailed person', bigkey,', sent ',bigvalue,'mails.'   # use parenthesis() after print if you are using python 3.
