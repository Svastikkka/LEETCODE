class Solution:
    def reorderLogFiles(self, logs):
        arr1,arr2=[],[]
        for i in logs:
            if i.split()[1].isdigit():
                arr1.append(i)
            else:
                arr2.append(i.split())
        arr2.sort(key=lambda x:x[0] )
        arr2.sort(key=lambda x:x[1:] )
        for i in range(len(arr2)):
            arr2[i]=" ".join(arr2[i])
        arr1.extend(arr2)
        return  arr1
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
s=Solution()
print(s.reorderLogFiles(logs))