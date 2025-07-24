a=[1,1,2,3,4,5]
b=[2,3,4,4,5,6]
ans=[]
ans=[]
        i=0
        j=0
        while i<len(a) and j<len(b):
            if a[i]<b[j]:
                if a[i] not in ans:
                    ans.append(a[i])
                i=i+1
            elif a[i]>b[j]:
                if b[j] not in ans:
                    ans.append(b[j])
                j=j+1
            else:
                if a[i] not in ans:
                    ans.append(a[i])
                i=i+1
                j=j+1
        while i<len(a):
            if a[i] not in ans:
                ans.append(a[i])
            i=i+1
        while j<len(b):
            if b[j] not in ans:
                ans.append(b[j])
            j=j+1
        return ans