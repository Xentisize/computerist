from enum import IntEnum
from typing import Tuple, List
from pprint import pprint

Nucleotide: IntEnum = IntEnum("Nucleotide", ("A", "C", "G", "T"))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"


def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if i + 2 >= len(s):
            return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)
    return gene


def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    return False


if __name__ == "__main__":
    g: Gene = string_to_gene(gene_str)
    pprint(g)

    acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
    gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)

    print(linear_contains(g, acg))
    print(linear_contains(g, gat))
    print(acg in g)
