.. _pythonDe6faces:

=======================
Dé à 6 faces avec Python
=======================


Description
===========

Le but de ce projet de simuler une expérience aléatoire de lancer d'un dé à 6 faces.
Tout comme le projet simulant un pile ou face, cette situation permet de comprendre
l'intérêt des listes et va un peu plus loin dans leur utilisation.



Exemple(s) d'utilisation
---------------------------------------

  * Algorithmique et programmation au lycée général et technologique
  * Domaine statistique et probabilités du programme de mathématiques
  en seconde et première Bac Pro.
  * Accompagnement personnalisé pour des élèves de seconde Bac Pro



Progression
===========
Pour afficher aléatoirement un nombre entre 1 et 6, on peut se contenter
des 3 lignes ci-dessous.
::
  while True:
    if button_a.get_presses():
        display.show(str(random.randint(1, 6)))

Ce qui n'a pas d'autre intérêt que d'introduire la fonction "randint".

Contrairement à la progression par blocs, on suggère ici de commencer par
 l'affichage tel qu'il est sur un vrai dé. Ce qui permet de réexploiter les listes
 d'images vues avec le projet pile ou face.

.. toctree::

   Niveau 1 <de6faces-python1>
   Niveau 2 <de6faces-python2>
   Niveau 3 <de6faces-python3>
