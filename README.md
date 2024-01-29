# Désarmer la désinformation TTP (tactiques, techniques et procédures)

Le désarmement est un cadre conçu pour décrire et comprendre les incidents de désinformation.Disarm fait partie des travaux sur l'adaptation des pratiques de sécurité de l'information (INFOSEC) pour aider à suivre et à contrer la désinformation et à d'autres dommages à l'information, et est conçu pour s'adapter aux pratiques et outils Infosec existants.

Le style de Disarm est basé sur le [mitre att & amp; ck framework](https://github.com/mitre-attack/attack-website/).Les modèles STIX pour les objets de désarmement sont disponibles dans le [DISARM_CTI Repo](https://github.com/DISARMFoundation/DISARM_cti) - Celles-ci facilitent le désarmement de données entre Isaos et des corps similaires en utilisant des normes comme les taxi.

## Qu'y a-t-il dans ce dossier

Désarmer la documentation:
* [DISARM_DOCUMÉTIATION](DISARM_DOCUMENTATION): Désarmer les guides de l'utilisateur, les guides de conception et la documentation TTP plus détaillée.
* [DISARM_HISTORY](DISARM_DOCUMENTATION/DISARM_HISTORY): modèles et rapports antérieurs.

Désarmer les cadres:* [Désarmer le cadre d'équipe rouge](generated_pages/disarm_red_framework.md) - Créateur de désinformation TTPS, répertorié par tactique.Il s'agit du «framework de désarme» classique qui est emballé avec MISP.La version [clickable](generated_files/disarm_red_framework_clickable.html) consiste à créer rapidement des listes de TTP.
* [Désarmer Blue Team Framework](generated_pages/disarm_blue_framework.md) - Répondeur de désinformation TTPS, répertorié par tactique.Ce sont des contre-mesures, répertoriés par les premières étapes tactiques dans lesquelles ils sont susceptibles d'être utilisés.

Désarmer des objets: toutes les entités utilisées pour créer l'équipe rouge et les frameworks d'équipe bleue:
* [Phases](generated_pages/phases_index.md): groupes de tactiques de niveau supérieur, créés pour que nous puissions vérifier que nous n'avons rien manqué
* [Tactics](generated_pages/tactics_index.md): étapes que quelqu'un qui exécute un incident de désinformation est susceptible d'utiliser
* [Techniques](generated_pages/techniques_index.md): activités qui pourraient être vues à chaque étape* [Tâches](generated_pages/tasks_index.md): des choses qui doivent être faites à chaque étape.Dans Pablospeak, les tâches sont des choses que vous faites, les techniques sont la façon dont vous les faites.
* [Compteurs](generated_pages/counters_index.md): contre-mesures pour désarmer TTPS.
* [Types d'acteurs](generated_pages/actortypes_index.md): ressources nécessaires pour exécuter des contre-mesures
* [Types de réponse](generated_pages/responsetype_index.md): les catégories de cours que nous avons utilisées pour créer des compteurs
* [MetaTechniques](generated_pages/metatechniques_index.md): un regroupement de niveau supérieur pour les contre-mesures
* [Incidents](generated_pages/incidents_index.md): descriptions d'incident utilisées pour créer les cadres de désarme

Il y a un répertoire pour chacun d'eux, contenant une fiche technique pour chaque entité individuelle (par exemple [Technique T0046 Recherche Optimisation du moteur](generated_pages/techniques/T0046.md)).Il y a aussi un répertoire [généré_files](generated_files) contenant des fichiers (csvs, sqlite etc) que nous générons à partir des tables ci-dessus.## Mise à jour du désarme

Changements majeurs: Tout changement majeur des modèles de désarmement est convenu par la Fondation Disarm.

Modifications mineures: nous aimons toutes les suggestions d'améliorations, de commentaires et d'offres d'aide - nous contacter en utilisant [ce formulaire Google](https://docs.google.com/forms/d/e/1FAIpQLSdZuyKFp1UZzk6qUE4IN1O14HaJ-F4TH9thxR3hrRU-Mu7QUQ/viewform).(Nous revenons également par le biais de listes de numéros précédents: [Liste des problèmes Amitt](https://github.com//DISARM/issues) et [Misinfosec Issues List](https://github.com/misinfosecproject/DISARM_framework/issues))

Utilisation de vos propres ensembles de données: le désarme est open source.Si vous voulez faire votre propre truc avec les données de désarmement, celles-ci vous aideront:
* Toutes les données de maîtrise pour le désarmement sont dans le répertoire [DISARM_MASHER_DATA](DISARM_MASTER_DATA).Recherchez la feuille de calcul [DISARM_FRAMEWORKS_MASHER.XLSX](DISARM_MASTER_DATA/DISARM_FRAMEWORKS_MASTER.xlsx).Cela contient des tactiques, des techniques, des tâches, des phases et des comptoirs des créateurs de désinformation.* Le [désarmement TTP Guide](https://docs.google.com/document/d/1Kc0O7owFyGiYs8N8wSq17gRUPEDQsD5lLUL_3KGCgRE/edit#) a des informations plus détaillées sur chaque technique.

* Le code pour créer tous les feuilles de données HTML est dans Directory [Code](CODE): vous aurez besoin de générer_disarm_pages.py et de tous les fichiers de modèle.

Si vous avez votre propre version de ce référentiel et mettez à jour DISARM_FRAMEWORKS_MASHER.XLSX, la dactylographie "Python generate_disarm_pages.py" mettra à jour tous les fichiers ci-dessus.Si vous souhaitez mettre à jour le fichier GitHub désarmé, désarmer les bases de données et désarmer le bundle STIX en même temps, exécutez le fichier generate_disarm_pages.ipynb à partir de Jupyter.


## Qui est responsable du désarmement (et un peu d'histoire)

* Maintenant: **[Disarm Foundation](https://www.disarm.foundation/)** maintient et met à jour la famille de désarmement des modèles: Disarm-Stix, le framework rouge désarme (de la création de désinformation), et le Disarm BlueCadre (des contre-mesures de désinformation et des atténuations).* En 2022, **Mitre, FIU et Cogseccollab Teams** ont travaillé ensemble pour fusionner les modèles de cadre Amitt et Spice pour créer les cadres de désarme, dirigés par SJ, Pablo, Mark et Jon Brewer (qui nous maintient tous organisés).Cette équipe a créé la Fondation Disarm.

* 2020?**[miter](https://www.mitre.org/) et [fiu: Florida International University](https://www.fiu.edu/)** a fourré le modèle Amitt Red pour créer le cadre d'épice,,Dirigé par Mark Finlayson à la CRF.

* 2020-2022: **[cogseccollab](http://cogsec-collab.org/)** a maintenu et mis à jour les modèles Amitt originaux.Cogseccollab est l'organisme à but non lucratif qui a sorti de Misinfosecwg.Cogseccollab a utilisé Amitt dans les réponses Covid19 de la Ligue CTI et l'a testée en essais avec l'OTAN, l'UE et les unités de désinformation de plusieurs autres pays.SJ Terp et Pablo Breuer ont tenu l'autorité de conception des modèles Amitt.* 2018-2020: **[misinfosecwg](https://github.com/credcoalition/community-site/wiki/Working-Groups)**, alias le groupe de travail Misinfosec de la coalition de crédibilité a créé les cadres de désarme originaux.La coalition de crédibilité est un choix naturel pour la partie des normes (car en 2017, tous les groupes - médias, militaires, publicités, public, etc. - avaient un ensemble différent de mots pour les composants de désinformation), et puisque SJ était là lorsque la coalition de crédibilité étaitCréés, ils étaient un endroit naturel pour faire ce travail.Le cadre rouge a été lancé en décembre 2018, raffiné dans un séminaire de coalition de crédibilité Misinfosec, et s'est disputé par SJ et Pablo chez Softwerx sur une quantité déraisonnable de café;Le cadre bleu a été lancé comme une collection de contre-mesures de désinformation potentielles, lors d'un séminaire de coalition Misinfosec en novembre 2019. Cette œuvre a été dirigée conjointement par SJ et Christopher Walker ("Walker") de Marvelous.ai, ensuite rejoint par John Gray à partir de mentionmapp,Mais c'était vraiment un effort communautaire de Credco, avec des contributions de nombreuses personnes et lieux, dont Roger Johnston, qui a rejoint après avoir présenté ATT & CKCON, et a commencé à construire de nombreux outils et connexions à des systèmes comme Stix et MISP.* 2017-2018: SJ Terp commence à travailler sur l'adaptation des outils, des processus et des procédures de sécurité des informations pour l'utilisation de la désinformation.Elle se connecte avec JJ Snow, Pablo Breuer, la collection habituelle de geeks InfoSec et l'équipe Sofwerx pour travailler sur la caractérisation et la lutte contre les incidents hybrides (Cybersecurity Plus Disinformation, notant que les opérations d'information l'ont toujours inclus).

* **Tous ceux qui contribuent à désarmer** (et il y a beaucoup d'entre vous).Merci à tous ceux qui contribuent au désarmement et ont contribué au désarmement au fil des ans.

* **Toi**.Merci d'être ici.

Désarm est licencié en vertu de [CC-BY-4.0](LICENSE.md)