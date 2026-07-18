# Accessibilité — HTML (web et courriel)

Règles générales dans le SKILL.md. C'est ici que vit la convention
`alt=""` — à ne pas confondre avec la bureautique (voir SKILL.md).

## Structure et titres

- Un seul `<h1>`, puis `<h2>`–`<h6>` sans saut de niveau.
- Repères de structure : `<header>`, `<nav>`, `<main>` (un seul), `<footer>`.
- Listes via `<ul>`/`<ol>`/`<li>` ; tableaux de données via `<table>`.

## Images : informatives vs décoratives

- **Informative** : `alt` décrivant le contenu/la fonction.
  ```html
  <img src="schema.png" alt="Parcours du chien guide : ...">
  ```
- **Décorative** : `alt=""` **vide** (présent mais vide), idéalement complété
  par `role="presentation"` ; pour une image de fond purement esthétique,
  passer par CSS (`background-image`) ou `aria-hidden="true"`.
  ```html
  <img src="filet.svg" alt="" role="presentation">
  ```
  > C'est l'inverse de la bureautique : ici le champ alt **doit** être vide pour
  > signaler le caractère décoratif. En .docx/.pptx/.xlsx/PDF, on pose un drapeau
  > « décoratif » sans vider le champ.

- **SVG informatif** : `role="img"` + `<title>` (et `aria-labelledby`).

## Tableaux

```html
<table>
  <caption>Intitulé du tableau</caption>
  <thead>
    <tr><th scope="col">Colonne A</th><th scope="col">Colonne B</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row">Ligne 1</th><td>…</td></tr>
  </tbody>
</table>
```
- `<th>` + `scope` (`col`/`row`) pour les en-têtes ; `<caption>` pour l'intitulé.
- Pas de `<table>` pour la mise en page (utiliser CSS Grid/Flexbox).

## Langue et titre

- `<html lang="fr">` ; changement de langue ponctuel via `lang` sur l'élément
  concerné.
- `<title>` de page renseigné et signifiant.

## Liens et formulaires

- Texte de lien explicite hors contexte (pas « cliquez ici »).
- Chaque champ de formulaire associé à un `<label for>` ; messages d'erreur liés
  au champ (`aria-describedby`).

## Contraste et couleur

- Vérifier avec `scripts/verifier_contraste.py` (≥ 4,5:1 courant ; ≥ 3:1 grand
  texte et composants d'interface / éléments graphiques).
- Aucune information par la seule couleur ; visibilité du focus clavier.
- Pas de soulignement décoratif (le souligné signale un lien).

## ARIA — principe de sobriété

N'employer ARIA que lorsqu'aucun élément HTML natif ne convient : « pas d'ARIA
vaut mieux qu'un mauvais ARIA ». Préférer les éléments sémantiques natifs.

## Spécificités courriel HTML

- Compatibilité variable des clients : rester sur du HTML simple et sémantique,
  `lang` sur la racine, `alt` correct sur les images, contrastes vérifiés.
- Éviter de porter le sens uniquement par des images : prévoir une version texte.

## Vérification

Contrôler les critères RGAA applicables (images, structure, couleurs, tableaux,
liens, langue) ; outils possibles : validateur HTML, extensions d'audit
d'accessibilité, et la checklist du SKILL.md.
