# Skill Accessibilité des documents

Une skill pour Claude qui applique les règles d'**accessibilité** (WCAG 2.1/2.2,
RGAA, PDF/UA-1) à tout document produit ou corrigé — Word (.docx),
PowerPoint (.pptx), Excel (.xlsx), PDF, et pages/courriels HTML.

Elle couvre la hiérarchie de titres, les alternatives textuelles (avec la
distinction décisive entre image décorative en HTML et en bureautique), les
ratios de contraste, la structure des tableaux de données, la langue et le titre
du document, les listes et les liens.

## Pourquoi ce projet

L'accessibilité numérique est un bien commun : un document accessible bénéficie
à tout le monde, et d'abord aux personnes en situation de handicap. Cette skill
vise à rendre cette conformité **systématique** et **reproductible**, quelle que
soit l'organisation qui l'utilise.

## Principe : portable, sans charte graphique

La skill ne contient **aucune identité visuelle** — ni police, ni couleur de
marque, ni marge, ni gabarit. Elle ne porte que les règles d'accessibilité, qui
sont les mêmes partout. Chaque organisation branche sa propre charte par-dessus.
C'est ce qui la rend portable d'une structure à l'autre.

Conséquence sur les couleurs : la skill **vérifie** les couleurs fournies contre
les seuils de contraste et **signale** une couleur de marque non conforme, sans
jamais la remplacer d'autorité — la décision sur l'identité visuelle appartient
à l'organisation.

## Contenu

```
skills/accessibilite-documents/
├── SKILL.md                  Règles universelles + checklist de livraison
├── references/               Mécanismes techniques par format
│   ├── docx.md   
│   ├── pptx.md   
│   ├── xlsx.md   
│   ├── pdf.md   
│   └── html.md
└── scripts/
    └── verifier_contraste.py Calcul des ratios de contraste WCAG
docs/instructions-organisation.md  Consigne prête à coller (déclenchement)
evals/evals.json                   Jeu de tests de départ
```

## Installation

### Sur Claude.ai (Pro, Team, Enterprise)

Compressez le dossier `skills/accessibilite-documents/` en `.zip`, puis
téléversez-le dans Réglages → Capacités → Skills (l'activation des skills et de
l'exécution de code peut être requise selon le forfait). Sur Team/Enterprise, un
administrateur peut le **provisionner pour toute l'organisation** depuis les
paramètres d'organisation : il devient alors disponible pour tous les membres.

### Sur Claude Code (marketplace de plugins)

```
/plugin marketplace add VOTRE-COMPTE/VOTRE-DEPOT
/plugin install accessibilite-documents@accessibilite-documents
```

## Faire en sorte qu'elle s'applique à tous les documents

Le déclenchement d'une skill dépend de sa **description** (large et explicite,
déjà calée ici), pas d'un réglage. Pour fiabiliser son application sur toute
production de document — y compris les demandes implicites — collez la consigne
de `docs/instructions-organisation.md` dans les instructions de votre
organisation ou de votre projet. Voir ce fichier pour le détail.

## Tester

`evals/evals.json` contient un jeu de prompts de départ et leurs critères de
réussite. Lancez-les après installation, en variant formulations explicites
(« rends ce document accessible ») et implicites (« prépare-moi cette note »),
pour vérifier que la skill se déclenche dans les deux cas.

## Contribuer

Les contributions sont bienvenues : voir [CONTRIBUTING.md](CONTRIBUTING.md).
Ouvrez une *issue* pour signaler un manque ou proposer une règle, ou une
*pull request* pour une modification.

## Licence

Projet sous licence **Apache 2.0** (voir [LICENSE](LICENSE) et [NOTICE](NOTICE)),
appliquée à l'ensemble — documentation comme code. C'est la licence la plus
répandue dans l'écosystème des skills, ce qui facilite l'adoption et la
contribution. Chacun peut réutiliser, modifier et redistribuer, y compris à des
fins commerciales, en conservant l'attribution et l'avis de licence, avec une
concession de brevets explicite.

Les référentiels d'accessibilité mobilisés (WCAG, RGAA, PDF/UA) restent la
propriété de leurs éditeurs ; ils ne sont pas redistribués ici.
