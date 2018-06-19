.. _goFast-python-coder:

.. index:: micropython, bouton, durée

=====
Coder
=====



Le code nécessaire à la réalisation du projet :ref:`projetGoFast` a été
écrit en micropython. Vous trouverez ci-dessous :

   * `Le code, étape par étape`_
   * `Le code final`_


Le code, étape par étape
========================

Initialisation du programme
---------------------------

#. Incluons la bibliothèque Micro:bit et la bibliothèque
   :code:`random` pour générer de l'aléa :

   .. literalinclude:: goFast.py
      :lines: 5-6

#. Il y a dans ce jeu différents états. Initialement, le programme
   comment à l'état 0.


   .. note:: 
   
      L'utilisation de la variable ``etat`` permet de naviguer
      entre différent moment du programme.
      
 
   * ``etat =  0`` : le jeu est en attente d'une partie.
     On quitte cet état en pressant le bouton A ou B     
   * ``etat = 1`` : le compte à rebours se lance.
     3 secondes plus tard, on passe automatiquement à l'état 2.      
   * ``etat = 2`` : la partie est en cours. Une pression sur le bouton
     A ou B permet de passer à l'état 3.      
   * ``etat = 3`` : l'écran indique le bouton gagnant puis passe
     automatiquement à l'état 0.
   
   
   .. literalinclude:: goFast.py
      :lines: 13

#. La variable ``victoire`` stocke le nom du bouton gagnant.
   Cette variable est un texte qui peut valoir ``"A"`` ou ``"B"``.
   En début de partie, nous l'initialisons à un texte vide :
      
   .. literalinclude:: goFast.py
      :lines: 18



   .. tip:: 
   
      Pour faire une pause d'une certaine durée, il n'est parfois
      pas recommandé d'utiliser la commande ``sleep``.
      
      En effet, ``sleep`` empêche l'exécution de toutes
      les autres directives du programme durant cette pause.
      
      Il est préférable de déterminer une durée depuis un temps de
      référence et de tester, **à chaque boucle d'itération** la
      durée écoulée.
      
      Pour cela, il faudra utiliser la commande ``runing_time()``.

#. Dans ce programme, il faut parvenir à déterminer une **durée**.
   Pour cela, nous allons utiliser la commande ``running_time()``
   qui retourne la durée depuis laquelle le Micro:bit est sous
   tension.
   
   Après avoir initialisé notre temps de référence ``t0``
   (au démarrage du micro:bit ou en appuyant sur un bouton),
   nous calculerons la différence ``running_time() - t0``
   qui déterminera la durée.
   
   Initialisons ``t0``
   
   .. literalinclude:: goFast.py
      :lines: 23

#. Pour déterminer une durée, définissons la fonction ``chrono()``.

   La durée écoulée entre le temps de référence ``t0`` et le moment
   de l'appel de la fonction.

   .. literalinclude:: goFast.py
      :lines: 25-28      

#. Enfin, affichons à l'écran une image pour indiquer le programme
   est en attente.

   .. literalinclude:: goFast.py
      :lines: 30    

Boucle
------

.. warning::
   
   Lorsqu'un objet connecté est mis sous tension, le programme
   s'exécute après une brève phase d'initialisation.
   
   S'il n'y a pas de boucle, le programme ne s'exécute **qu'une seule
   fois** puis… plus rien!
   
   En fait, un objet connecté est en permanence en train d'attendre
   que quelque chose se passe : un bouton pressé, un geste, une
   certaine température, luminosité ou autres.
   
   Un peu comme votre clavier qui attend **en permanence** que vous
   appuyiez sur une touche.
   
   
   C'est pour cela qu'il est nécessaire d'exécuter une boucle infinie
   qui met le microcontrôleur en état d'attente.
   

#. La phase de configuration est terminée. Passons maintenant
   à la boucle qui… tourne en boucle.

   .. literalinclude:: goFast.py
      :lines: 32    

#. Configurons l'état ``0`` du programme qui attend que l'un
   des joueurs presse son bouton.
   
   Lorsqu'un bouton est pressé, il faut initialiser le temps de 
   référence ``t0`` puis changer d'état. La pause ``sleep(250)``
   permet d'éviter un *double-clic* du bouton
   qui entraînerait la fin prématurée de la partie.

   .. literalinclude:: goFast.py
      :lines: 34-39 

#. Il est temps de relever la durée écoulée depuis le temps de
   référence.

   .. literalinclude:: goFast.py
      :lines: 42

#. L'état ``1`` affiche le compte à rebours.

   .. literalinclude:: goFast.py
      :lines: 44

   Mais attention, si un joueur presse un bouton dans cet état,
   la partie est immédiatement perdue.
   
   .. literalinclude:: goFast.py
      :lines: 46-51
   
   Affichons le compte à rebours (sans oublier que les durées
   sont en millisecondes).
   
   .. literalinclude:: goFast.py
      :lines: 54-59
   
   


Le code final
=============


.. literalinclude:: goFast.py
   :linenos: