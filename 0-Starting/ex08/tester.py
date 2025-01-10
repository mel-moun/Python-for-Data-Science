from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

# Test ft_tqdm
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

# Test tqdm
for elem in tqdm(range(333)):
    sleep(0.005)
print()
