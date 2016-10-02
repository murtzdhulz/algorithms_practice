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
    def word_break_DP(self, input_str, lookup, answer, cache):
        # print input_str
        # print cache
        if len(input_str)==0:
            print answer
            return True

        if input_str in cache:
            print "Cache Hit"
            return False

        cur_word=""

        for i in xrange(len(input_str)):
            # print cur_word
            cur_word+=input_str[i]
            if cur_word in lookup and self.word_break_DP(input_str[i+1:],lookup,answer+cur_word+" ",cache):
                return True

        # print 'Coming here'
        cache.add(input_str)
        # print 'Return False'
        return False

input_string = "playhardandpartyharderbuddy"
dictionary = ["hardest","hard","too","bro","dude","buddy","harder","party","play","hello","and","a","pl","bu","ha"]
cache=set()
wb = WordBreak()
wb.word_break_backtrack(input_string,dictionary,"")
wb.word_break_DP(input_string,dictionary,"",cache)