# Problem Title: Heaters
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        houses = sorted(houses)
        heaters = sorted(heaters)

        prev_heater = heaters[0]
        while j+1 < len(heaters) and heaters[j+1] <= houses[0]:
            j = j+1

            prev_heater = heaters[j]

        if j == len(heaters)-1:
            return max(abs(prev_heater-houses[0]), abs(prev_heater-houses[-1]))
        min_dist = abs(prev_heater-houses[0])
        j = j+1
        next_heater = heaters[j]
        while i < len(houses):
            while houses[i] > next_heater:
                prev_heater = next_heater
                j += 1
                if j < len(heaters):
                    next_heater = heaters[j]
                else:
                    return max(min_dist, abs(houses[-1]-heaters[-1]))
            dist = min(houses[i]-prev_heater, next_heater-houses[i])
            if dist > min_dist:
                min_dist = dist
            i += 1
        return min_dist

