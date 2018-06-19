.. _goFast-bloc-coder:

.. index:: programmation par blocs, bouton, durée

===============
Coder par blocs
===============


Structure de base du programme
==============================


Initialisation du programme
---------------------------



.. image:: /_static/goFast_makecode_01.*

Quelques remarques concernant cette initialisation du micro:bit.

.. important:: 
   Il y a dans ce jeu différents **états**.
   Le programme débute à l'état ``0``.
    
   * ``etat =  0`` : le jeu est en attente d'une partie.
     On quitte cet état en pressant le bouton A ou B     
   * ``etat = 1`` : le compte à rebours se lance.
     3 secondes plus tard, on passe automatiquement à l'état 2.      
   * ``etat = 2`` : la partie est en cours. Une pression sur le bouton
     A ou B permet de passer à l'état 3.      
   * ``etat = 3`` : l'écran indique le bouton gagnant puis passe
     automatiquement à l'état 0.


.. note::
   * **Victoire**
   
      La variable ``victoire`` permet d'afficher le gagnant.
      Ce sera un texte qui vaudra ``"A"``, ``"B"`` ou rien du tout ``""``.
   
   * **Temps de référence** 
   
      Pour déterminer les durées, nous allons utilisé et mettre à jour
      à la demande un temps de référence ``t0``.
      
      Ainsi, la durée sera déterminée par
      la différence entre le ``temps d'exécution`` du micro:bit
      et ce temps de référence.

Boucle principale
-----------------


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
   qui met le microcontrôleur en état d'attente. Cette boucle infinie
   se nomme ``toujours``.

Dans la boucle principale du programme, nous testerons donc
les différents états. Pour chacun des états, nous appellerons
la **fonction** dédiée.

.. image:: /_static/goFast_makecode_02.*

.. tip::
   Pour que cette boucle n'exécute que la tâche souhaitée, nous
   testons la valeur de la variable ``etat``.
   
   Ainsi, à chaque itération de la boucle, tant que ``etat`` n'est pas
   modifiée, c'est toujours la même fonction qui est appelée.

   Cette méthode est très pratique pour afficher le compte à rebours
   (état ``1``) ou le gagnant (état ``3``).

.. note:: 
   La durée d'exécution du jeu est mise à jour entre les tests des 
   états 0 et 1.
   
   Comme indiquée plus haut, la durée sera déterminée par
   la différence entre le ``temps d'exécution`` du micro:bit
   et le temps de référence ``t0``.

La fonction ``etat_0``
----------------------

L'état ``0`` est un état de *repos* du micro:bit : il ne fait rien
à par attendre qu'une partie démarre. Pour le sortir de cet état,
il suffit de presser un des deux boutons.

.. image:: /_static/goFast_makecode_03.*

.. note::
   Dès qu'un bouton est pressé, le temps de référence de cette
   nouvelle partie est réinitialisé.
   
   Nous ajoutons une pause afin éviter de détecter un double appui
   ou un appui prolongé sur le bouton. Ceci entraînerait, inévitablement,
   la perte de la partie pour le joueur concerné.

   
La fonction ``etat_1``
----------------------

La fonction ``etat_1`` est dédiée à l'affichage du compte à rebours.
La partie a débutée et si un joueur a le malheur de presser son 
bouton maintenant : la partie s'arrête et le nom du gagnant s'affiche
en passant à l'état ``3``.

.. image:: /_static/goFast_makecode_04.*

.. note::
   Une fois que le compte à rebours est écoulé, on détermine
   de façon aléatoire un temps d'attente entre 500ms et 5000ms.
   On passe alors à l'état 2.
   


La fonction ``etat_2``
----------------------

Cet état est le jeu à proprement parlé. Si un des joueurs appui
sur son bouton avant que la première LED ne s'allume, la partie est
immédiatement perdue pour lui.

En revanche, s'il est le premier à appuyer après la durée d'attente
(aléatoire et déterminée à l'état ``1``), alors il est le gagnant.

.. image:: /_static/goFast_makecode_05.*

   

La fonction ``etat_3``
----------------------

Cet état arrêter la partie. Mais avant cela, il y a une petite
animation, un léger suspens et puis une flêche indique le gagant.


.. image:: /_static/goFast_makecode_06.*

.. note::
   Les flêches sont différenciées selon les points cardinaux. La flêche
   qui pointe vers la gauche est la flêche Ouest alors que celle pointant
   vers la droite est la flêche Est.

