# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 02:30:57 2017

@author: SAHAJA
"""
import hashlib

def convert(text):
    l = text.lower().split()
    add = []


    def correct(l):
        if (add[1] == 0):
            if (l[1] == "you" and (l[2] == "eat" or l[2] == "go")):
                l.insert(1, "do")
            elif ((l[1] == "you" or l[1] == "they") and (l[2] == "eating" or l[2] == "going")):
                l.insert(1, "are")
            elif ((l[1] == "i" or l[1] == "they") and (l[2] == "eat" or l[2] == "go")):
                l.insert(1, "do")
            elif (l[1] == "i" and (l[2] == "eating" or l[2] == "going")):
                l.insert(1, "am")
            elif ((l[1] == "he" or l[1] == "she") and (l[2] == "eat" or l[2] == "go")):
                l.insert(1, "does")
            elif ((l[1] == "he" or l[1] == "she") and (l[2] == "eating" or l[2] == "going")):
                l.insert(1, "is")
            elif ((l[1] == "he" or l[1] == "she") and (l[2] == "today")):
                l.insert(1, "is")
            elif ((l[1] == "he" or l[1] == "she") and (l[2] == "yesterday")):
                l.insert(1, "was")
            elif ((l[1] == "you") and (l[2] == "today")):
                l.insert(1, "are")
            elif ((l[1] == "you") and (l[2] == "yesterday")):
                l.insert(1, "were")

            return l


    def isQuestion(l):
        q = ["who", "where", "what", "why", "when", "how", "which", "whom"]
        z = []
        c = 0
        for word in l:
            if (word in q):
                #            print("found ",word)
                z.append(word)
                c += 1
        if (c > 0):
            add.append(1)
            return z
        else:
            add.append(0)
            return False


    z = isQuestion(l)


    # print(z)


    def helpVerb(l):
        hp = ["is", "am", "are", "was", "were", "be", "been", "being", "has", "have", "had", "does", "do", "did", "can",
              "will", "shall", "could", "would", "should", "must", "may", "might"]
        c = 0
        for word in l:
            if (word in hp):
                #            print("found ",word)
                z.append(word)
                c += 1
        if (c > 0):
            add.append(1)
            return z
        else:
            add.append(0)
            return False


    z1 = helpVerb(l)


    # print(z1)

    def isPronoun(l):
        pn = ["i", "we", "you", "she", "he", "it", "they", "them", "his", "her", "me"]
        c = 0
        for word in l:
            if (word in pn):
                #            print("found ",word)
                z.append(word)
                c += 1
        if (c > 0):
            add.append(1)
            return z
        else:
            add.append(0)
            return False


    z2 = isPronoun(l)


    # print(z2)

    def isVerb(l):
        vv = ["go", "eat", "going", "eating", "sleeping", "read", "walk"]
        c = 0
        for word in l:
            if (word in vv):
                #            print("found ",word)
                z.append(word)
                c += 1
        if (c > 0):
            add.append(1)
            return z
        else:
            add.append(0)
            return False


    z3 = isVerb(l)


    # print(z3)
    # print(add)


    def checkDay(l):
        days = ["yesterday", "today", "tomorrow"]
        c = 0
        for word in l:
            if (word in days):
                #            print("found ",word)
                z.append(word)
                c += 1
        if (c > 0):
            add.append(1)
            return z
        else:
            add.append(0)
            return False


    z4 = checkDay(l)
    # print(z4)
    # print(add)
    if (z4 != False):
        z4c = correct(z4)
        string = ' '.join(map(str, z4c))
        # print("corrected >", string)
        return string
    elif (z3 != False):
        z3c = correct(z3)
        string = ' '.join(map(str, z3c))
        # print("corrected >", string)
        return string
    else:
        string = ' '.join(map(str, z2))
        # print("corrected >", string)
        return string






