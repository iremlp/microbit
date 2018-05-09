.. _projetTempCoder:

=====
Coder
=====


Nous détaillons ici le code nécessaire à la réalisation
du projet :ref:`projetTemp`.


.. index:: micropython, température



Le code, étape par étape
========================
Ce projet a été programmé en micropython.


#. Incluons la bibliothèque Micro:bit

   .. literalinclude:: temperature.py
      :lines: 2

#. Créons les images qui nous servirons à animer l'écran.
   La luminosité d'une diode varie de :command:`0` (éteinte)
   à :command:`9` (maximale).
   
   .. literalinclude:: temperature.py
      :lines: 6-35

#. Indiquons au programme que le jeu commence.
   Ainsi au démarrage, le jeu commence. Lorsque l'énigme sera résolue,
   l'écran affichera le code secret attendu.
   
   .. literalinclude:: temperature.py
      :lines: 38
   

Le code final
=============


.. literalinclude:: temperature.py
   :linenos: