

print ( "Chargement des Qestions et Reponses ...")



#==============================================================================
# ajoute de la première QR
q = "Quand le terme ≪ Intelligence Artificielle ≫ a-t-il été fondé?" 
choix=['années 1930','années 1960', 'années 1990','années 2000']  
rep = [False, True, False, False] 
qr = nouvelleQR(q, choix, rep) 
ajouterQR(qr) 
#==============================================================================
q = "Qu'est-ce que l'intelligence artificielle?"
choix=["Ensemble des théories et des techniques mises en œuvre en vue de réaliser des machines capables de simuler l'intelligence humaine", 
       "Ensemble de programmes disponible à importer pour écrire des logicieles",
       "Jouer à un jeu en utilisant  de l'intelligence", 
       "Programmer avec votre propre intelligence"]
rep = [False, True, False, False] 
qr = nouvelleQR(q, choix, rep)  
ajouterQR(qr) 
#==============================================================================   
q = "Laquelle de ces affirmations vous semble la plus correcte?"
choix=["Le but de l'IA est de développer des techniques qui simulent le processus de raisonnement en lui-même.",
       "Les techniques de l'IA sont utilisées par les  sites web et logicieles d'auto-formation  pour soutenir les interactions avec l'apprenant.",
       "Le rôle des techniques de l'IA dans les logicieles d'auto-formation est de simuler l'intelligence humaine."]   

rep = [False, True, False] 
qr = nouvelleQR(q, choix, rep)  
ajouterQR(qr) 
#==============================================================================   
q="Qui a inventé le trem Intelligence Artificielle?" 
choix=["Arthur Samule", "James Slagle", "Jhon McCarthy",  "EF Morue"]
rep = [False, False, True, False] 
qr = nouvelleQR(q, choix, rep)  
ajouterQR(qr) 
#==============================================================================
q="Lequel des éléments suivants n’est pas l’avantage de l’IA ?"
choix=["Grande vitesse", "Menaçante" , "Précision" , "Coût élevé"]
rep = [False, True, False, False] 
qr = nouvelleQR(q, choix, rep)  
ajouterQR(qr) 
#==============================================================================
q="Les caractéristiques du système informatique capable de penser, de raisonner et d’apprendre sont connues par :"
choix=["Intelligence artificielle", "intelligence automatique", "intelligence virtuelle"]
rep = [True, False, False] 
qr = nouvelleQR(q, choix, rep)  
ajouterQR(qr) 

#==============================================================================
q="Le succès d’un comportement intelligent d’un système peut être mesuré avec un :"
choix=["Test du système",  "Test de Turing", "Test intelligent",  "Test de machine"]
rep = [False, True, False, False] 
qr = nouvelleQR(q, choix, rep)  
ajouterQR(qr) 
#==============================================================================
q="Laquelle des applications suivantes n’est pas de l’IA"
choix=["Photoshop", "Telsa", "Siri" , "Netflix"]
rep = [True, False, False, False] 
qr = nouvelleQR(q, choix, rep)  
ajouterQR(qr) 
#==============================================================================
q="Lequel des domaines suivants ne peut pas contribuer à construire un système intelligent ?"
choix=["Science des neurones", "Mathématiques",  "L’informatique",  "Géologie"]
rep = [False, False, False, True] 
qr = nouvelleQR(q, choix, rep)  
ajouterQR(qr) 
#==============================================================================
q="En quelle année le terme Intelligence Artificielle a été inventé ?"
choix=["1956", "1957",  "1965", "1959"]
rep = [True, False, False, False] 
qr = nouvelleQR(q, choix, rep)  
ajouterQR(qr) 
#==============================================================================
q="Si un robot peut modifier sa propre trajectoire en réponse à des conditions externes, il est considéré comme :" 
choix=["intelligent", "Extra ordinaire" , "Testeur de Turing", "Interpreteur de Connaissance"]
rep = [True, False, False, False] 
qr = nouvelleQR(q, choix, rep)  
ajouterQR(qr) 
#==============================================================================
q="quels sont les événements majeurs dans l'histoire de l'IA parmis les suivants:" 
choix=["1945 Invention du transistor", "1997: Deep blue bat Kasparove en jeu d'échecs" ,
       "1950 Test de Turing", "2016 AlphGo bat Lee en jeu de Go"]
rep = [False, True, True, True] 
qr = nouvelleQR(q, choix, rep)  
ajouterQR(qr) 
#==============================================================================




