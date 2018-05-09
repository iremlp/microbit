.. _projetTempCoder:

.. index:: micropython, température

=====
Coder
=====




Le code nécessaire à la réalisation du projet :ref:`projetTemp` a été
écrit en micropython. Vous trouverez ci-dessous :

   * `Le code, étape par étape`_
   * `Le code final`_


Le code, étape par étape
========================



#. Incluons la bibliothèque Micro:bit

   .. literalinclude:: temperature.py
      :lines: 2

#. Créons les images qui nous servirons à animer l'écran.
   La luminosité d'une diode varie de :code:`0` (éteinte)
   à :code:`9` (maximale).
   
   Lorsque la température augmente, l'affichage passe progressivement
   de :code:`image1` à :code:`image 5`.
   
   .. literalinclude:: temperature.py
      :lines: 6-35

#. Il y aura deux états dans le jeu :

   *  La variable :code:`victoire` est vrai et l'écran 
      affiche le code secret.       
   *  la variable :code:`victoire` est fausse et l'écran
      affiche l'énigme.
      
   Au début, la variable est donc fausse.
   
   .. literalinclude:: temperature.py
      :lines: 38

#. La phase de configuration est terminée. Passons maintenant à 
   la boucle qui… tourne en boucle. 
   
   Tout ce qui suivra cette codee sera donc indenté (tabulation).

   .. literalinclude:: temperature.py
      :lines: 41

#. Nous envisageons trois actions possibles :

   a) le jeu se réinitialise grâce au bouton A ;
   
      .. literalinclude:: temperature.py
         :lines: 43-44      
   
   b) le jeu est gagné et l'écran affiche le code final
   (après une petite animation);
   
      .. literalinclude:: temperature.py
         :lines: 47-52      
   
   c) le jeu est en cours et l'écran affiche les :code:`image`.
   
      .. literalinclude:: temperature.py
         :lines: 55
         
      Lire la température
   
      .. literalinclude:: temperature.py
         :lines: 57
         
      Plus la température augmente, plus les images affichées
      remplissent l'écran
      
      .. literalinclude:: temperature.py
         :lines: 60-71
      
      et enfin, si la température dépasse 34°C,
      alors là on passe en mode :code:`victoire` vrai.
      On ajoute une petite animation pour montrer que la
      victoire approche.
   
      .. literalinclude:: temperature.py
         :lines: 73-80
      
      Pour finir, une pause syndicale de 500ms.
   
      .. literalinclude:: temperature.py
         :lines: 81
   
   
   
         
   
   
   






Le code final
=============


.. literalinclude:: temperature.py
   :linenos: