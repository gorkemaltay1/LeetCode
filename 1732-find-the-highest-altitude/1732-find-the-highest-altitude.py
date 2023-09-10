class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        point = 0
        for i in gain:
            point += i
            altitudes.append(point)
        return max(altitudes)