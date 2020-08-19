def printall(s):
    storage = ''
    for ch in s:
        if ch != '$':
            storage += ch
    ans = []
    def dfs(s, i, storage,st):
        if i == len(s):
            ans.append(st)
            return
	if s[i] == '$':
            for n in storage:
                dfs(s,i+1,storage,st+n)
        else:
            dfs(s,i+1,storage,st+s[i])
    dfs(s,0,storage,'')
    return ans

print(printall('2$3'))

print(printall('23$$'))

print(printall('$43$'))
