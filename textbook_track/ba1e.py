#!/usr/bin/env python3
# BA1E
# Find Patterns Forming Clumps in a String


def make_kmers(dna, k):
    """Make all possible kmers of size k from a DNA string."""
    return [dna[i:i+k] for i in range(len(dna) - k + 1)]


def find_patterns_forming_clumps(genome, k, L, t):
    """Find set of patterns forming (L, t)-clumps in genome by
    sliding window of size L over genome and counting kmers that occur t times."""
    from collections import Counter
    patterns = []
    for i in range(len(genome) - L + 1):
        dna = genome[i:i+L]
        kmer_counts = Counter(make_kmers(dna, k))
        for kmer, count in kmer_counts.items():
            if count == t:
                patterns.append(kmer)
    # return set so that duplicates are removed
    return set(patterns)


def main():
    """Find Patterns Forming Clumps in a String."""
    # genome = 'CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC'
    # k = 5
    # L = 75
    # t = 4

    genome = 'GGGACATACGTTATACATTACTTAAACGGGCTGTTTTATGGTGCGAATTAAATGCTTTTGCGTAGAATCATGTTTAGCGCGTTCTAATGCCCTCGTCGGCAGTAGGCGTCCACGGCGCGAATTAGACGCGTTCTGCAGGCGTAGGTCCGCAAATCGAGCATGGGCTACGCATTGTATGGGGCCACACAGCAGCCTGCCTAAGCTATTGAACTCCAGGTGTTCCTGGGGACCTACCCGGTGAAGATAATTGGCCAACGGCAGTTGCGGATTCAAAGGACAAGGACACGGCTAGTAACTGTTCGCTAGATGGCCGTGCTGTTGTGTACCGGTAGGGTGTTGTTCCCAAAACCTCGACCCCGGGAGCATCTGCCTATACGATTGCCAACAGATTGACCCACTCAGCTCGTTTGTTCAATAGTTAAACTCCTCGGGATTTTGGCAGCGACCTGTAAGTAGCCGCGTGTGCAACAACACGCAGGTGAGGTATTACATCGGCACGACCGGTACGGGTCGAGTCGCCGCGCCCAGATGAGTACAGGTTTCACGACGCGGTGACAGAGGAGCCTGGGTGCTGTAACCTATTAAAGTGACAATCATCTGACATCCGAAGTTACCCTCCGGAGATTGATAGGCTCGGCTGAGTCTTGGGATGGTCTCCGGGGTTCAGTCGCGACGGCACAATCCGTGTTTTTAACGCCAGGCCCCCATCGGCCGCTCACACACGACGAGGTGAGAATACACGGAGTTATATTGTCGAATCCAGTAAAGAATAGCTATGTGCATGTGCTTAGACGGGACCGGACATATTCTGCTCGCAAATGTCATCCTGTTCCAATCCGTACAATACAGCGATGTTCCACTATATACTGATAAGACCGGAAGGGTCCCTCGAGTACCTGACCTGAACCGCGAGCAATTCGAGATTACATATTAGGGTTGCCGACGGACCATACTGACTGTGTGACCTCACATCGGGAGCGTTTGTGACCTCGTGGGGGTAGGTGTGACCTCATTCGCCACACGGTTACGCTTAAAGAGAAGAACAGGCACGGTGGCTTATCCTCATGTCGTCGTCTGTGGCTTATGGCTTATACCTCAGCAACCTCACTAGGCGTGGTACTGCATATGTGGCTTATACCTCAGTGGCTTATACCTCGATACACTTCCTTCGCGTGGTGTGGCTTATGTCAGTATCTGTGACCTCCCTCACTTCCCCAACTGGTGGCTTATTCCGTGGCTTATACCGTGGCTTATCCTCGCTCTTGTGGCTTATACGATCTGTGGCTTATCTGACCTGTGGCTTATACGTATTCGCGTATTCGCGCTACGTATTCGAAGGTTGTCTGTGACCTCGAAGTGGCTTATGGTGGCTTATTGGCGTGGCACGTATTCGGCTTATTTCTACGTACGTATTCGGTGGCACGTATTCGGTGAACGTATTCGATGTAAGTGCGGGCCACTGTGACCTCGACTTAAGCTTCGTGTGACCTCGCGCGTTAGTGAGCTGTGACCTCGCACGTATTCGTATTCGGTGACCGTGGCTTATCTCTGGTGCTTGGTGGCTTATTTATAAGGCAGATAGCGTGGCTTAGTGGCTTATTAAACGTATTCGCTGTGGCTTATTACTTCATAAAACGTATTCGCAGGTCAATACCCAACTGCCCTCTCCAAGTTTGCGCTGGTAACGTATTCGGTATTCGACACGTATTCGTGGGACGTATTCGAAACGTCTAGCAACGTATTCGCGGTCTTTCCGTTAATGGAACGCGACGTATTCGGACGCCAAGCAAGTACGACACGGACATGTGGACGTATTCGGGAGACGTATTCGGTTACGTATTCGTATTCGATTAAGGGGACGTATTCGACGTACGTATTCGAAAGGGGCTACGATGGTACCCTACCGTGAGACGTACGTGGTCACGGACTCTCGAGTAATTTGATGTGGAACATACAGAGAGTCGGCGGAGTAATTAAAGTGTGTAACGCTGGTCAGTTTGTTACGAGCAAATCCCGTGTGGGTATCTGGCGGACCCTGCACGAAGTGCCCTTACACTCAAGATGCCGGTAATACTAATACTGTAGACAGCGGCCACTAGAAATGCTTGCGCTAGCAGTCCATATCTACCAATCTCTGCGGGTGAAATCTTCCTGAGACGCAATGGTCATGCTTAGGCCGGGTCCTCACACGCGTGGTTTTCCCATAAATACTGTCTCACCTGACAGATGGCGAAGTTTGATCATTTAAAAAACCACGACTGTCTTCTGGGTCACAACCGGCGTATATACAAACCAATCTCTCGACATTACTATCCGCACGGCGAAATCCAAGTTTGAGGTGGACGAAGGGGCTCAAGTAGGGAGCAAGGCAGATCCGAGTCGCAAGAAGCTCTGGACCCACCGGCACTGTCATCCCCATGCTATACTGGATCAGCGCCGCATTCAACTCAGCTGGCTTGGGTGCGTATCGCCAGATGACATTTAGAAGCGCCTTCCATCTGAACTATCAACAAAATGGTTGTTCCCGTGACTGGGGCAGCTCCAGGGGCTAGCGGCCAGGGGTATATCCTTAGCAAATCCCCTTCCGGCCCTTAATGTACCCTGACGTGAATTAGTGCCCCGTCAATTGTGCGCGGGCACACTGGGAAATACCGCGGATGAGATATACACTGGTCGGAATTAGTCCAGCTAGGACCGCTCCGCACACGGTTCCTAAGAGACTTGCGTGCACATACGGACAAAGCTTCTACATCAACGGCACCTAGGGAATATAGCAAGGGACACAGAGCTCGACCACGTTAGGATACTATTGAGTTAGGCCTAGCTACTATCAGTACTTTTGAGAGGCGCCATTAACGCTGGTCTGCAGAGACGGGTACTCCGTTCGACAATAAAGTGCGAGCTCGAGCAGTGATGCTGGGGCATATCACCGCTCTTCTACTCATTTATACAAATCTCTATGCCCACTAGACGACTTGTTCCGCGGCTCGCTGGGGCGGACGCCCTAGAGTTCAAAGTAGGCGTTTTCTAGGCACGGGAGGCTAGGGTTGGAGGAGGAAGGCAACGACTGGTCTGGCGGTTCACCAATTGGCCATACATCTAATCCTGCTGGTCGGCGCGACGCATGCAAGCGACTCGCAACCTGTTGCTCTTGCATAACCGCCCGTCTGCGGGTCGGTTGGTCCTTCCCATTTAATAGGATCTTCGTGGCGAGAGGGTAGGCAAGTTTTTAAGTACGAAATCGCCTCAAAAATTGACTCCGGTTCCGCCTCTATGAATCGTACTTCTATGGCTTTTAGCTAACAGCCGCCGACACTGCAACATACTTCGATAGTGTGCGATTCCGTTGTTGTGAACTGCTATGTGAAAAAAGCGGGGAGACATACGGAAACGTAGGGACCAGGGGCAGACTAAATTCCTATATATGGGCTGCGTAGGGGTAGATATAATAACACGGGGTGTTTGTGGCACCAGTTCTTCCATTCAACTCTGGTGCATGAACGCCATGTCAGGCTCAAAAGTTCGAACCTGCGCAAGTCCACAGTAGGAGAAGCTATGTCGAACGTGGACGGTGGGGTGTGAACGTGCACCTGAAGCTGCACTGTTCGCCAATATAAGAACAGTCTCTGTGCCACTTTGGTAATTCCGTCTGTTTGGTCAGCTCGTAAATAGTAACATTGGTGTCCAGATTGTTGGGGTGTATCGTACAAGTTAATCGGCTTGATCTTGCGGTACGGGACAACACAAAATAGATGAAGGACACCAATCCACTTCGCCGCAGAGGAATTATCCACGGGTACACTTATGATAATTCGCGGTCTGACGATTGACATGGGCACGGTATCTTCTATTTCTTCGTTATGAATTAGACCCACGAGGACATAAAGCGGAGTTGGAGATTGCTGCTATCGTCCGGGAGAGGTATTCCATCTCAAGCTAACGAAGCGATTCCATGTCGGAAAGGATTTATTGATGTTCTCACGAGTCCCGGACAGGTTACAGTAAGATGTAGGGTCCTCTAAACATAATAGTTATTGCTCGGTTGCTGAGCCTACAGCCGGGCGGTTAAACTTGTATTATTCCTACTCCAGGAGTACTTAGTGTGTGTTACCCGGGAGCGGCACCCGTATATAGAATCCATGGCTCTTTATCCCGCGGTACTCTGATTGGCCGAACTTTAATTAGCGCAAGGTCCCACTACGTGCAAAGTGCACAAGTGAAATCTTTAATCCATCTGCATCGCTCGTAGCCGACTGTGAATCTACAGCTGCTCACTCGACGGGCTGAGTCCCCAGTTGAAACCGGGGCATACGCTTTGTGCCACACATGCCTGAGCGCACCACCATGTCTAAATAGAAATCAAAAGGAACTGGGACTAAAGGGCGCGTTCGGCGATAACCCCTACGCATTCGGGAGGTACGTGGATATTCTACCTGTTCTCGGTCATTCTTACATATCAAGGTCCGTACACTTGCGGGGCAACTTATTTCTAACTGGCCCCACGTGGAAATCACACACAAAATTTAGCTGTATTGCATAGGAAACAGGCTCCTGATATTAGTTGCTTTCAGCTCCCGTAATCAATGAAATTCGGAAAAGGCTCATTATTGATGCCAAAAGAATAGGGCTACCTCCTTTTGTCAGCGAGGCATCGCTGCCGAGCATAAGAACTTCGGACCCTGTCTAGCGAATCCATCCGGACATCCATCGTTTATGACGAAGTGCCACCACCTAGAAAGGCGCGGCGGTGTCACCGTATGGCAATTGGCAAAAACCCTGCTTGCAAGTCGCACGGGATGAGGCGTCTCACTGCTAATAACTGCAGCTTACTGGGTTTCTAGGTCAACAGTAGCCGTTGCGGGACCGGGTGCAAAGGGGCGGCCTGGCCTGGTTTAGTCTGATGTGACAGGATACGTACTGTATATGGTTGTTAACGATGCTACTTTATCTCGTTCTATCAGACTCTCAACTACTGCGCCCGTTCGCATTCCCTGGGTCTTGTTAATAGGCAGGCGATACAACAGCCCTTGATCTATCGTCCGGGTACCTCACCTATAGCCAGGATAATTAGGACGTTCGAGGGGCTGACTATAGGCACCTCATGCCAATAAGTTCTCTCTTTATTATGTTCGTCGCATATAATAAAACTGTCAGGGAATGCAAATAAGACTGACGGTCGGACTCTTTTCTTTGCAACACGTGCTTTCTGCCCTGCCTCCGAAATTCTCTCTAGTTCCAGGCTTCAGGTTGAATAGTCCTGAAGTGTTTGTCACCTTATTAGGTTACCGCATGTTATCAACTGGTGAAGCACATAATCGCAAAACAATGCCGTTTAAACCCCATGAGGTAAGATAACCCTAACCCCAGATAACCCAGAAGATAACCCCCATTCGAGATAACCCTCATGATCCTGCAATCACGTGCTAAGATTGCTTCCTGCCTGTAGAGATAACCCACCTTTAGTGGTTGCACCAAGATAACCCTGGTCTCCAGATAACCCTAACAGATAACCCAAAGATAACCCCAGATAACCCTCATTAACACAGATAACCCATAACAGATAACCCGTGGCGGAAGATAGATAACCCCTTGCAGATAACCCGAAAGTATCAGTGACACATTAGTCATACCCAGATAACCCCCTTGCCGTCCACCATACAGCAGATAACCCCCTATCCACAGGACTATTCATGCAGCCGAAATGACATAAAGATAACCCGCTAGCTTCGCACACAGATAACCCCCAAAGATAACCCCGTTCCTCACCTCGCCGCGTTCCACCTTATCCGCGTTCCGCACCGCGTTCCTTACCTCCGCGTTCCTCCATGATGATTCAGATAACCCCAGATAACCCCCAGTAGATAACCCGCAGATAACCCGCGCTGGCGTCAACCATGCTTTATTGCCGCCCTTCCCGCGTTCCTATTAAAACTATTTTTGCGTGTGCGGCTGATACCGCGTTCCGAATCGGACACTGGGAAGTCTTCTGACCGCGTTCCTGAGTGGATAACGGCCCGCGTTCCCTGGGCTCGAAAGTCCCGCGTTCCGGCGCTCCGCGTTCCACGCCCCGCGTTCCCGCGTTCCTCCCGCGTTCCCCCGCGTTCCCGCGTTCCCCATCTGCCGCGTTCCCGTCACGGGAAGGGAGTGCGCTTCCGCGTAAGCCGCGTTCCCTACGTTAATTATCGTCAGCTATTCGTTAGTAAAATGGGCAACATCTACCTTCCGGTCCGCGTTCCGTTCCATCCGCAATTTCGCGCGATAGCTTAGGCAATCCGGTATCCGCGTTCCCCCGCGTTCCGCGTTCCGCGTTCCTCGTCAAACAAACTGACGTCCGTCCTAGATGGTCAATCTGGCATGCATGAAGTCAGTTAACGAACTCAGAGCTGTTCCGTCAGTGGCGACCCCTCCAGCCAACGCTAGCCTAATGGTTAACTTCCGCTTATGGCTACAGGTGGTCGCAGATAATGTCAATAGACACCTCCGCGAACAAATAGCGGTCCTGCTCAACGTACGGGAACTGATTGTCAATCTCAGTCTCTGGACCTGGGAATGCGCAACTTTACCTGGGCTAGCCATGTTACCTCCCGGAGATTCAACGCCCGGTTGTTCGCTGCTAAGCCGCTGCTAACAGTTGAAATATTATTAATTCTACTCTATTCGCTGCTAAACGCTGCGCTGCTAATACTCGCCGCTGCTAACATTCATTATCGATACGTGGCCGTCAGATCTGATTTAAGATCAACGCTGCTAATGCTAATCATGACTAGTCATTCATCGAAAACTCGTGTCGTTACTAGTCATCCATCGCTGCTAAGAAATCCCCACCACTCGCTGCTAACGCTGCCGCTGCTAACTGCTCGCTGCTAAAGTCATGGTTACTAACCCTGTAGTATTAACGCTGCTAATGCTCCACGCTGCTAAACCCTGTAATGGTAACCCTGTCTAGTCATGCACCGCTGCTAATAACCCTGTACCCTGTAAATCCTAACCCTCGCTGCTAAACGCTGCTAAACCCACTAGTCCGCTGCTAATGGATAGTCAATTAACCCTGTCCCTGTACCCTGTCGCTGCTACGCTGCTAACGCTGCTAATAATTATTTAACCCTGTTTGAGTGTAACCCGCTGCTAAGACCGCTGCTAACTGCGCCGCTGCTAATAAGTCACGCTGCTAAGTTGCATGGTAATGCATTTGAGTGGACGGTTCAGCGGTATTAGTGATTGAGTGGAGTGGATAGTCTTGAGTGGATTATTAGTGTTGCATGGTATAACCCTGTATTTAACCCTGTCCTGTGCATGGTAACCTAACCTAACCCTGTAAAGGGCATGTTGAGTGGATAACCCTGTGTTGAGTGGATTAGTTTGAGTGGAGAGTATGGTATGGTAAATGCTAACCCTGTTTTGAGTGGTTGAGTGGATAAGGTTGCTGGATATGCATGTAACCCTGTGGAGTAACCCTGTTAACCCTGTGAGTGGACATGGTTTTGAGTGGAGGTAACATTTGTGCGCAAGGGTGTATTAGTGCGTATTGTATGCATGGTATCCCGAGCCCCTGTTTGAGTGGATTGTTGAGTGGATAAGTGGCCTGCATGGTATGTGTATGGGCGGCTAAGGTATTAGTGGATCAGGCTAAAAACTTGATGTCTTTTAGTAACAGCGCTTGCATTGCATGGTATCTATAAGAAGTACTGCGCCTATGCATGGTACCCTATCTATTAGTGCATGGTAGTGTTAGCATGCGTGCATGGTAAGGGCAAAGGCAGGCAAAGGTTTCCAAACTTTCACGACTATGTGTAGCCATAGGGCGGCAAAGGTGCAGGCAAAGGTCAAAGGGCAAAGGTGGTCAAATGGCGGAACATCAAAACATATGGCAAAGGTGGTCCGGACTGCGCGGCAAAGGTGATCTTAGGCAAAGGTAGATTGAGCTGGACGTCTCGAACGGCAAAGGTAAGGTGGTGAAAGAGGGGCAAAGGTTGTCCCCTCCGGCAAAGGGGCAAAGGTCCGCCCTCGTTAGGCAAAGGTGGCAAAGGTGGCAAAGGTAGTGGGTTGGTCAACACCCCTGACATCCACGTACTCTGGCAAAGGTCGTGGGCGATTTCCCGATCGTGCACTCATTTTCCGGCAAAGGTGTGGCAAAGGTAATATGATAGGCAAAGGCAAAGGTGGCAAAGGTATGGCAAAGGTCTACGACCGTCAACAGCTTCTGGCAGGGATGGAGCTGGCACATTAGATGGCTTAGCTGGGCTTATCAGTTGGCAAAGGTCCTTGCTATTTACGTTCACTGGGCAAAGGTAGAGCCCAGTGCCTGGCAAAGGTAAGAATGTGATAAATCATACTCATCTGGTAGCGAATATGTTGTAATAACTGAAACGGATGCTGTCTCTAGTTATAGGTGAATACAAGGACGGGTAGAAAAGATCACTATGTCTCTAGACTCTGTCTCTAGATTCAGCGCTTCGCTCATGTCTCTAGTCGGTTAGCAGGTGTTGTCTCTAGCGCAATTGTCTCTAGACTCCCGTGACTCGCGGCCGCGCACATGTCTCTAGCGTGTTGTCTCTAGAAGGTGAAGTACAATGTCTCTAGTCTGAATACAGCGTCATGTCTCTAGGATGTACGGTTTACGAAACGTAGTGCAGGTGCTCTTTACACACGCGTACATGCCTTCGTTCGTTGTCTCTAGAACATAACACAGAAGTCAGATGTGTCTCACAGAAGTCTCTTTGTCTACAGAAGTCTACAGAAGTCAAGTCAGAAGTCAACAGAAGTCTTTGTCTCTAACAGAAGTCGAACACTTGTCTACAGAAGTCAGTAGCCTGTCACAGAAGTCTGTCTCTAGAAGCGTGGGGGAACGGGATTTAACAGAAGTCCGCCTGTCTCTAGCACAGAAGTCAGATATTACAGAAGTACAGAAGTCCTCACAGAAGTCGTTCAGCAATACACCGTATAGAGGACAGAAGTCCGGTACAGAAGTCCATTTTGGCAAGCTACAGAAGTCAGGTGCCCTACAGAAGTCAGAAGTCAACGGGTTGCGCTATTAACTATAAAATACAGAAGTCCAGTCTTCATGCTTGCGAAACAGAAGTCGGTGATACAGAAGTCTTAGCCGCCAGGCACAGAAGTCGACAGAAGTCAGACTACATCGAACAGAAGTCGTCAGAAGTCTCATCCGAGGTTGAGAGCTGCGGGTGGTTTCACATTGCGTGGAGTATAATACAGAAGTCGAAGCGTCATCGTCAATATGTAAAATACGACGCGTACTAAGATAAGGTTCCGACACGGACGGGTAACGTGCGGGATGACTAACTATGGTTCCGTTAGCTTCCATTCGCACGGCGGAAGAATAGCCTGTTATATCTGATCTTGCAACCAATATTGTGTCCGTGGGCAGGGAACGAAAGAGCCGGTAGCCGTGGTCATCTTGCGGGATGCTCTTTAGCATCTTTTTACTTTACTATTTCTCTCGACGACCTCTCATGGTCCAACACGCAGCCACAACGATAAACCGGTAGTGCACGTTTATGTCAGCTTCTTCCCATTTCCCGGTCCAAAGCGTCTACCTGTGCTTCTTTGTAGCCTGGTCCGGATATCGTGTAGAATCAAGCCAGTTCTACAAGAGTGGGAGTGGGCCGCCGCAGCAGACATACTTTCCACTACTTCCCAGGGAACGTCGTCCTCTCTCCCTCCCCACGTCATTTCTCCCATTCGGTTAGGCCTAACCATCGGAGTACTTGTATTTGGACGATAGCAGAACTACATCTTTGCTGGCTCACAGCGTTAAGACCAAATTCAGGCCAGTCCTTCAAGGTTCAACCTATGACAAGGTGCTCAGTTATGATGCGGGTTAATACGGTCCGAAAATACGCATTCCCCTCATCATCTTTACGGAAACGGGCTAGTGTCCGTGTATGAGTATGGGTCTCGGTTCCTTTTAGCCCTTCGCTACGCGCAGTAGTTTGTGGGAATGGGAGAGAATGTACGCTTG'
    k = 9
    L = 505
    t = 16

    patterns = find_patterns_forming_clumps(genome, k, L, t)
    print(*patterns)


if __name__ == '__main__':
    main()
