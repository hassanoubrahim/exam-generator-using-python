

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
        for qr in lqr:
            print("=================================================================")
            print(qr[0])
            for i in range(len(qr[1])):
                print("[{}] : {}".format(i, qr[1][i] ))
            rep=input("Votre choix (plusieurs reponses sont possibes ex:0 2): ")
            liste_rep=  rep.split(' ')
            nb_true_rep=qr[2].count(True)
            sub_score=0.0
            good_ans=set([i for i, e in enumerate(qr[2]) if e == True])
            for r in liste_rep:
                try:
                    j = int(r)
                    good_ans.append(j)
                    if qr[2][j] : 
                        sub_score=sub_score + 1.0/nb_true_rep 
                except : continue
            if  sub_score != 1:
                print("-----------------------/ \----------------------------------------")
                print("----------------------/ ! \---------------------------------------")
                print("Votre réponse est incorrecte! la bonne réponse est : ", good_ans)
                print("-----------------------------------------------------------------")
            score +=sub_score 
    print("Votre score={:.2f}%".format((score/n)*100)) 
    do = str(input("Continuez?(y/n): "))


print("Thank you and good luck in the exam!")
         
             

