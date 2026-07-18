# Accessibilité — PowerPoint (.pptx)

Règles générales dans le SKILL.md. Ici, les spécificités des diapositives.

## Titre de diapositive et structure

- Chaque diapositive a un **titre** (espace réservé « Titre »). C'est l'équivalent
  du repère de navigation : un lecteur d'écran parcourt les diapositives par leur
  titre. Si un titre doit être masqué visuellement, le conserver dans la
  structure plutôt que le supprimer.
- Utiliser les **espaces réservés (placeholders)** des dispositions plutôt que
  des zones de texte libres : ils portent la sémantique et l'ordre.

## Ordre de lecture

- L'ordre de lecture suit l'ordre des objets dans l'arbre de la diapositive
  (volet « Ordre de lecture » / « Sélection »). Le **vérifier** : l'ordre visuel
  et l'ordre de restitution doivent coïncider (titre, puis contenu, puis
  éléments secondaires).

## Images : informatives vs décoratives

Même logique qu'en Word, dans `p:nvPicPr > p:cNvPr` :

- **Informative** : attribut `descr` renseigné.
- **Décorative** : poser le **drapeau décoratif** (extension
  `adec:decorative val="1"`, namespace
  `http://schemas.microsoft.com/office/drawing/2017/decorative`) dans `p:cNvPr`,
  et **ne pas** laisser un champ alternatif vide. Interface : case « Marquer
  comme décorative » de la boîte « Texte de remplacement ».

Avec python-pptx, le alt text informatif se pose via le XML de la forme :
`shape._element._nvXxPr.cNvPr.set("descr", "...")`. Le drapeau décoratif
s'injecte en ajoutant l'extension `adec:decorative` à `cNvPr` (pas d'API dédiée).

## Tableaux et graphiques

- Tableaux : ligne d'en-tête identifiée ; structure simple, pas de fusions.
- Graphiques : fournir une **alternative/description** restituant les données
  clés ; ne pas coder l'information uniquement par la couleur des séries
  (ajouter étiquettes, motifs ou valeurs).

## Contraste

- Vérifier texte sur fond **et** texte sur image de fond avec
  `scripts/verifier_contraste.py`. Sur photo de fond, prévoir un voile/aplat
  pour garantir le ratio.

## Listes, liens, couleurs

- Listes via les niveaux de puces natifs.
- Liens au texte explicite.
- Aucune information par la seule couleur ; pas de souligné décoratif.

## Vérification

Révision > Vérifier l'accessibilité dans PowerPoint, ou contrôle manuel via la
checklist du SKILL.md (titres de diapositives, ordre de lecture, alternatives,
contraste).
