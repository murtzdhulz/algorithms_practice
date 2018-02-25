class WordBreak:
    def word_break_backtrack(self, input_str, lookup, answer):
        if len(input_str)==0:
            print answer
            return True

        cur_word=""

        for i in xrange(len(input_str)):
            # print cur_word
            cur_word+=input_str[i]
            if cur_word in lookup and self.word_break_backtrack(input_str[i+1:],lookup,answer+cur_word+" "):
                return True

        return False

    # Doesn't seem to work well
    # def word_break_DP(self, input_str, lookup, answer, cache):
    #     # print input_str
    #     # print cache
    #     if len(input_str)==0:
    #         print answer
    #         return True
    #
    #     if input_str in cache:
    #         print "Cache Hit"
    #         return False
    #
    #     cur_word=""
    #
    #     for i in xrange(len(input_str)):
    #         # print cur_word
    #         cur_word+=input_str[i]
    #         if cur_word in lookup and self.word_break_DP(input_str[i+1:],lookup,answer+cur_word+" ",cache):
    #             return True
    #
    #     # print 'Coming here'
    #     cache.add(input_str)
    #     # print 'Return False'
    #     return False

    def word_break(self, s, word_dict):
        f = [False]*(len(s)+1)
        f[0] = True

        for i in xrange(1,len(s)+1):
            for j in xrange(i):
                if f[j] and s[j:i] in word_dict:
                    f[i] = True
                    break
        return f[len(s)]

input_string = "playhardandpartyharderbuddy"
dictionary = ["hardest","hard","too","bro","dude","buddy","harder","party","play","hello","and","a","pl","bu","ha"]
# cache=set()
wb = WordBreak()
# wb.word_break_backtrack(input_string,dictionary,"")
# wb.word_break_DP(input_string,dictionary,"",cache)

print wb.word_break(input_string,dictionary)

