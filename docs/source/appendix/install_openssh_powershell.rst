.. note::

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder sur Facebook ! Plongez plus profondément dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et vos défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des conseils et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _openssh_powershell:

Installer OpenSSH via PowerShell
===================================

Lorsque vous utilisez la commande ``ssh <nom_utilisateur>@<nom_hôte>.local`` (ou ``ssh <nom_utilisateur>@<adresse_IP>``) pour vous connecter à votre Raspberry Pi, mais que le message d'erreur suivant apparaît :

    .. code-block::

        ssh: Le terme 'ssh' n'est pas reconnu comme le nom d'un cmdlet, fonction, fichier de script ou programme exécutable. Vérifiez
        l'orthographe du nom, ou si un chemin a été inclus, assurez-vous que le chemin est correct et réessayez.


Cela signifie que votre système informatique est trop ancien et ne dispose pas d'`OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ préinstallé. Vous devez suivre le tutoriel ci-dessous pour l'installer manuellement.

#. Tapez ``powershell`` dans la barre de recherche de votre bureau Windows, faites un clic droit sur ``Windows PowerShell``, puis sélectionnez ``Exécuter en tant qu'administrateur`` dans le menu qui apparaît.

    .. image:: img/powershell_ssh.png
        :align: center

#. Utilisez la commande suivante pour installer ``OpenSSH.Client``.

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Après l'installation, le message suivant sera retourné.

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Vérifiez l'installation en utilisant la commande suivante.

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. À ce stade, le système vous indiquera que ``OpenSSH.Client`` a été installé avec succès.

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning::

        Si le message ci-dessus n'apparaît pas, cela signifie que votre système Windows est toujours trop ancien, et nous vous conseillons d'installer un outil SSH tiers, comme PuTTY.

#. Maintenant, redémarrez PowerShell et continuez à l'exécuter en tant qu'administrateur. Vous pourrez désormais vous connecter à votre Raspberry Pi en utilisant la commande ``ssh``, et vous serez invité à entrer le mot de passe que vous avez configuré précédemment.

    .. image:: img/powershell_login.png