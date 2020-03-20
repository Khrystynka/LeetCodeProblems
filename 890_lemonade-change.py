# Problem Title: Lemonade Change
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        d = {5: 0, 10: 0, 15: 0, 20: 0}
        change_req = []
        for bill in bills:
            change = bill - 5
            d[bill] += 1
            if change == 15:
                if d[change] > 0:
                    d[change] -= 1
                elif d[10] > 0 and d[5] > 0:
                    d[10] -= 1
                    d[5] -= 1
                elif d[5] > 3:
                    d[5] -= 3
                else:
                    return False
            elif change == 10:
                if d[10] > 0:
                    d[10] -= 1

                elif d[5] > 2:
                    d[5] -= 2
                else:
                    False

            elif change == 5:
                if d[change] > 0:
                    d[change] -= 1

                else:
                    return False

        return True

