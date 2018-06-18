
========
Niveau 1
========

Ce que l’on veut obtenir : afficher "P" ou "F" de façon aléatoire à l’issue d’une courte animation.
Ce premier niveau permet de se familiariser avec les fonctions utilisées pour interagir avec le microbit.
Contrairement à la programmation par bloc, il est plus efficace ici de choisir "P" ou "F"
aléatoirement dans la liste composée de ces 2 singletons.
De plus cela permettra facilement de truquer l'expérience aléatoire.

Les notions abordées
--------------------

Dans ce niveau nous trouvons les notions suivantes :
  * interactions avec le microbit (bouton, affichage)
  * aléa (random)
  * notion de liste


Les éléments utiles
-------------------

On propose aux élèves d'appeler les éléments suivants ::

  import random # bibliothèque pour générer de l'aléa
  Image("xxxxx:xxxxx:xxxxx:xxxxx:xxxxx") # où x représente l'intensité d'une diode comprise entre 0 et 9
  random.choice(liste)    # pour choisir un élément au hasard dans une liste
  ["P", "F"]    # liste des issues (texte) que l'on veut afficher


Une solution possible
---------------------

Le résultat escompté est le suivant :

.. literalinclude:: pileface1.py
   :language: python
