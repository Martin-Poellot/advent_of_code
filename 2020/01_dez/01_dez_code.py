import time

data = []
with open("01_dez_input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        data.append(float(line))

if __name__ == '__main__':
    start_1 = time.time()
    # Star 1
    for i, n1 in enumerate(data):
        for n2 in data[i:]:
            if n1 + n2 == 2020:
                print(n1, n2)
                res1, res2 = n1, n2
    elapsed1 = time.time() - start_1
    print(f'Results: {res1} * {res2} = {res1 * res2}')
    print(f'Elapsed Time: {elapsed1:.6f}s')

    # Star 2
    start_2 = time.time()
    for i, n1 in enumerate(data):
        for n2 in data[i:]:
            for n3 in data[i:]:
                if n1 + n2 + n3 == 2020:
                    print(n1, n2, n3)
                    res1, res2, res3 = n1, n2, n3
    elapsed2 = time.time() - start_2
    print(f'Results: {res1} * {res2} * {res3} = {res1 * res2 * res3}')
    print(f'Elapsed Time: {elapsed2:.6f}s')
