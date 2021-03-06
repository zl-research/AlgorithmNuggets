class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        
        # 100pass -Proper short smart thinking soltuion - reverse the string and operate
        
        # Remove all the "-" and reverse the string
        S = S.replace("-","")[::-1]
        
        # Split string based on the length
        result = []
        for i in range(0,len(S),K):
            result.append(S[i:i+K].upper())
        return "-".join(result)[::-1]
            
        
        
        """
        # logic missing for initial key0 calculation with proper formatting of remaining string
        
        import re
        
        # String split by -
        keys = S.split("-")
        i = 0
        while i < len(keys) and keys[i] == "": 
            i += 1
        
        if i == len(keys):
            return ""
        
        keys = keys[i:]
        
        # Take into account, string except the first part to operate on
        subString = "".join(keys[1:])
        
        if not subString or len(keys) == 1:
            if len(keys[0]) < K:
                return keys[0].upper()
            else:
                return "-".join(re.findall("."*K, keys[0].upper()))
        
        # Debug
        # print keys, subString.upper()
        
        if len(subString)%K == 0:
            kSplit = [keys[0].upper()]
            kSplit.extend(re.findall("."*K, subString.upper()))
            return "-".join(kSplit)
        else:
            kSplit = [keys[0].upper()+subString[:len(subString)%K].upper()]
            kSplit.extend(re.findall("."*K, subString[len(subString)%K:].upper()))
            return "-".join(kSplit)
        """
            
        
        
