# Accessibilité — Excel (.xlsx)

Règles générales dans le SKILL.md. Spécificités des classeurs.

## Structure des données

- Organiser les données en **table** (Insertion > Tableau / `ws.add_table` avec
  openpyxl) : la ligne d'en-tête est alors identifiée et annoncée.
- **Une seule table par plage logique** ; éviter plusieurs tableaux collés sans
  séparation, et les lignes/colonnes vides « décoratives ».
- **Éviter les cellules fusionnées** : elles perturbent la navigation au
  clavier et la restitution. Préférer « Centrer sur plusieurs colonnes » si un
  effet visuel est requis, ou repenser la disposition.
- Pas de mise en page « artistique » dans la grille (faux tableaux de
  présentation).

## En-têtes et libellés

- Première ligne = **en-têtes de colonnes** explicites ; si pertinent, première
  colonne = en-têtes de lignes.
- **Nommer les feuilles** de façon parlante (onglets) plutôt que « Feuil1 ».
- Définir la **zone d'impression** et les **titres à répéter** pour les longs
  tableaux.

## Couleur : le piège principal en tableur

- Ne **jamais** coder une information par la seule couleur de cellule
  (« rouge = en retard », « vert = OK »). Doubler par un texte, un symbole, ou
  une colonne d'état explicite.
- Vérifier le contraste texte/remplissage avec
  `scripts/verifier_contraste.py`, y compris pour la mise en forme
  conditionnelle.

## Images et objets

- Images informatives : texte alternatif renseigné.
- Images décoratives : **drapeau décoratif** (comme en Word/PowerPoint), pas de
  champ vide.

## Langue, titre, liens

- Renseigner le **titre** du document dans les propriétés.
- Liens au texte explicite (le texte affiché de la fonction LIEN_HYPERTEXTE doit
  décrire la destination).

## Vérification

Révision > Vérifier l'accessibilité dans Excel, ou contrôle manuel : en-têtes
de table déclarés, absence de fusion, information non portée par la seule
couleur, alternatives d'images.
