class StringManipulation:
    def __init__(self,words):
        self.words = words
        
    def total_words(self):
        return len(self.words)
    
    def count(self,some_word):
        return self.words.count(some_word)
        
    def words_of_length(self,length):
        l=[]
        for each in self.words :
            if(len(each) == length):
                l.append(each)
        return l
        
    def words_start_with(self,char):
        x=len(char)
        f=True
        l=[]
        for each in self.words:
            for i in range(x):
                if(each[i]==char[i]):
                    l.append(each)
        return l
        
    def longest_word(self):
        s=''
        max=len(self.words[0])
        for each in self.words:
            if(len(each)>max):
                max=len(each)
                s=each
        return s
        
    def palindromes(self):
        l=[]
        for each in self.words:
            if(each==each[::-1]):
                l.append(each)
        return l