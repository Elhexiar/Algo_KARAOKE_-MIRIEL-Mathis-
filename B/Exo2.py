class Joueur :
    def __init__(self,name,nbmusique) :

        self.pseudo = name
        scorelist = []
        for i in range(nbmusique):
            scorelist.append(0)
        
        self.scores = scorelist

    def getPlayerName(self):
        return(self.pseudo)

    def resultatChanson(self,nbchanson,newScore):

        if(newScore > self.scores[nbchanson]):

            self.scores[nbchanson] = newScore
        
        else:
            print("Vous n'avez malheureuseument pas ameliorez votre score")
    
        return()
    
    def getScoreList(self):

        return(self.scores)

    def getSpecificScore(self,nbchanson):

        return(self.scores[nbchanson])

    def getAverage(self):

        divider = 0
        sum = 0
        for i in range(len(self.scores)):

            if(self.scores[i]>=50):
                sum += self.scores[i]
                divider += 1
            
        if(divider > 0):
            average = sum/divider
            return(average)
        else:
            return(0)

    def getBest(self):

        best = 0
        index = 0

        for i in range(len(self.scores)):

            if(self.scores[i]>=50 and self.scores[i]>best):
                best = self.scores[i]
                index = i

        if(best>0):
            return(best)
        else:
            return(0)

    def getWorst(self):

        worst = 101
        index = 0

        for i in range(len(self.scores)):

            if(self.scores[i]>=50 and self.scores[i]<worst):
                worst = self.scores[i]
                index = i

        if(worst < 101):
            return(worst)
        else:
            return(0)



class Karaoke:

    def __init__(self):

        playerlist = []
        songlist =[]
        inp = 5

        print("Entrez le nom des musique !\n")
        while(len(songlist)<1 or inp != "0"):
            inp = input()
            if(inp !=0):
                songlist.append(inp)
                print("Le chanson ",inp," vient d'etre ajouter, entrée 0 si vous avez fini d'entrer les chanson")

        inp = 5
        print("entrez les joueur qui participerons !\n")
        while(len(playerlist)<1 or inp != "0"):
            inp = input()
            if(inp !=0):
                playerlist.append(Joueur(inp,len(songlist)))
                print("Le joueur ",inp," vient d'etre ajouter, entrée 0 si vous avez fini d'entrer les joueur")

        
        self.listeJoueur = playerlist
        self.listeChanson = songlist

    def getNomChanson(self,nbchanson):

        print("La chanson n°",nbchanson," est ",self.listeChanson[nbchanson])

    def addPlayer(self,newPlayer):

        self.listeJoueur.append(newPlayer)

    def removePlayer(self):

        index = 0

        print("Le Karaoke possede les joueur suivant lequel voulez vous supprimez ?")

        for i in range(len(self.listeJoueur)):

            print(i+1," : ",self.listeJoueur[i].getPlayerName())

        while(index<=0 or index >len(self.listeJoueur)):
            index = input()
        
        self.listeJoueur.pop(index)

    def addNewScore(self,nbplayer,nbsong,newScore):

        self.listeJoueur[nbplayer].resultatChanson(nbsong,newScore)

    def getBestSpecificScore(self,nbchanson):

        best = 0
        player = ""
        ignored = 0
        for i in range(len(self.listeJoueur)):
            if(self.listeJoueur[i].getSpecificScore(nbchanson)>=50 and self.listeJoueur[i].getSpecificScore(nbchanson)>best):
                best = self.listeJoueur[i].getSpecificScore(nbchanson)
                player = self.listeJoueur[i].getPlayerName()

            else: ignored +=1
        
        if(best>0):







    


    
        