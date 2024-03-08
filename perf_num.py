import sys
from tqdm import tqdm

USAGE = "python perf_num.py <max_num>"

def args_check(args):
    if len(args) != 2:
        print(f"Usage: {USAGE}")
        exit(1)
    try:
        int(args[1])
    except:
        print(f"Usage: {USAGE}")
        exit(1)

def perf_num(num: int) -> bool:
    divs = []
    for i in range(1, num):
        if num % i == 0:
            divs.append(i)
    return (sum(divs) == num)

def main(args):
    args_check(args)
    perf_nums = []
    max = int(args[1])
    for num in tqdm(range(1, max+1), desc="Checking numbers"):
        if perf_num(num):
            perf_nums.append(num)
    for num in perf_nums:
        print(f"Perfect number found: {num}")

if __name__ == "__main__":
    main(sys.argv)