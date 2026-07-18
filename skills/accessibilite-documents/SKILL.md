---
name: accessibilite-documents
description: >
  Applique les règles d'accessibilité (WCAG 2.1/2.2, RGAA, PDF/UA-1) à TOUT
  document produit ou corrigé : Word (.docx), PowerPoint (.pptx), Excel (.xlsx),
  PDF, et pages/courriels HTML. Couvre la hiérarchie de titres (un seul H1,
  H2–H6 sans saut de niveau), les alternatives textuelles (y compris la
  distinction décisive entre image décorative en HTML et en bureautique), les
  ratios de contraste, la structure des tableaux de données, la langue et le
  titre du document, les listes et liens. À utiliser systématiquement dès qu'un
  document doit être accessible — même si l'utilisateur ne dit pas explicitement
  « accessible », « RGAA » ou « WCAG ». Cette skill ne contient AUCUNE charte
  graphique (polices, couleurs de marque, marges, gabarits) : elle est portable
  d'une organisation à l'autre et se combine avec l'identité visuelle propre à
  chaque structure.
---

# Accessibilité des documents

## Objet et portée

Cette skill définit **les contraintes d'accessibilité, et elles seules**. Elle
est volontairement **agnostique vis-à-vis de la mise en page** : elle n'impose
ni police, ni couleur de marque, ni marge, ni logo, ni gabarit. Chaque
organisation branche sa propre identité visuelle par-dessus ces règles. C'est ce
qui la rend **portable** : les règles d'accessibilité sont les mêmes partout
(WCAG, RGAA, PDF/UA), seule la couche graphique varie.

Conséquence pratique sur les couleurs : quand une organisation fournit ses
couleurs de marque, **vérifier** leur contraste contre les seuils ci-dessous.
Si une couleur de marque échoue, le **signaler** à l'utilisateur (et proposer
la nuance conforme la plus proche) plutôt que de remplacer silencieusement la
couleur — la décision sur l'identité visuelle appartient à l'organisation.

## Démarche

À chaque production ou correction de document :

1. Lire d'abord le fichier de référence du format concerné dans `references/`
   (mécanismes techniques propres au format).
2. Produire le contenu en appliquant les **règles universelles** ci-dessous.
3. Avant de livrer, dérouler la **checklist de vérification** finale.
4. Pour les couleurs, utiliser `scripts/verifier_contraste.py` plutôt que de
   juger à l'œil.

Les skills de format (`docx`, `pptx`, `xlsx`, `pdf`) restent utilisées pour la
mécanique de génération ; cette skill se superpose à elles pour la conformité.

---

## Règles universelles

### 1. Hiérarchie de titres

- **Un seul H1** par document : c'est le titre principal, unique.
- Ensuite **H2 → H6 sans saut de niveau** : on ne passe pas de H2 à H4. La
  hiérarchie reflète la structure logique, pas la taille visuelle souhaitée.
- Les titres utilisent de **vrais styles de titre** (style « Titre 1/2/3 » en
  Word, balises `<h1>`–`<h6>` en HTML), jamais du texte simplement mis en gras
  ou agrandi : un lecteur d'écran ne reconnaît que le balisage structurel.
- Ne pas utiliser un niveau de titre pour obtenir un effet visuel ; pour
  l'apparence, c'est le style (couche graphique) qui s'en charge.

### 2. Alternatives textuelles des images

La règle dépend du **rôle** de l'image ET du **format** :

- **Image informative** (apporte de l'information) : alternative textuelle
  concise et pertinente décrivant le contenu OU la fonction. Pas de « image de »,
  pas le nom de fichier.
- **Image complexe** (graphique, schéma, infographie) : alternative courte +
  **description longue** restituant les données/le propos dans le texte ou un
  passage adjacent.
- **Image purement décorative** : à neutraliser pour les technologies
  d'assistance, mais **le mécanisme diffère selon le format** —

  | Contexte | Image décorative |
  |---|---|
  | **HTML / web** | `alt=""` (vide) **+** `role="presentation"` (ou `aria-hidden="true"` selon le cas) |
  | **Bureautique (Word, PowerPoint, Excel, PDF)** | **Marquer l'image comme « décorative »** via le drapeau dédié. **Ne PAS laisser le champ de texte alternatif vide** : un champ vide déclenche une erreur du vérificateur d'accessibilité (« texte de remplacement manquant »). |

  C'est l'erreur classique : transposer la convention web (`alt=""`) dans un
  .docx. En OOXML, l'image décorative se déclare par l'attribut `decorative="1"`
  dans ses propriétés non visuelles (espace de noms `adec` de Microsoft), ce qui
  la fait ignorer par les lecteurs d'écran **sans** champ vide. Détails par
  format dans `references/`.

- Le **texte ne doit pas être présenté sous forme d'image** (image de texte).
  Si inévitable, l'alternative reproduit l'intégralité du texte.

### 3. Contraste des couleurs

Seuils WCAG (niveau AA) — vérifier avec `scripts/verifier_contraste.py` :

- **Texte courant** : ratio ≥ **4,5:1**.
- **Grand texte** (≥ 24 px / 18 pt, ou ≥ 18,66 px / 14 pt en gras) : ≥ **3:1**.
- **Composants d'interface et éléments graphiques porteurs de sens**
  (bordures de champ, icônes informatives, traits de graphique) : ≥ **3:1**.
- Niveau AAA (renforcé, si demandé) : **7:1** texte courant, **4,5:1** grand texte.

Et surtout : **ne jamais transmettre une information par la seule couleur**
(ex. « les cellules en rouge sont en retard »). Doubler par un libellé, un
symbole, un motif ou du texte.

### 4. Tableaux

- Réserver les tableaux aux **données tabulaires** ; **pas de tableau de mise en
  page**.
- Déclarer la **ligne et/ou la colonne d'en-tête** (en HTML : `<th>` + `scope`
  ; en Word/PowerPoint : « ligne d'en-tête » cochée et « répéter en haut de
  chaque page » ; en Excel : table structurée / en-têtes identifiés).
- **Éviter les cellules fusionnées** et les tableaux imbriqués : ils cassent la
  restitution. Si une fusion est indispensable, garder la structure la plus
  simple possible.
- Prévoir un **titre/légende** de tableau quand cela aide à la compréhension.
- Un tableau = une structure cohérente (pas de lignes vides « décoratives »).

### 5. Langue et titre du document

- **Titre du document** renseigné dans les propriétés (≠ nom de fichier) : c'est
  ce qu'annonce d'abord le lecteur d'écran.
- **Langue principale** déclarée (propriété de langue du document / attribut
  `lang`). Marquer les **changements de langue** d'un passage à l'autre.

### 6. Listes

Utiliser de **vraies listes** (à puces ou numérotées via le mécanisme de liste
du format), jamais des tirets ou numéros saisis à la main : la structure de
liste est annoncée aux technologies d'assistance.

### 7. Liens

- Texte de lien **explicite et compréhensible hors contexte** : décrire la
  destination, pas « cliquez ici » ni « en savoir plus » isolé.
- Éviter d'afficher des URL brutes longues comme libellé.

### 8. Typographie et repères

- **Pas de soulignement décoratif** : le souligné est, par convention, réservé
  aux liens. Pour insister, employer le gras (ou un style dédié).
- Ne pas s'appuyer uniquement sur des **caractéristiques sensorielles** (forme,
  position, « le bouton à droite », « le carré vert ») pour désigner un élément.
- **Ordre de lecture logique** : l'ordre dans lequel le contenu est restitué
  doit suivre l'ordre de lecture visuel attendu.

---

## Checklist de vérification finale

Avant de livrer tout document, vérifier :

- [ ] Un seul H1, puis H2–H6 sans saut de niveau, via de vrais styles de titre.
- [ ] Chaque image informative a une alternative pertinente ; chaque image
      complexe a une description longue.
- [ ] Chaque image décorative est traitée selon le format : `alt=""` + rôle en
      HTML ; **drapeau « décoratif »** (champ non vide) en bureautique.
- [ ] Aucune image de texte (ou alternative reprenant tout le texte).
- [ ] Contrastes vérifiés au script : ≥ 4,5:1 (courant), ≥ 3:1 (grand texte /
      éléments graphiques). Couleurs de marque non conformes signalées.
- [ ] Aucune information portée par la seule couleur.
- [ ] Tableaux = données, en-têtes déclarés, fusions évitées, pas de tableau de
      mise en page.
- [ ] Titre du document renseigné ; langue principale déclarée ; changements de
      langue marqués.
- [ ] Listes et liens structurés ; liens au texte explicite.
- [ ] Aucun soulignement décoratif ; ordre de lecture logique.
- [ ] (PDF) Sortie balisée PDF/UA-1 ; (HTML) validation RGAA des critères
      applicables.

---

## Références par format

Lire le fichier correspondant **avant** de produire le document :

- `references/docx.md` — Word : styles de titre, drapeau décoratif OOXML,
  en-têtes de tableau, propriétés de langue/titre.
- `references/pptx.md` — PowerPoint : ordre de lecture des espaces réservés,
  alternatives, images décoratives.
- `references/xlsx.md` — Excel : tables structurées, en-têtes, alternatives,
  pièges du « tout couleur ».
- `references/pdf.md` — PDF/UA-1 : balisage, arbre de structure, pipeline
  fpdf2 + pikepdf, vérification.
- `references/html.md` — Web/courriel : `alt`/`role`, `lang`, `<th scope>`,
  ARIA minimal, critères RGAA.
