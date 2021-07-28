from func_fatorial import fatorial

def numero_binomial(n, k):
    fat_k_vezes_n = fatorial(k) * fatorial(n)
    binominal = fatorial(k) // fat_k_vezes_n
    return binominal