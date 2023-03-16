class Joueur :
    def __init__(self,name) :

        self.pseudo = name
        self.scores = [0,0,0,0,0]

    def resultatChanson(self,nbchanson,newScore):

        if(newScore > self.scores[nbchanson]):

            self.scores[nbchanson] = newScore
        
        else:
            print("Vous n'avez malheureuseument pas ameliorez votre score")
    
        return()
    
    def getScoreList(self):

        ignored = 0

        print("Le joueur ",self.pseudo," a les scores suivants :")
        
        for i in range (len(self.scores)):

            if (self.scores[i]>=50):
                print("Chanson n°",i, " : ",self.scores[i])
            else : ignored +=1
            
        if(ignored == 5):
            print(self.pseudo, " N'a pas encore enregistré de score sur aucune chanson !")

    def getSpecificScore(self,nbchanson):

        if(self.scores[nbchanson]>=50):
            print("Pour la chanson n°",nbchanson,", ",self.pseudo, " a un score de :",self.scores[nbchanson], "")
        else: ("Pour la chanson n°",nbchanson,", ",self.pseudo, " n'a pas encore de score enregistré !")

        return()

    def getAverage(self):

        divider = 0
        sum = 0
        for i in range(len(self.scores)):

            if(self.scores[i]>=50):
                sum += self.scores[i]
                divider += 1
            
        if(divider > 0):
            average = sum/divider
            print("La moyenne des score de ",self.pseudo, " est de : ", average)
        else:
            print(self.pseudo," n'a pas encore enregistré de score !")

    def getBest(self):

        best = 0
        index = 0

        for i in range(len(self.scores)):

            if(self.scores[i]>=50 and self.scores[i]>best):
                best = self.scores[i]
                index = i

        if(best>0):
            print("Le meilleur score de ",self.pseudo, " est de : ",best," sur la chanson n°",index)
        else:
            print(self.pseudo," n'a pas encore enregistré de score !")

        return()

    def getWorst(self):

        worst = 101
        index = 0

        for i in range(len(self.scores)):

            if(self.scores[i]>=50 and self.scores[i]<worst):
                worst = self.scores[i]
                index = i

        if(worst < 101):
            print("Le pire score de ",self.pseudo, " est de : ",worst," sur la chanson n°",index)
        else:
            print(self.pseudo," n'a pas encore enregistré de score !")

        return()