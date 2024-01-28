# Cadre TTP (tactiques, techniques et procédures) de désinformation de DISARM

DISARM est un cadre conçu pour décrire et comprendre les incidents de désinformation. DISARM fait partie des travaux visant à adapter les pratiques de sécurité de l’information (infosec) pour aider à suivre et à contrer la désinformation et d’autres atteintes à l’information, et est conçu pour s’adapter aux pratiques et outils de sécurité de l’information existants.

Le style de DISARM est basé sur le[MITRE À&Cadre CK](https://github.com/mitre-attack/attack-website/). Les modèles STIX pour les objets DISARM sont disponibles dans le[Dépôt DISARM_CTI](https://github.com/DISARMFoundation/DISARM_cti)- ceux-ci facilitent la transmission des données DISARM entre les ISAO et des organismes similaires utilisant des normes telles que TAXII.

## Qu'y a-t-il dans ce dossier

DOCUMENTATION DE DÉSARMEMENT :

-   [DÉSARM_DOCUMENTATION](DISARM_DOCUMENTATION): guides d'utilisation DISARM, guides de conception et documentation TTP plus détaillée.
-   [DISARM_HISTORY](DISARM_DOCUMENTATION/DISARM_HISTORY): modèles et rapports antérieurs.

DÉSARMER LES CADRES :

-   [Cadre de l’équipe rouge DISARM](generated_pages/disarm_red_framework.md)- TTP créateurs de désinformation, classés par étape tactique. Il s'agit du "DISARM Framework" classique fourni avec MISP. Le[cliquable](generated_files/disarm_red_framework_clickable.html)La version sert à créer rapidement des listes de TTP.
-   [Cadre de l’équipe bleue DISARM](generated_pages/disarm_blue_framework.md)- TTP de réponse à la désinformation, classés par étape tactique. Il s’agit de contre-mesures, classées selon les premières étapes tactiques dans lesquelles elles sont susceptibles d’être utilisées.

DÉSARMER LES OBJETS : toutes les entités utilisées pour créer les frameworks Red Team et Blue Team :

-   [Étapes](generated_pages/phases_index.md): regroupements de tactiques de niveau supérieur, créés pour que nous puissions vérifier que nous n'avons rien manqué
-   [Tactique](generated_pages/tactics_index.md): étapes qu'une personne à l'origine d'un incident de désinformation est susceptible d'utiliser
-   [Techniques](generated_pages/techniques_index.md): activités visibles à chaque étape
-   [Tâches](generated_pages/tasks_index.md): les choses qui doivent être faites à chaque étape. En langage pablo, les tâches sont les choses que vous faites, les techniques sont la façon dont vous les faites.
-   [Compteurs](generated_pages/counters_index.md): contre-mesures pour DÉSARMER les TTP.
-   [Types d'acteurs](generated_pages/actortypes_index.md): ressources nécessaires pour exécuter des contre-mesures
-   [Types de réponses](generated_pages/responsetype_index.md): les catégories de cours d'action que nous avons utilisées pour créer des compteurs
-   [Métatechniques](generated_pages/metatechniques_index.md): un regroupement de niveau supérieur pour les contre-mesures
-   [Incidents](generated_pages/incidents_index.md): descriptions d'incidents utilisées pour créer les frameworks DISARM

Il existe un répertoire pour chacun d'entre eux, contenant une fiche technique pour chaque entité individuelle (par ex.[technique T0046 Optimisation des moteurs de recherche](generated_pages/techniques/T0046.md)). Il y a aussi un répertoire[fichiers_générés](generated_files)contenant tous les fichiers (CSV, sqlite, etc.) que nous générons à partir des tableaux ci-dessus.

## Mise à jour du DÉSARMEMENT

Changements majeurs : toute modification majeure apportée aux modèles DISARM est approuvée par la Fondation DISARM.

Changements mineurs : nous aimons toutes les suggestions d'amélioration, commentaires et offres d'aide - contactez-nous en utilisant[ce formulaire Google](https://docs.google.com/forms/d/e/1FAIpQLSdZuyKFp1UZzk6qUE4IN1O14HaJ-F4TH9thxR3hrRU-Mu7QUQ/viewform). (Nous revenons également sur les listes de problèmes précédentes :[Liste des problèmes de l'AMITT](https://github.com//DISARM/issues)et[Liste des problèmes de mésinfosec](https://github.com/misinfosecproject/DISARM_framework/issues))

Utilisation de vos propres ensembles de données : DISARM est open source. Si vous souhaitez faire votre propre travail avec les données DISARM, celles-ci vous aideront :

-   toutes les données de base pour DISARM sont dans le répertoire[DISARM_MASTER_DATA](DISARM_MASTER_DATA). Cherchez le[DISARM_FRAMEWORKS_MASTER.xlsx](DISARM_MASTER_DATA/DISARM_FRAMEWORKS_MASTER.xlsx)tableur. Celui-ci contient les tactiques, techniques, tâches, phases et compteurs des créateurs de désinformation.

-   Le[DÉSARMER Guide TTP](https://docs.google.com/document/d/1Kc0O7owFyGiYs8N8wSq17gRUPEDQsD5lLUL_3KGCgRE/edit#)contient des informations plus détaillées sur chaque technique.

-   Le code pour créer toutes les fiches HTML se trouve dans le répertoire[CODE](CODE): vous aurez besoin de generate_DISARM_pages.py et de tous les fichiers modèles.

Si vous disposez de votre propre version de ce référentiel et mettez à jour DISARM_FRAMEWORKS_MASTER.xlsx, en tapant "python generate_DISARM_pages.py" mettra à jour tous les fichiers ci-dessus à partir de celui-ci. Si vous souhaitez mettre à jour le fichier DISARM github, les bases de données DISARM et le bundle DISARM STIX en même temps, exécutez le fichier generate_DISARM_pages.ipynb depuis Jupyter.

## Qui est responsable du DÉSARMEMENT (et un peu d'histoire)

-   Maintenant:**[Fondation DÉSARMER](https://www.disarm.foundation/)**maintient et met à jour la famille de modèles DISARM : DISARM-STIX, le cadre DISARM Red (de création de désinformation) et le cadre DISARM Blue (de contre-mesures et d'atténuation de la désinformation).

-   En 2022,**Equipes MITRE, CRF et CogSecCollab**a travaillé pour fusionner les modèles de framework AMITT et SPICE pour créer les frameworks DISARM, dirigés par SJ, Pablo, Mark et Jon Brewer (qui nous maintient tous organisés). Cette équipe a créé la FONDATION DISARM.

-   2020?**[MITRE](https://www.mitre.org/)et[CRF : Université internationale de Floride](https://www.fiu.edu/)**a dérivé le modèle AMITT RED pour créer le cadre SPICE, dirigé par Mark Finlayson de la CRF.

-   2020-2022:**[CogSecCollab](http://cogsec-collab.org/)**maintenu et mis à jour les modèles AMITT originaux. CogSecCollab est l'organisation à but non lucratif issue de MisinfosecWG. CogSecCollab a utilisé AMITT dans les réponses Covid19 de la Ligue CTI et l'a testé lors d'essais avec les unités de désinformation de l'OTAN, de l'UE et de plusieurs autres pays. SJ Terp et Pablo Breuer détenaient l'autorité de conception des modèles AMITT.

-   2018-2020:**[MisinfosecWG](https://github.com/credcoalition/community-site/wiki/Working-Groups)**, alias le groupe de travail Misinfosec de la Credibility Coalition, a créé les cadres DISARM originaux. La Credibility Coalition est un choix naturel pour le volet normes (car en 2017, chaque groupe - médias, militaires, publicité, public, etc. - avait un ensemble de mots différent pour désigner les éléments de désinformation), et puisque SJ était là lorsque la Credibility Coalition a été créée. créés, ils étaient un lieu naturel pour faire ce travail. Le Red Framework a été lancé en décembre 2018, affiné lors d'un séminaire Misinfosec de la Credibility Coalition et mis en forme par SJ et Pablo chez SOFTWERX autour d'une quantité déraisonnable de café ; le Blue Framework a été lancé comme un ensemble de contre-mesures potentielles de désinformation, lors d'un séminaire de la Coalition Misinfosec en novembre 2019. Ce travail a été dirigé conjointement par SJ et Christopher Walker ("Walker") de Marvelous.AI, rejoints plus tard par John Gray de MentionMapp, mais il s'agissait en réalité d'un effort de la communauté CredCo, avec les contributions de nombreuses personnes et lieux, y compris Roger Johnston, qui nous a rejoint après notre présentation à ATT&CKcon, et a commencé à créer de nombreux outils et connexions à des systèmes comme STIX et MISP.

-   2017-2018 : SJ Terp commence à travailler sur l'adaptation des outils, processus et procédures de sécurité de l'information à l'utilisation de la désinformation. Elle s'associe à JJ Snow, Pablo Breuer, à la collection habituelle de geeks de la sécurité de l'information et à l'équipe SOFWERX pour travailler à la caractérisation et à la lutte contre les incidents hybrides (cybersécurité et désinformation, sachant que les opérations d'information l'ont toujours inclus).

-   **Tous ceux qui contribuent à DISARM**(et vous êtes nombreux). Merci à tous ceux qui contribuent à DISARM et qui ont contribué à DISARM au fil des ans.

-   **Toi**. Merci d'être ici.

DISARM est sous licence[CC-BY-4.0](LICENSE.md)
