import requests
from queue import Queue
class Questions:
    def __init__(self, cat):
        self.token = requests.get("https://opentdb.com/api_token.php", params={"command":"request"}).json()['token']
        #print(self.token)
        self.id = cat
        self.new = [[] for i in range(3)]
        self.wrong = Queue()
        self.correctstreak = 0
        self.totalcorrect = 0
        self.totalwrong = 0
        self.currpos = 1
        self.fwrong = 0
        self.dlist = ["easy", "medium", "hard"]
        self.dind = 0
        self.available = [0 for i in range(3)]
        if cat == None:
            for i in requests.get("https://opentdb.com/api_category.php").json()['trivia_categories']:
                self.addcat(i["id"])
        else:
            self.addcat(cat)
        self.org = [i for i in self.available]

    def addcat(self, catid):
        tp = requests.get("https://opentdb.com/api_count.php", params={"category":catid}).json()['category_question_count']
        self.available[0] += tp['total_easy_question_count']
        self.available[1] += tp['total_medium_question_count']
        self.available[2] += tp['total_hard_question_count']
        

    def next(self):
        if not self.wrong.empty() and self.currpos%3 == 0:
            self.currpos+=1
            return self.wrong.get()
        if len(self.new[self.dind])==0:
            amount = min(50, self.available[self.dind])
            if amount == 0:
                if not self.wrong.empty():
                    return self.wrong.get()
                else:
                    requests.get("https://opentdb.com/api_token.php", params={"command":"reset", "token":self.token})
                    self.available = [i for i in self.org]
                    amount = min(50, self.available[self.dind])
            self.new[self.dind] = requests.get("https://opentdb.com/api.php",
                            params={"token":self.token, "category":self.id,
                            "difficulty":self.dlist[self.dind], "amount":amount}).json()["results"]

            self.available[self.dind]-=amount
        if not self.wrong.empty(): self.currpos+=1
        return self.new[self.dind].pop()
    
    def answer(self, ans, question):
        if ans==question['correct_answer']:
            self.totalcorrect +=1
            self.correctstreak +=1
            if self.correctstreak > 4 and self.dind<2: self.dind += 1
            return True
        else:
            self.totalwrong += 1
            self.wrong.put(question)
            self.correctstreak =0
            return False
