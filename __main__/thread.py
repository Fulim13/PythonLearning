import multiprocessing


def task(n):
    print(f"Processing {n}")
    return n * n


if __name__ == "__main__":
    with multiprocessing.Pool() as pool:
        tasks = range(5)
        results = pool.map(task, tasks)
    print(results)
