# Automation BDD Python Quickstart

Ce projet template vous permettra de commencer rapidement à créer la glue entre les scénarios BDD issus de la phase de _BDD formulation_ et les tests logiciels.

Il existe plusieurs packages python capables de supporter cette glue, les plus connus étant [pytest-bdd](https://pytest-bdd.readthedocs.io/en/stable/) et [behave](https://behave.readthedocs.io/en/stable/). Le parti pris est ici celui de [pytest-bdd](https://pytest-bdd.readthedocs.io/en/stable/) car vous permettra de réutiliser tout ce que vous savez déjà sur [pytest](https://docs.pytest.org/).

## Pré-requis

Il vous faut une version de Python>=3.7.

## Installation de [pytest-bdd](https://pytest-bdd.readthedocs.io/en/stable/)

Vous n'utilisez pas un environnement virtuel Python ? On ne vous en voudra pas, mais ce serait top de vous y intéresser.

Environnement virtuel ou non, il s'agit de se placer dans le dossier projet _python_ du repository puis de saisir la commande suivante :

```
> pip install -r requirements.txt
```

## Vérifier que ça fonctionne

Il suffit de saisir la commande suivante :

```
> pytest
```

Vous pouvez essayer, c'est sans danger. Ce sera avec ce mot _pytest_ que vous lancerez tous vos tests.

## Comment ça marche ?

Les scénario écrit au format Gherkin sont placés dans le dossier _tests/features_.

Les steps quant à eux se trouvent dans des fichiers python dans le dossier _tests/steps_, comme vous le feriez normalement avec [pytest](https://docs.pytest.org/).

Allez, c'est parti regardez dans ces fichiers comment faire la glue !

## Ah oui, un dernier détail

Pour éviter certaines galères avec les _Scenario Outlines_ vérifiez bien que l'encodage de vos fichiers sont en UTF-8.
