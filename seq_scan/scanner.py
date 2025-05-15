def pam_match(seq, pam_pattern):
    """Return True if seq matches PAM pattern with N wildcard support."""
    if len(seq) != len(pam_pattern):
        return False
    for s_char, p_char in zip(seq.upper(), pam_pattern.upper()):
        if p_char == 'N':
            continue
        if s_char != p_char:
            return False
    return True

def find_targets(sequence, pam_pattern, target_len):
    """Find all CRISPR target sites in sequence matching PAM on both strands."""
    sequence = sequence.upper()
    rev_comp_seq = reverse_complement(sequence)
    targets = []

    seq_len = len(sequence)
    pam_len = len(pam_pattern)

    # Scan plus strand
    for i in range(seq_len - pam_len - target_len + 1):
        pam_seq = sequence[i + target_len:i + target_len + pam_len]
        if pam_match(pam_seq, pam_pattern):
            target_seq = sequence[i:i + target_len]
            targets.append({
                'strand': '+',
                'target_seq': target_seq,
                'pam_seq': pam_seq,
                'target_start': i,
                'target_end': i + target_len,
                'pam_start': i + target_len,
                'pam_end': i + target_len + pam_len
            })

    # Scan minus strand
    for i in range(seq_len - pam_len - target_len + 1):
        # PAM on minus strand: check rev comp
        pam_seq = rev_comp_seq[i:i + pam_len]
        if pam_match(pam_seq, pam_pattern):
            # Target on minus strand is after PAM on reverse complement, map indices back to original
            target_start = seq_len - (i + pam_len + target_len)
            target_end = seq_len - (i + pam_len)
            pam_start = seq_len - (i + pam_len)
            pam_end = seq_len - i

            target_seq = sequence[target_start:target_end]
            targets.append({
                'strand': '-',
                'target_seq': target_seq,
                'pam_seq': sequence[pam_start:pam_end],
                'target_start': target_start,
                'target_end': target_end,
                'pam_start': pam_start,
                'pam_end': pam_end
            })

    return targets

def reverse_complement(seq):
    complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C', 'N':'N'}
    return ''.join(complement.get(base, 'N') for base in reversed(seq.upper()))
