import threading



# Доб строки в файл
# with open('out.txt', 'w') as f:
#     for _ in range(10):
#         f.write('test\n')


# with open('out.txt', 'a') as f:
#     for _ in range(5):
#         f.write('apple\n')

def write_to_file(path: str, ix: int) -> None:
    for _ in range(5):
        with open(path, 'a') as f:
            f.write(f'{ix} apple\n')


jobs = [threading.Thread(target=write_to_file, args=('outs.txt', ix)) for ix in range(5)] 

for job in jobs:
    job.start()

for job in jobs:
    job.join()