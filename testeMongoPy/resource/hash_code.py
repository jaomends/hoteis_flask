import math

# Funções auxiliares
def rotr(x, n):
    return (x >> n) | (x << (32 - n))

def ch(x, y, z):
    return (x & y) ^ (~x & z)

def maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

def sigma0(x):
    return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)

def sigma1(x):
    return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)

def gamma0(x):
    return rotr(x, 7) ^ rotr(x, 18) ^ (x >> 3)

def gamma1(x):
    return rotr(x, 17) ^ rotr(x, 19) ^ (x >> 10)

# Constantes do SHA-256
k = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
    0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
    0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
    0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f,
    0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]


# Função principal para calcular o hash SHA-256
def sha256(mensagem):
    # Inicialização dos valores iniciais do hash
    h = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
    ]

    # Preparação da mensagem
    mensagem = bytearray(mensagem)
    mensagem.append(0x80)  # Adicionar bit '1' ao final da mensagem

    # Adicionar bits de padding até o tamanho adequado
    while len(mensagem) % 64 != 56:
        mensagem.append(0x00)

    # Adicionar tamanho original da mensagem (em bits)
    tamanho = len(mensagem) * 8
    tamanho_bytes = tamanho.to_bytes(8, 'big')
    mensagem.extend(tamanho_bytes)

    # Processamento em blocos de 512 bits
    for i in range(0, len(mensagem), 64):
        bloco = mensagem[i:i+64]

        # Preparar as palavras de mensagem
        w = [0] * 64
        for j in range(16):
            w[j] = int.from_bytes(bloco[j*4:(j+1)*4], 'big')

        # Expansão das palavras de mensagem
        for j in range(16, 64):
            s0 = gamma0(w[j-15])
            s1 = gamma1(w[j-2])
            w[j] = (w[j-16] + s0 + w[j-7] + s1) & 0xffffffff

        # Inicialização das variáveis de trabalho
        a, b, c, d, e, f, g, h = h

        # Loop principal do algoritmo SHA-256
        for j in range(64):
            s0 = sigma0(a)
            s1 = sigma1(e)
            ch_temp = ch(e, f, g)
            temp1 = (h + s1 + ch_temp + k[j] + w[j]) & 0xffffffff
            temp2 = (s0 + maj(a, b, c)) & 0xffffffff

            h = g
            g = f
            f = e
            e = (d + temp1) & 0xffffffff
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xffffffff

        # Atualização dos valores finais do hash
        h = [
            h[0] == (h[0] + a) & 0xffffffff,
            (h[1] + b) & 0xffffffff,
            (h[2] + c) & 0xffffffff,
            (h[3] + d) & 0xffffffff,
            (h[4] + e) & 0xffffffff,
            (h[5] + f) & 0xffffffff,
            (h[6] + g) & 0xffffffff,
            (h[7] + h) & 0xffffffff
        ]

    # Conversão dos valores finais do hash para hexadecimal
    hash_sha256 = ''.join(format(x, '08x') for x in h)
    return hash_sha256

# Exemplo de uso
mensagem = "Exemplo de mensagem"
hash_sha256 = sha256(mensagem.encode('utf-8'))
print("Hash SHA-256 da mensagem:", hash_sha256)
