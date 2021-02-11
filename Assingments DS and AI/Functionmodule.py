#1
def count_letter_spacing(string_para):
    '''count the letters with the spacing'''
    length=len(string_para)
    print('string length  :',length)
    
#2    
def count_words(string_para):
    '''count the words'''
    f_str=string_para.split()
    totalwords=len(f_str)
    print('number of words used in the paragraph:',totalwords)
    
#3  
def count_letter(string_para):
    '''count the letters without spacing'''
    spacing = ' '
    count = 0 
    for i in string_para:
        if i is not spacing:
            count = count + 1
    print('number of letter used in the paragraph:' , count)
            
    
#4                            
def count_spacing(string_para):
    '''count space in paragraph'''
    count=0
    spacing = ' '
    for para in string_para:
        if spacing is para:
            count=count+1
    print('the spacing used:',str(count))

    
#5    
def count_punctuation(string_para):
    '''count the punctuations 
    Enter the string in replacement of string_para'''
    count=0
    punct=['.','?',':',',',';','!','-','_']
    for string in string_para:
        if string in punct:
            count = count+1
    print('number of punctuations used in the paragraph:' , count)


    
    
    
#6
def count_extract_punctuation(string_para):
    '''count the punctuations 
    Enter the string in replacement of string_para'''
    count=0
    punct=['.','?',':',',',';','!','-','_']
    newstring=''
    for string in string_para:
        if string not in punct:
            newstring=newstring+string
    print(f"{newstring}")

    
    
    
    
    
    
    
    
    
    
    
    
    
     