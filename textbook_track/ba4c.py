#!/usr/bin/env python3
# BA4C
# Generate the Theoretical Spectrum of a Cyclic Peptide

aa_to_mass = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
        'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
        'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
        'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}


def mass(peptide):
    """Return total mass of peptide."""
    return sum([aa_to_mass[aa] for aa in peptide])


def subpeptides(peptide):
    """Generate all subpeptides from the cyclopeptide of peptide by taking slices of its dipeptide."""
    dipeptide = peptide + peptide
    subpeptides = []
    for i in range(len(peptide)):
        for j in range(1, len(peptide)):
            subpeptide = dipeptide[i:i+j]
            subpeptides.append(subpeptide)
    subpeptides.append(peptide)
    subpeptides = sorted(subpeptides, key = len)
    return subpeptides


def theoretical_spectrum(peptide):
    """Generate sorted theoretical spectrum of the cyclopeptide of peptide from its subpeptides."""
    return [0] + sorted([mass(s) for s in subpeptides(peptide)])


def check_answer(cyclospectrum, spectrum):
    """Compare multisets of cyclospectrum and spectrum."""
    from collections import Counter
    print(f'cyclospectrum: {cyclospectrum}')
    print(f'spectrum: {spectrum}')
    return Counter(cyclospectrum) == Counter(spectrum)


def main():
    """Generate the Theoretical Spectrum of a Cyclic Peptide."""
    # peptide = 'NQEL'
    # spectrum = [0, 113, 114, 128, 129, 227, 242, 242, 257, 355, 356, 370, 371, 484]

    peptide = 'SDEGDLLHYGWR'

    cyclospectrum = theoretical_spectrum(peptide)
    # print(check_answer(cyclospectrum, spectrum))
    print(*cyclospectrum)


if __name__  == '__main__':
    main()
