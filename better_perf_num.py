import sys
from tqdm import tqdm
import time

USAGE = "python perf_num.py <perf_num amount>"

def args_check(args):
    if len(args) != 2:
        print(f"Usage: {USAGE}")
        exit(1)
    try:
        int(args[1])
    except:
        print(f"Usage: {USAGE}")
        exit(1)
    if int(args[1]) <= 0:
        print("amount must be greater than 0")
        exit(1)

def is_prime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main(args):
    args_check(args)
    doubs = [1, 2]
    perf_nums = []
    num_perfs = int(args[1])
    for _ in tqdm(range(num_perfs), desc="Computing numbers"):
        while True:
            pot_num = sum(doubs)
            if is_prime(pot_num):
                perf_nums.append(pot_num * doubs[-1])
                doubs.append(doubs[-1] * 2)
                break
            else:
                doubs.append(doubs[-1] * 2)
        time.sleep(.01)
    for num in perf_nums:
        print(f"Perfect number found: {num}")


if __name__ == "__main__":
    main(sys.argv)