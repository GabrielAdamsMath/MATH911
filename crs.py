
global ruleCount
ruleCount = 11


r0 = "aa"
r1 = "bb"
r2 = "cc"
r3 = "abab"
r4 = "acacacac"
r5 = "bcbcbcbc"
r6 = "bab"
r7 = "cacacac"
r8 = "cbcbcbc"
r9 = "acacaca"
r10 = "bcbcbcb"

rules = [r0,r1,r2,r3,r4,r5,r6]

def ApplyRule(ruleNo,word):
    if ruleNo ==0:
        old = word
        word = word.replace("aa","")
        if old == word :
            return False
        
    if ruleNo == 1:
        old = word
        word = word.replace("bb","")
        if old == word :
            return False
        
    if ruleNo == 2:
        old = word
        word = word.replace("cc","")
        if old == word :
            return False
        
    if ruleNo ==3:
        old = word
        word = word.replace("abab","")
        if old == word :
            return False
    
    if ruleNo == 4:
        old = word
        word = word.replace("acacacac","")
        if old == word :
            return False
        
    if ruleNo == 5:
        old = word
        word = word.replace("bcbcbcbc","")
        if old == word :
            return False
    
    if ruleNo == 6:
        old = word
        word = word.replace("ba","ab")
        if old == word :
            return False
        
    if ruleNo == 7:
        old = word
        word = word.replace("cacacac","a")
        if old == word :
            return False
        
    if ruleNo == 8:
        old = word
        word = word.replace("cbcbcbc","b")
        if old == word :
            return False

    if ruleNo == 9:
        old = word
        word = word.replace("acacaca","c")
        if old == word :
            return False
        
    if ruleNo == 10:
        old = word
        word = word.replace("bcbcbcb","c")
        if old == word :
            return False

    return word

def isPrefixOf(rule1, rule2):
    for i in range(len(rule1)):
        if rule2.startswith(rule1[0+i:]):
            return (rule1,rule2)
    return False

def wherePrefix(rule1,rule2):
    for i in range(len(rule1)):
        if rule2.startswith(rule1[0+i:]):
            return i
    return False

def findPairs(rules):
    pairs = []
    for i in rules:
        for j in rules:


            if i == j:
                continue
            
            result = isPrefixOf(i,j)
            
            if result:
                pairs.append(result)
    return pairs


def applyTillFail(word,ruleAmount):

    failCount = 0
    while(failCount != ruleAmount):
        for i in range(ruleAmount):
            new = True
            new = ApplyRule(i,word)
            #print("Checking:" + word + " With rule" + str(i))
            if new == False and new != "":
                failCount = failCount + 1
               # print(failCount)
            elif new == "":
                word = new
                return word
            else:
                word = new
                failCount = 0

        if failCount != ruleAmount:
            failCount = 0
    return word


def checkPair(pair,rules):

    loc = wherePrefix(pair[0],pair[1])
    combined = (pair[0])[:loc] + (pair[1])


    leftRight = ApplyRule(rules.index(pair[0]),combined)
    leftRight = applyTillFail(leftRight,ruleCount)


    rightLeft = ApplyRule(rules.index(pair[1]),combined)
    rightLeft = applyTillFail(rightLeft,ruleCount)

    result = (leftRight,rightLeft)
    return result
print(ApplyRule(1,"aab"))

#isPrefixOf(r1,r4)

pairs = findPairs(rules)
print(pairs)
#print(checkPair(pairs[0],rules))

print(applyTillFail("a",ruleCount))
#Check all the pairs


bad = []
for i in pairs:
    pair = checkPair(i,rules)
    if pair[0] != pair [1] and pair[0] != "":
        bad.append(pair)
        bad.append(rules.index(i[0]))
        bad.append(rules.index(i[1]))

#After 1st run bab = a. Added this rule 6
#After 2nd run ab=ba. Changed rule 6 ba->ab
#After 3rd run cacacac = a. Added this rule 7
#After 4th run cbcbcbc = b Added this rule 8
#After 5th run acacaca = c Added this rule 9
#After 6th run bcbcbcb = c Added this rule 10
#After 7th run, no more non-confluent critical pairs

print(bad)