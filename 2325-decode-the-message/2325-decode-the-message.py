from collections import OrderedDict
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        keyDict = {" ":" "}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        finalMessage =""
        keyList= list(OrderedDict.fromkeys(key))
        if " " in keyList:
            keyList.pop(keyList.index(" "))
        for i in keyList:
            keyDict[i] = alphabet[keyList.index(i)]
        for i in message:
            if i != " ":
                finalMessage = finalMessage + keyDict[i]
            else:
                finalMessage += " "
        return finalMessage
                
            
            