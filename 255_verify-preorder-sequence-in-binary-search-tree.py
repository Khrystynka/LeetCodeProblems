# Problem Title: Verify Preorder Sequence in Binary Search Tree
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        '''def verify(sublist,start,end,min_el=float('-inf'),max_el=float('inf')):
            #print start,end
            if start>=end:
                return True
            root=sublist[start]
            i=start+1
            while i<=end  and sublist[i]<root and sublist[i]<max_el and sublist[i]>min_el:
                i+=1
            for j in range(i,end+1):
                if sublist[j]<root or sublist[i]>max_el or sublist[i]<min_el:
                    return False
            return verify(sublist,start+1,i-1,min_el,root) and verify(sublist,i,end,root,max_el) 
        return verify(preorder,0,len(preorder)-1)'''

        stack1 = []
        last_el = None
        for node in preorder:
            if stack1 == [] or node < stack1[-1]:
                stack1.append(node)
            else:
                while stack1 != [] and node > stack1[-1]:
                    popped_node = stack1.pop()
                    if last_el and last_el > popped_node:
                        return False
                    last_el = popped_node
                stack1.append(node)
        if stack1 == [] or not last_el:
            return True
        return stack1[-1] > last_el

