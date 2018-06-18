.. _pythonDe6faces:

===================
Dé 6 faces (Python)
===================


Description
===========

Le but de ce projet de simuler une expérience aléatoire de lancer d'un dé à 6 faces.
Tout comme le projet simulant un pile ou face, cette situation permet de comprendre
l'intérêt des listes et va un peu plus loin dans leur utilisation.



Exemple(s) d'utilisation
------------------------

  * Algorithmique et programmation au lycée général et technologique
  * Domaine statistique et probabilités du programme de mathématiques en seconde et première Bac Pro.
  * Accompagnement personnalisé pour des élèves de seconde Bac Pro



Progression
===========

Pour afficher aléatoirement un nombre entier entre 1 et 6,
on peut se contenter des 3 lignes ci-dessous.

.. code-block:: python

   while True:
      if button_a.get_presses():
         # "str" car "display.show" n'affiche que du texte
         display.show(str(random.randint(1, 6)))  


Ce qui n'a pas d'autre intérêt que d'introduire la fonction
:code:`randint`.
Ici, contrairement à la progression utilisée lors du projet 

, nous suggèrons de commencer par simuler l'affichage tel
qu'il apparaît sur un vrai dé.
Cela qui permet de réexploiter les listes d'images
introduites avec le projet pile ou face.


Progression
===========

.. toctree::
   :maxdepth: 1
   
   Niveau 1 <de6faces-python1>
   Niveau 2 <de6faces-python2>
   Niveau 3 <de6faces-python3>
