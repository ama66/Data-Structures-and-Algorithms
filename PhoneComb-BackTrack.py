# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.

# Example:

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

mapping = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

def combos(digits):
    
    if len(digits) == 0:
        return []

    output = []

    cur_digit = digits[0]
    
    letters = mapping[cur_digit]
    
    ## Leap of Faith here, recursion magic
    ## assume we got all possible combination from a smaller digits input 
    
    remaining_combos = combos(digits[1:])

    for i in range(len(letters)):
        letter = letters[i]

        for word in remaining_combos:
            output.append(letter + word)

        if len(remaining_combos) == 0:
            output.append(letter)

    return output

print(combos("23"))
print(combos("2389"))


['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
['adtw', 'adtx', 'adty', 'adtz', 'aduw', 'adux', 'aduy', 'aduz', 'advw', 'advx', 'advy', 'advz', 'aetw', 'aetx', 'aety', 'aetz', 'aeuw', 'aeux', 'aeuy', 'aeuz', 'aevw', 'aevx', 'aevy', 'aevz', 'aftw', 'aftx', 'afty', 'aftz', 'afuw', 'afux', 'afuy', 'afuz', 'afvw', 'afvx', 'afvy', 'afvz', 'bdtw', 'bdtx', 'bdty', 'bdtz', 'bduw', 'bdux', 'bduy', 'bduz', 'bdvw', 'bdvx', 'bdvy', 'bdvz', 'betw', 'betx', 'bety', 'betz', 'beuw', 'beux', 'beuy', 'beuz', 'bevw', 'bevx', 'bevy', 'bevz', 'bftw', 'bftx', 'bfty', 'bftz', 'bfuw', 'bfux', 'bfuy', 'bfuz', 'bfvw', 'bfvx', 'bfvy', 'bfvz', 'cdtw', 'cdtx', 'cdty', 'cdtz', 'cduw', 'cdux', 'cduy', 'cduz', 'cdvw', 'cdvx', 'cdvy', 'cdvz', 'cetw', 'cetx', 'cety', 'cetz', 'ceuw', 'ceux', 'ceuy', 'ceuz', 'cevw', 'cevx', 'cevy', 'cevz', 'cftw', 'cftx', 'cfty', 'cftz', 'cfuw', 'cfux', 'cfuy', 'cfuz', 'cfvw', 'cfvx', 'cfvy', 'cfvz']

