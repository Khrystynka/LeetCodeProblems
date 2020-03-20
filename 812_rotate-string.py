# Problem Title: Rotate String
'''class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool"""
# Rabin Karpp alorithm - Rolling hash
        self.p=101
        self.k=10**7
        n=len(A)
        A=A+A
        if len(B)!=n:
            return False
        def new_hash(s,start,end,prev_hash=None,ind_remove=None,ind_add=None):
            hash_val=0
            if not prev_hash:
                for i in range(0,(end-start)+1):
                    hash_val+=ord(s[start+i])*(self.p**i)
            else:
                
                hash_val=(prev_hash-ord(s[ind_remove]))/self.p+ord(s[ind_add])*(self.p**(n-1))
            return hash_val #% self.k
        hash_txt=new_hash(A,0,n-1)
        hash_pattern=new_hash(B,0,n-1)
        if hash_txt==hash_pattern:
                return True
            
        for i in range(1,n):
            hash_txt=new_hash(A,i,i+n-1,hash_txt,i-1,i+n)
            print hash_txt,hash_pattern
            if abs(hash_txt-hash_pattern)<=1 :
                print A[i:i+n],B
                return True
            
        return False'''


class Solution:
    def rotateString(self, A, B):

        trial = 0

        # comparing hash is much more efficient
        while hash(A) != hash(B) and trial != len(B):

            # don't you love python sometimes
            temp_char = B[-1]
            B = B[:-1]
            B = temp_char + B
            trial += 1

        return hash(A) == hash(B) and A == B

