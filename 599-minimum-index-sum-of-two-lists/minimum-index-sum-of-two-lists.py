class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashmap = {}
        maxind = len(list1) + len(list2)
        final = []
        for i in range(len(list1)):
            hashmap[list1[i]] = i
        for j in range(len(list2)):
            if list2[j] in hashmap:
                if hashmap[list2[j]]+j < maxind:
                    final.clear()
                    final.append(list2[j])
                    maxind = hashmap[list2[j]]+j
                if hashmap[list2[j]]+j == maxind and list2[j] not in final:
                    final.append(list2[j])
        return final