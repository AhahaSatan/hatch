class Parser:
    def __init__(self, sources):
        self.lines = []
        for filename in sources:
            with open(filename) as f:
                l = [x.strip() for x in f.readlines()]
                for i in l:
                    k=self.clean(i)
                    if len(k)>0:
                        if len(self.lines)>0 and self.lines[-1][-1].isalpha():
                            k[0] = k[0].lower()
                            self.lines[-1] = self.lines[-1]+k
                        else: self.lines.append(k)

    def parsefile(self, filename):
        tp = []
        with open(filename) as f:
                l = [x.strip() for x in f.readlines()]
                for i in l:
                    k=self._clean(i)
                    if len(k)>0:
                        if len(tp)>0 and tp[-1][-1].isalpha():
                            k[0] = k[0].lower()
                            tp[-1] = tp[-1]+k
                        else: tp.append(k)

        return tp


    def _clean(self, line):
        p = []
        for i in line.split():
            try:
                int(i)
            except ValueError:
                if len(i)>1 or i[0].isalpha():
                    p.append(i)
        return p
    
