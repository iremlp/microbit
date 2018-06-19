
========
Niveau 1
========

Ce que l’on veut obtenir : afficher  un nombre entier entre 1 et 6 de façon aléatoire mais
à la façon d'un vrai dé, c-a-d avec des points.
Ce premier niveau permet d'introduire la problèmatique et de réinvestir les notions
utilisées lors du projet pile ou face.

Les notions abordées
--------------------

Dans ce niveau nous trouvons les notions suivantes :
  * constitution d'une liste
  * tirage d'un élément au hasard dans une liste


Les éléments utiles
-------------------

On propose aux élèves d'appeler les éléments suivants ::

  .. code-block:: python

    un = Image("00000:00000:00900:00000:00000")   # création d'une image par face
    issues = [un, ...]    # création d'une liste d'images
    random.choice(issues)     # tirage d'un élément au hasard dans une liste



Une solution possible
---------------------

Le résultat escompté est le suivant :

.. literalinclude:: de1.py
   :language: python
