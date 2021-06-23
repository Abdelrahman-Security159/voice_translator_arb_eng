import dectionary_words as dw
#import arabic_reshaper as ar


class Translate():
    list_of_results = []
    list_of_transls = []
    talk_to_flag = 'bro'
    talker_flag  = 'أ'                                              # Checking from who is talking
    your_flag    = ''
    preposition  = 'i'                                             # After che
    char = ''
    word_curbus = ''
    translate_type = ''
    
    def __init__(self):
        dectionary_word = dw
    
    def search(self, word_list):                                    # Hello bro I need help
        for word in word_list:                                      
            self.list_of_results.append(word)                       # [hello, bro, i, need, help]
            
        looper = 0
        while looper < len(self.list_of_results) :                  # [hello, bro, i, need, help]
            
            self.char = self.list_of_results[looper][0]             # [h    , b  , i, n   , h   ]
            self.list_of_transls.append(dw.curbus[self.char][self.list_of_results[looper]])       # [c_h  , c_b, c_i, c_n, c_h]
            type_of_word = str(type(self.list_of_transls[looper]))
            
            if type_of_word.split("'")[1] == "dict": #<type 'str'>
                if self.list_of_transls[looper]["id"] == "name":
                    self.talk_to_flag = self.list_of_results[looper]
                    self.list_of_transls[looper] = dw.name[self.list_of_results[looper]]
                    
                elif self.list_of_transls[looper]["id"] == "pp":
                    self.preposition = self.list_of_results[looper]
                    self.talker_flag = dw.talker[self.list_of_results[looper]]
                    if self.talker_flag == 'P':
                        self.talker_flag = "ون"
                        self.list_of_transls[looper] = "هم"
                    else:
                        self.list_of_transls[looper] = dw.pp[self.list_of_results[looper]]
                    
                elif self.list_of_transls[looper]["id"] == "verb":
                    if self.talker_flag == 'ون':
                        self.list_of_transls[looper] = 'ي' + dw.verb[self.list_of_results[looper]] + self.talker_flag
                    else:
                        self.list_of_transls[looper] = self.talker_flag + dw.verb[self.list_of_results[looper]]

                elif self.list_of_transls[looper]["id"] == "your":
                    self.your_flag = dw.your[self.talk_to_flag]
                    self.list_of_transls[looper] = ''
                    
                elif self.list_of_transls[looper]["id"] == "you":
                    if self.list_of_results[looper + 1] == "are":
                        self.list_of_transls[looper] = "أن" + dw.you_are[self.talk_to_flag]
                    else:
                        self.list_of_transls[looper] = dw.you[self.talk_to_flag]
                    
                elif self.list_of_transls[looper]["id"] == "adj":
                    self.list_of_transls[looper] = self.list_of_transls[looper][self.list_of_results[looper]] + dw.adj_kind[self.talk_to_flag]
                
            else:
                if self.list_of_transls[looper] == "":
                    if self.list_of_results[looper + 1] == "you":
                        self.list_of_transls[looper] = "حال"
                else:
                    self.list_of_transls[looper] += self.your_flag
                    self.your_flag = ''
            looper += 1
        
        for i in self.list_of_transls:
            print(i, end=' ')
            
            
            
    