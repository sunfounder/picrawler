.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et obtenez des aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_move:

Déplacer
==============

Voici le premier projet de PiCrawler. Il exécute sa fonction de base : se déplacer.

.. image:: img/move.png

**Exécuter le code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 move.py

Après l'exécution du code, PiCrawler effectuera les actions suivantes dans cet ordre : avancer, reculer, tourner à gauche, tourner à droite, se tenir debout.

**Code**

.. note::
    Vous pouvez **modifier/réinitialiser/copier/exécuter/arrêter** le code ci-dessous. Mais avant cela, vous devez accéder au répertoire source du code, comme ``pisloth\examples``. Après avoir modifié le code, vous pouvez l'exécuter directement pour voir l'effet.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    
    crawler = Picrawler() 
    
    def main():  
        
        speed = 80
              
        while True:
           
            crawler.do_action('forward',2,speed)
            sleep(0.05)     
            crawler.do_action('backward',2,speed)
            sleep(0.05)          
            crawler.do_action('turn left',2,speed)
            sleep(0.05)           
            crawler.do_action('turn right',2,speed)
            sleep(0.05)  
            crawler.do_action('turn left angle',2,speed)
            sleep(0.05)  
            crawler.do_action('turn right angle',2,speed)
            sleep(0.05) 
            crawler.do_step('stand',speed)
            sleep(1)
    
    if __name__ == "__main__":
        main()


**Comment ça fonctionne ?**

Tout d'abord, importez la classe ``Picrawler`` depuis la bibliothèque ``picrawler`` que vous avez installée, qui contient toutes les actions de PiCrawler et les fonctions qui les implémentent.

.. code-block:: python

    from picrawler import Picrawler

Ensuite, instanciez la classe ``crawler`` :

.. code-block:: python

    crawler = Picrawler() 

Enfin, utilisez la fonction ``crawler.do_action()`` pour faire déplacer PiCrawler.

.. code-block:: python
    
    crawler.do_action('forward',2,speed)    
    crawler.do_action('backward',2,speed)         
    crawler.do_action('turn left',2,speed)          
    crawler.do_action('turn right',2,speed) 
    crawler.do_action('turn left angle',2,speed) 
    crawler.do_action('turn right angle',2,speed)

En général, tous les mouvements de PiCrawler peuvent être réalisés avec la fonction ``do_action()``. Elle comporte trois paramètres :

* ``motion_name`` est le nom de l'action spécifique, incluant : ``forward``, ``turn right``, ``turn left``, ``backward``, ``turn left angle``, ``turn right angle``.
* ``step`` représente le nombre de fois que chaque action est effectuée, par défaut égal à 1.
* ``speed`` indique la vitesse de l'action, par défaut égal à 50, avec une plage de 0 à 100.

De plus, ``crawler.do_step('stand',speed)`` est également utilisé ici pour faire tenir PiCrawler debout. L'utilisation de cette fonction sera expliquée dans l'exemple suivant.
