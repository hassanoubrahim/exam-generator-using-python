

import copy, sys
from random import  shuffle
#liste de questions et leurs réponses
QR = []


def nouvelleQR (question, choix, rep) :
    '''   
    # question : la question
    # choix: les choix multiples sous forme de liste
    # rep: liste de boolean de m^eme taille que de la liste choix
        '''
    if len(choix)!=len(rep):
        raise ValueError("La taille de liste des choix de être égale à celle ddes réponses.") 
    return [question, choix, rep]



def  ajouterQR (qr) :
    global QR
    QR.append(qr)
    

def  ordreAleatoire(n) :
    global QR
    shuffle(QR)
    return QR[:n]
    

exec(open("./QR.py").read())



score=0.0
n = len(QR)
do='y'
while do == 'y': 
    n = int(input("Entrez le nombre de questions <= {} : ".format(len(QR)) )) 
    if  not( n>0 and n<=len(QR) ):
        print(" Erreur: impossible de générer des questons, relancez le programe!")
        sys.exit(1)
        break # stops the loop when n is valid
    else:
        lqr = ordreAleatoire(n)
        good_ans = []
        user_ans = []
        for qr in lqr:
            print("=================================================================")
            print(qr[0])
            for i in range(len(qr[1])):
                print("[{}] : {}".format(i, qr[1][i] ))
            rep=int(input("Votre choix (plusieurs reponses sont pas possibes ex:2): "))
            user_ans.append(rep)
            for i in range(len(qr[2])):
                if qr[2][i] == True:
                    good_ans.append(i)
        score = 0
        #print('good ansers', good_ans, 'user ansers:', user_ans)
        for i in range(n):
            if good_ans[i] == user_ans[i]:
                score += 1
        print('votre score est : ', float(score/n))
        do = str(input("Continuez?(y/n): "))

print('thanks for taking this exam')
                    






