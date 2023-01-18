class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            ruleKey = 0
        if ruleKey == "color":
            ruleKey = 1
        if ruleKey == "name":
            ruleKey = 2
            
        count = 0
        for i in items:
            if i[ruleKey]==ruleValue:
                count += 1
        return count