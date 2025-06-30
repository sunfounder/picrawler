.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et obtenez des aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions et concours festifs** : Participez à des concours et des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_avoid:

Évitement d'Obstacle
=========================

Dans ce projet, PiCrawler utilise un module ultrasonique pour détecter les obstacles 
devant lui. Lorsque PiCrawler détecte un obstacle, il envoie un signal et cherche une 
autre direction pour continuer à avancer.

.. .. image:: img/avoid1.png

**Exécuter le Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 avoid.py

Après l'exécution du code, PiCrawler avancera. S'il détecte qu'un obstacle est à moins de 10 cm, il s'arrêtera, émettra un signal d'alerte, puis tournera à gauche et s'arrêtera. Si aucun obstacle n'est détecté après le virage à gauche, ou si la distance à l'obstacle est supérieure à 10 cm, il continuera à avancer.

**Code**

.. note::
    Vous pouvez **Modifier/Réinitialiser/Copier/Exécuter/Arrêter** le code ci-dessous. Mais avant cela, vous devez vous rendre dans le répertoire du code source, tel que ``picrawler\examples``. Après avoir modifié le code, vous pouvez l'exécuter directement pour voir l'effet.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from robot_hat import TTS, Music
    from robot_hat import Ultrasonic
    from robot_hat import Pin
    import time

    tts = TTS()
    music = Music()

    crawler = Picrawler() 
    sonar = Ultrasonic(Pin("D2") ,Pin("D3"))
    music.music_set_volume(100)

    alert_distance = 15
    speed = 80

    def main():
        distance = sonar.read()
        print(distance)
        if distance < 0:
            pass
        elif distance <= alert_distance:
            try:
                music.sound_play_threading('./sounds/sign.wav', volume=100)
            except Exception as e:
                print(e)
            crawler.do_action('turn left angle',3,speed)
            time.sleep(0.2)
        else :
            crawler.do_action('forward', 1,speed)
            time.sleep(0.2)

    if __name__ == "__main__":
        while True:
            main()

**Comment ça fonctionne ?**

Vous pouvez obtenir la distance en important la classe ``Ultrasonic``.

.. code-block:: python

    from robot_hat import Ultrasonic

Ensuite, initialisez les broches du module ultrasonique.

.. code-block:: python

    sonar = Ultrasonic(Pin("D2") ,Pin("D3"))


Voici le programme principal.

* Lisez la ``distance`` détectée par le module ultrasonique et filtrez les valeurs inférieures à 0 (lorsque le module ultrasonique est trop éloigné de l'obstacle ou qu'il ne peut pas lire les données correctement, ``distance < 0`` apparaîtra).
* Lorsque la ``distance`` est inférieure ou égale à ``alert_distance`` (la valeur seuil définie précédemment, soit 10), le son ``sign.wav`` est joué. PiCrawler effectue un ``virage à gauche``.
* Lorsque la ``distance`` est supérieure à ``alert_distance``, PiCrawler se déplace ``en avant``.

.. code-block:: python

    distance = sonar.read()
    print(distance)
    if distance < 0:
        pass
    elif distance <= alert_distance:
        try:
            music.sound_play_threading('./sounds/sign.wav', volume=100)
        except Exception as e:
            print(e)
        crawler.do_action('turn left angle',3,speed)
        time.sleep(0.2)
    else :
        crawler.do_action('forward', 1,speed)
        time.sleep(0.2)


.. note::

    Vous pouvez ajouter différents effets sonores ou musiques dans les dossiers ``musics`` ou ``sounds`` via :ref:`filezilla`.
