# Accessibilité — Word (.docx)

Mécanismes techniques propres à Word. Pour les règles générales, voir le
SKILL.md. Rien ici ne concerne la charte graphique : on agit sur la
**structure**, pas sur l'apparence.

## Titres

- Appliquer les **styles** « Titre 1 », « Titre 2 », … (`w:pStyle` =
  `Heading1`, `Heading2`, …), pas une mise en forme manuelle gras/taille.
- Un seul « Titre 1 ». Le titre visible du document peut aussi être porté par le
  style « Titre » (Title) ; dans ce cas le premier niveau de structure reste un
  unique H1 logique.
- Pour modifier l'apparence d'un niveau, **redéfinir le style** (couche
  graphique de l'organisation) — ne pas rétrograder/sauter de niveau pour des
  raisons visuelles.

## Images : informatives vs décoratives

Dans l'XML d'un dessin (`w:drawing`), les propriétés non visuelles
`wp:docPr` portent le texte alternatif (`descr`) et le titre (`title`).

- **Informative** : renseigner `descr` avec une alternative pertinente.

  ```xml
  <wp:docPr id="3" name="Image 3" descr="Schéma du parcours du chien guide : ..."/>
  ```

- **Décorative** : **marquer le drapeau décoratif**, et NE PAS se contenter d'un
  `descr` vide. Le drapeau se pose via l'extension Microsoft
  (`http://schemas.microsoft.com/office/drawing/2017/decorative`) :

  ```xml
  <wp:docPr id="4" name="Filet décoratif 4">
    <a:extLst xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
      <a:ext uri="{C183D7F6-B498-43B3-948B-1728B52AA6E4}">
        <adec:decorative val="1"
          xmlns:adec="http://schemas.microsoft.com/office/drawing/2017/decorative"/>
      </a:ext>
    </a:extLst>
  </wp:docPr>
  ```

  Dans l'interface Word, cela correspond à la case « Marquer comme décorative »
  de la boîte « Texte de remplacement ». Résultat : l'image est ignorée par les
  lecteurs d'écran **sans** déclencher l'erreur « texte de remplacement
  manquant » qu'un champ vide provoquerait.

### Avec python-docx

`python-docx` n'expose pas directement le alt text ni le drapeau décoratif. Deux
voies :

1. **Alt text informatif** : après insertion, éditer `docPr` de l'inline shape :

   ```python
   from docx import Document
   doc = Document("doc.docx")
   pic = doc.add_picture("schema.png")
   # accéder au docPr de l'inline shape correspondante
   inline = doc.inline_shapes[-1]
   docPr = inline._inline.docPr
   docPr.set("descr", "Schéma du parcours : ...")
   ```

2. **Drapeau décoratif** : injecter l'extension `adec:decorative` dans `docPr`
   via `lxml` (l'élément n'a pas d'API dédiée). Construire le sous-arbre
   `a:extLst > a:ext > adec:decorative val="1"` et l'ajouter à `docPr`.

Si la manipulation XML devient lourde, post-traiter le `.docx` (qui est un ZIP)
en éditant `word/document.xml`, puis revérifier avec le Vérificateur
d'accessibilité de Word.

## Tableaux

- Cocher **« Ligne d'en-tête »** : en XML, marquer la première ligne avec
  `<w:tblHeader/>` dans `w:trPr`, ce qui la fait répéter et l'identifie comme
  en-tête.
- Éviter `w:gridSpan` / `w:vMerge` (fusions) autant que possible.
- Pas de tableau pour mettre en page du texte : utiliser des sections,
  colonnes ou tabulations.
- Donner un intitulé au tableau (légende) quand utile.

## Langue et titre du document

- **Titre** : propriété de cœur du paquet (`docProps/core.xml`,
  `dc:title`). Avec python-docx : `doc.core_properties.title = "..."`.
- **Langue** : style par défaut ou `w:lang` ; définir la langue principale et
  marquer les passages dans une autre langue avec leur propre `w:lang`.

## Autres points

- **Listes** : vrais styles de liste (List Bullet / List Number), pas de tirets
  saisis.
- **Liens** : texte explicite via le champ d'affichage de l'hyperlien.
- **Pas de soulignement décoratif** : réserver le souligné aux liens.

## Vérification

Si l'environnement le permet, faire tourner le Vérificateur d'accessibilité de
Word (Révision > Vérifier l'accessibilité) ; sinon, dérouler la checklist du
SKILL.md et contrôler manuellement la structure XML.
