# Contribuer

Merci de votre intérêt. Ce projet vise à faire de l'accessibilité des documents
un réflexe systématique, et il s'améliore par les retours du terrain.

## Comment contribuer

- **Signaler un manque ou une erreur** : ouvrez une *issue* en décrivant le
  format concerné (docx, pptx, xlsx, pdf, html), le comportement observé et le
  comportement attendu. Joignez si possible un exemple minimal.
- **Proposer une règle ou une correction** : ouvrez une *pull request*. Reliez-la
  à une *issue* si elle existe.

## Principes à respecter

1. **Pas de charte graphique.** La skill reste agnostique vis-à-vis de l'identité
   visuelle (polices, couleurs de marque, marges, gabarits). On ajoute des
   **règles d'accessibilité**, pas des choix esthétiques.
2. **Portabilité.** Toute règle doit valoir pour n'importe quelle organisation.
3. **Justifier, ne pas asséner.** Préférez « tel réglage parce que telle
   technologie d'assistance en a besoin » aux impératifs sans explication : Claude
   généralise mieux quand il comprend le pourquoi.
4. **Référencer la source** (critère WCAG/RGAA, clause PDF/UA) quand c'est utile.
5. **Web ≠ bureautique.** Attention à la distinction des mécanismes (ex. image
   décorative : `alt=""` en HTML, drapeau « décoratif » sans champ vide en
   bureautique). Ne pas transposer l'un sur l'autre.

## Tests

Si vous modifiez une règle, ajoutez ou ajustez un cas dans `evals/evals.json`
(prompt réaliste + critères de réussite vérifiables) et vérifiez que les cas
existants passent toujours.

## Licence des contributions

En contribuant, vous acceptez que votre apport soit publié sous la licence du
projet, **Apache 2.0** (voir `LICENSE`). Ajoutez l'en-tête SPDX approprié aux
nouveaux fichiers de code (`# SPDX-License-Identifier: Apache-2.0`).
