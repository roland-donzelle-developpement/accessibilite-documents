#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Contributeurs du projet accessibilite-documents
# SPDX-License-Identifier: Apache-2.0
"""Vérifie les ratios de contraste WCAG entre deux couleurs.

Indépendant de toute charte graphique : on lui fournit les couleurs effectives
du document et il indique les seuils satisfaits. Aucune couleur n'est imposée.

Usage :
    python verifier_contraste.py "#1A1A1A" "#FFFFFF"
    python verifier_contraste.py 26,26,26 255,255,255 --taille grand
    python verifier_contraste.py "#777" "#FFF"            # texte courant par défaut

Formule : luminance relative WCAG 2.x puis (L1 + 0,05) / (L2 + 0,05).
Seuils AA : 4,5:1 (texte courant), 3:1 (grand texte / éléments graphiques).
Seuils AAA : 7:1 (texte courant), 4,5:1 (grand texte).
"""
import argparse
import sys


def _parse_couleur(valeur: str) -> tuple[int, int, int]:
    v = valeur.strip().lstrip("#")
    if "," in v:
        parts = [int(p) for p in v.split(",")]
        if len(parts) != 3:
            raise ValueError(f"Format RGB attendu r,g,b : {valeur!r}")
        return tuple(parts)  # type: ignore[return-value]
    if len(v) == 3:  # forme courte #abc
        v = "".join(c * 2 for c in v)
    if len(v) != 6:
        raise ValueError(f"Hex attendu (#rrggbb ou #rgb) : {valeur!r}")
    return tuple(int(v[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def _luminance(rgb: tuple[int, int, int]) -> float:
    def canal(c: int) -> float:
        s = c / 255.0
        return s / 12.92 if s <= 0.03928 else ((s + 0.055) / 1.055) ** 2.4

    r, g, b = (canal(x) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio_contraste(c1: tuple[int, int, int], c2: tuple[int, int, int]) -> float:
    l1, l2 = sorted((_luminance(c1), _luminance(c2)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def main() -> int:
    p = argparse.ArgumentParser(description="Vérifie le contraste WCAG entre deux couleurs.")
    p.add_argument("couleur1", help="Premier ton (#rrggbb, #rgb ou r,g,b)")
    p.add_argument("couleur2", help="Second ton (#rrggbb, #rgb ou r,g,b)")
    p.add_argument(
        "--taille",
        choices=["courant", "grand", "graphique"],
        default="courant",
        help="courant=texte normal (4,5:1) ; grand=>=18pt/14pt gras (3:1) ; "
        "graphique=composants & éléments graphiques (3:1)",
    )
    args = p.parse_args()

    try:
        c1, c2 = _parse_couleur(args.couleur1), _parse_couleur(args.couleur2)
    except ValueError as e:
        print(f"Erreur : {e}", file=sys.stderr)
        return 2

    r = ratio_contraste(c1, c2)
    seuil_aa = 4.5 if args.taille == "courant" else 3.0
    seuil_aaa = 7.0 if args.taille == "courant" else 4.5

    print(f"Couleurs   : {args.couleur1}  /  {args.couleur2}")
    print(f"Contexte   : {args.taille}")
    print(f"Ratio      : {r:.2f}:1")
    print(f"AA  (>= {seuil_aa:g}:1) : {'CONFORME' if r >= seuil_aa else 'NON CONFORME'}")
    print(f"AAA (>= {seuil_aaa:g}:1) : {'CONFORME' if r >= seuil_aaa else 'NON CONFORME'}")
    if r < seuil_aa:
        print("\n-> Couleur non conforme. À signaler à l'organisation ; ne pas "
              "modifier une couleur de marque sans son accord.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
