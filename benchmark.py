import time
import csv
from ipfeddh import IPFEDDH



## Tests 
def simulate_increasing_bits():
    results = []
    stages = [512, 1024, 2048]
    l = 100
    for bits in stages:
        G = IPFEDDH(bits)

        x = G.random_vector(l, G.p)
        y = G.random_vector(l, G.p)

        start_time = time.time()
        mpk, msk = G.setup(l)
        setup_time = time.time() - start_time

        start_time = time.time()
        ct = G.encrypt(mpk, x, l)
        encrypt_time = time.time() - start_time

        start_time = time.time()
        sk = G.keyder(msk, y, l)
        keyder_time = time.time() - start_time

        start_time = time.time()
        v = G.decrypt(mpk, ct, sk, y, l)
        decrypt_time = time.time() - start_time

        setup_time *= 1_000_000_000
        keyder_time *= 1_000_000_000
        encrypt_time *= 1_000_000_000
        decrypt_time *= 1_000_000_000
        total_time = setup_time + keyder_time + encrypt_time + decrypt_time

        print("bits: ", bits)

        results.append([bits, l, setup_time, encrypt_time, keyder_time, decrypt_time, total_time])

    with open('data/ipfe-ddh_timings_increasing_bits.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['bits', 'l', 'time setup', 'time encrypt', 'time keyder', 'time decrypt', 'time total'])
        csvwriter.writerows(results)


def simulate_increasing_length():
    results = []
    bits = 512
    length = [100, 1000, 10000]
    G = IPFEDDH(bits)
    
    for l in length:
        x = G.random_vector(l, G.p)
        y = G.random_vector(l, G.p)
        
        start_time = time.time()
        mpk, msk = G.setup(l)
        setup_time = time.time() - start_time

        start_time = time.time()
        ct = G.encrypt(mpk, x, l)
        encrypt_time = time.time() - start_time

        start_time = time.time()
        sk = G.keyder(msk, y, l)
        keyder_time = time.time() - start_time

        start_time = time.time()
        v = G.decrypt(mpk, ct, sk, y, l)
        decrypt_time = time.time() - start_time

        setup_time *= 1_000_000_000
        keyder_time *= 1_000_000_000
        encrypt_time *= 1_000_000_000
        decrypt_time *= 1_000_000_000
        total_time = setup_time + keyder_time + encrypt_time + decrypt_time

        print("bits: ", bits)

        results.append([bits, l, setup_time, encrypt_time, keyder_time, decrypt_time, total_time])

    with open('data/ipfe-ddh_timings_increasing_length.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['bits', 'l', 'time setup', 'time encrypt', 'time keyder', 'time decrypt', 'time total'])
        csvwriter.writerows(results)


simulate_increasing_bits()
simulate_increasing_length()