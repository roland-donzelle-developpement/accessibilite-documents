# Accessibilité — PDF (PDF/UA-1)

Règles générales dans le SKILL.md. Un PDF accessible est un PDF **balisé**
(tagged PDF) conforme à PDF/UA-1 (ISO 14289-1).

## Principes

- Le PDF doit porter un **arbre de structure** (tags) : `H1`…`H6`, `P`, `L`/`LI`
  pour les listes, `Table`/`TR`/`TH`/`TD` pour les tableaux, `Figure` pour les
  images, `Link` pour les liens.
- **Ordre de lecture** logique dans l'arbre de structure, indépendant de l'ordre
  d'apparition graphique.
- **Langue** du document déclarée (`/Lang`) ; titre dans les métadonnées XMP
  (`dc:title`) et `/Title` ; afficher le titre plutôt que le nom de fichier
  (`DisplayDocTitle` à vrai dans `/ViewerPreferences`).
- Marquer le PDF comme conforme PDF/UA dans les métadonnées XMP.

## Images

- **Informative** : balise `Figure` avec attribut `/Alt` (texte alternatif).
- **Décorative** : baliser en **artefact** (hors arbre de structure) — c'est
  l'équivalent PDF de « décoratif ». Ne pas laisser une `Figure` sans `/Alt`.

## Tableaux

- Vraie structure `Table` avec cellules d'en-tête `TH` (attribut `Scope` :
  `Row`/`Column`) et cellules de données `TD`.
- Pas de tableau de mise en page.

## Pipeline recommandé (génération programmatique)

`fpdf2` pour produire le contenu balisé, puis `pikepdf` pour finaliser/poser les
métadonnées PDF/UA :

1. **fpdf2** : activer le balisage et structurer.
   - Renseigner titre et langue : `pdf.set_title(...)`, `pdf.set_lang("fr-FR")`.
   - Utiliser l'API de structure / les balises de fpdf2 pour émettre H1–Hn, P,
     listes, tableaux, et `Alt` sur les images informatives ; marquer les images
     décoratives en artefact.
2. **pikepdf** : ouvrir le PDF, écrire/compléter les métadonnées XMP (conformité
   PDF/UA, `dc:title`, `dc:language`), s'assurer de `/Lang`,
   `/MarkInfo /Marked true`, et `DisplayDocTitle`.

> Adapter à la version de fpdf2 disponible : vérifier le support du balisage de
> structure dans la version installée et compléter au besoin via pikepdf.

## Vérification

- Vérifier avec un contrôleur PDF/UA si disponible (ex. veraPDF) : structure de
  balises, `/Lang`, titre, alternatives, ordre de lecture, artefacts.
- À défaut d'outil, contrôler programmatiquement la présence de l'arbre de
  structure, de `/Lang`, du `/Title`, et de `/Alt` sur les figures
  informatives ; dérouler la checklist du SKILL.md.
