# encoding=utf-8
__author__ = 'daby-one'



import sys
import time
G,D,I= g,d,i = -1,1,0
B = b = blanc = "_"





class MachineTuring():

    def __init__(self,ei,ef):
        self.etats = []
        self.ei = ei # état initial
        self.pi = 0 # position initiale
        self.ef = ef # état final
        self.position = 0 # position actuelle
        self.message = ""

    def ajouter_etat(self,numero,entree,e_suivant,sortie,mvt):
        try:
            self.etats[numero][entree] = {"e_suivant" : e_suivant, "sortie" : sortie, "mvt" : mvt }
        except:
            self.etats.append({entree : {"e_suivant" : e_suivant, "sortie" : sortie, "mvt" : mvt }})

    def lire(self,entree):
        try:
            tmp = self.etats[self.ea][entree]
            self.message[self.position] = tmp["sortie"]
            self.position = self.position + tmp["mvt"]
            if self.position < 0:
                raise Exception("Débordement à droite.")
            self.ea = tmp["e_suivant"]
        except Exception as e:
            print str(e)
            print "Erreur lecture"
            exit(-1)

    def demarrer(self,message,position):
        self.position = position
        self.message = list(message)
        print self.message
        self.ea = self.ei
        max_it = 1000
        print ''.join(self.message) + " état ::"+str(self.ea)
        print (" "*self.position)+"^"
        while self.ea != self.ef and max_it != 0:
            max_it -=  1
            self.lire(self.message[self.position])
            print " => état ::"+str(self.ea)+"\n" + ''.join(self.message) 
            print (" "*self.position)+"^"
            time.sleep(0.5)
        else:
            print (''.join(self.message)).replace("$","").replace("#","").replace("_","")
            print "OK en "+str(1000-max_it)+"mouvements"

    def get_etats(self):
        return self.etats


if __name__ == '__main__':

    m1 = MachineTuring(0,1)
    m1.ajouter_etat(0,'A',0,'A',D)
    m1.ajouter_etat(0,'B',0,'A',D)
    m1.ajouter_etat(0,'_',1,'_',I)

    #m1.demarrer("ABBA",0)

    m2 = MachineTuring(0,3)
    m2.ajouter_etat(0,'1',2,'1',D)
    m2.ajouter_etat(0,'0',1,'0',D)
    m2.ajouter_etat(1,'0',1,'0',D)
    m2.ajouter_etat(1,'1',2,'1',D)
    m2.ajouter_etat(1,'_',3,'_',D)
    m2.ajouter_etat(2,'1',2,'1',D)
    m2.ajouter_etat(2,'0',2,'0',D)
    m2.ajouter_etat(2,'_',3,'0',D)



    #m2.demarrer("10001__",2)


    m3 = MachineTuring(0,8)

    m3.ajouter_etat(0,"_",1,"_",D)

    m3.ajouter_etat(1,"a",1,"a",D)
    m3.ajouter_etat(1,"b",1,"b",D)
    m3.ajouter_etat(1,"_",2,"_",G)

    m3.ajouter_etat(2,"a",3,"_",D)
    m3.ajouter_etat(2,"b",5,"_",D)
    m3.ajouter_etat(2,"_",8,"_",I)

    m3.ajouter_etat(3,"_",4,"a",D)

    m3.ajouter_etat(4,"a",4,"a",D)
    m3.ajouter_etat(4,"b",4,"b",D)
    m3.ajouter_etat(4,"_",7,"a",G)

    m3.ajouter_etat(5,"_",6,"b",D)

    m3.ajouter_etat(6,"a",6,"a",D)
    m3.ajouter_etat(6,"b",6,"b",D)
    m3.ajouter_etat(6,"_",7,"b",G)

    m3.ajouter_etat(7,"a",7,"a",G)
    m3.ajouter_etat(7,"b",7,"b",G)
    m3.ajouter_etat(7,"_",2,"_",G)



    #m3.demarrer("_ab_____",0)
    #m3.demarrer("_babaabb____________",0)

    m4 = MachineTuring(0,4)
    m4.ajouter_etat(0,"a",1,"_",D)
    m4.ajouter_etat(1,"a",1,"a",D)
    m4.ajouter_etat(1,"b",1,"b",D)
    m4.ajouter_etat(1,"_",2,"_",G)
    m4.ajouter_etat(2,"b",3,"_",G)
    m4.ajouter_etat(3,"a",3,"a",G)
    m4.ajouter_etat(3,"b",3,"b",G)
    m4.ajouter_etat(3,"_",0,"_",D)
    m4.ajouter_etat(0,"_",4,"_",D)

    #m4.demarrer(sys.argv[1],0)

    m5 = MachineTuring(0,6)
    m5.ajouter_etat(0,"a",1,"_",D)
    m5.ajouter_etat(0,"b",2,"_",D)
    m5.ajouter_etat(1,"a",1,"a",D)
    m5.ajouter_etat(1,"b",1,"b",D)
    m5.ajouter_etat(1,"_",3,"_",G)
    m5.ajouter_etat(2,"a",2,"a",D)
    m5.ajouter_etat(2,"b",2,"b",D)
    m5.ajouter_etat(2,"_",4,"_",G)
    m5.ajouter_etat(3,"a",5,"_",G)
    m5.ajouter_etat(4,"b",5,"_",G)
    m5.ajouter_etat(5,"a",5,"a",G)
    m5.ajouter_etat(5,"b",5,"b",G)
    m5.ajouter_etat(5,"_",0,"_",D)
    m5.ajouter_etat(0,"_",6,"_",I)
 
    #m5.demarrer(sys.argv[1],0)

    m6 = MachineTuring(0,16)
    m6.ajouter_etat(0,'1',0,'1',D)
    m6.ajouter_etat(0,'0',0,'0',D)
    m6.ajouter_etat(0,'#',1,'#',G)
    m6.ajouter_etat(1,'1',2,'#',D)
    m6.ajouter_etat(1,'0',8,'#',D)
    m6.ajouter_etat(2,'0',2,'0',D)
    m6.ajouter_etat(2,'1',2,'1',D)
    m6.ajouter_etat(2,'#',2,'#',D)
    m6.ajouter_etat(2,'$',3,'$',G)
    m6.ajouter_etat(3,'1',4,'$',D)
    m6.ajouter_etat(3,'0',5,'$',D)
    m6.ajouter_etat(3,'#',5,'$',D)
    m6.ajouter_etat(4,'$',6,'0',G)
    m6.ajouter_etat(5,'$',6,'1',G)
    m6.ajouter_etat(6,'$',6,'$',G)
    m6.ajouter_etat(6,'1',6,'1',G)
    m6.ajouter_etat(6,'0',6,'0',G)
    m6.ajouter_etat(6,'#',7,'#',G)
    m6.ajouter_etat(7,'#',7,'#',G)
    m6.ajouter_etat(7,'0',1,'0',I)
    m6.ajouter_etat(7,'1',1,'1',I)
    m6.ajouter_etat(7,'$',12,'$',D)
    m6.ajouter_etat(8,'1',8,'1',D)
    m6.ajouter_etat(8,'0',8,'0',D)
    m6.ajouter_etat(8,'#',8,'#',D)
    m6.ajouter_etat(8,'$',9,'$',G)
    m6.ajouter_etat(9,'1',10,'$',D)
    m6.ajouter_etat(9,'0',11,'$',D)
    m6.ajouter_etat(9,'#',11,'$',D)
    m6.ajouter_etat(10,'$',6,'1',G)
    m6.ajouter_etat(11,'$',6,'0',G)
    m6.ajouter_etat(12,'1',12,'1',D)
    m6.ajouter_etat(12,'#',12,'#',D)
    m6.ajouter_etat(12,'0',12,'0',D)
    m6.ajouter_etat(12,'$',13,'$',G)
    m6.ajouter_etat(13,'1',14,'$',D)
    m6.ajouter_etat(13,'0',15,'$',D)
    m6.ajouter_etat(13,'#',16,'#',I)
    m6.ajouter_etat(14,'$',12,'1',G)
    m6.ajouter_etat(15,'$',12,'0',G)

    #calcule le xor entre a et b ($a#b$_)
    #m6.demarrer("$101101#0000$_",1)




