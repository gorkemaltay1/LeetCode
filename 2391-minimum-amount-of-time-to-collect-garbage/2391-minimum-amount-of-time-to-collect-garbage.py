class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        paperTime = 0
        metalTime = 0
        garbageTime = 0
        for index, item in enumerate(reversed(garbage)):
            if "P" in item:
                paperTime += sum(travel[:len(garbage) - index - 1])
                break
        for index, item in enumerate(reversed(garbage)):
            if "G" in item:
                garbageTime += sum(travel[:len(garbage) - index - 1])
                break
        for index, item in enumerate(reversed(garbage)):
            if "M" in item:
                metalTime += sum(travel[:len(garbage) - index - 1])
                break
        
        for i in garbage:
                if "P" in i:
                    paperTime += i.count("P")
                if "M" in i:
                    metalTime += i.count("M")
                if "G" in i:
                    garbageTime += i.count("G")
        return paperTime+metalTime+garbageTime
            