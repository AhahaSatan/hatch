class Spellchecker:
    def __init__(self):
        f = open("dictionary.txt", "r")
        self.s = set()
        npos = 1
        self.trie = [{}]
        self.capitals = {}
        for tps in f.readlines():
            q = tps.strip()
            i = q.lower()
            self.capitals[i]=q
            cpos = 0
            self.s.add(i)
            for j in i:
                if j not in self.trie[cpos]:
                    self.trie[cpos][j] = npos
                    self.trie.append({})
                    cpos = npos
                    npos += 1
                else:
                    cpos = self.trie[cpos][j]
        g = open("commonwords.txt", "r")
        self.rank = {}
        count = 0
        for tps in g.readlines():
            i = tps.split()[0].lower()
            if i in self.s:
                self.rank[i]=count
                count += 1

    def recommendations(self, word):
        if word in self.s: return [word]
        l = []
        cpos = 0
        if word[:-1] in self.s: l.append(word[:-1])
        for i in range(len(word)):
            if word[:i]+word[i+1:] in self.s: l.append(word[:i]+word[i+1:])
            for j in self.trie[cpos]:
                    if word[i]!= j and word[:i]+j+word[i:] in self.s:
                        l.append(word[:i]+j+word[i:])
                    if word[:i]+j+word[i+1:] in self.s:
                        l.append(word[:i]+j+word[i+1:])

            if word[i] not in self.trie[cpos]:
                break
            else:
                cpos = self.trie[cpos][word[i]]
        else:
            for i in self.trie[cpos]:
                if word+i in self.s: l.append(word+i)
        unr = []
        tpl = []
        for w in l:
            if w in self.rank:
                tpl.append([self.rank[w], self.capitals[w]])
            else:
                unr.append(self.capitals[w])
        tpl.sort()
        
        return [i[1] for i in tpl]+unr
