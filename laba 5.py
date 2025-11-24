import math
import random
import datetime
import os
import sys
import json
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. math
try:
    num = 16
    print(f"Квадратний корінь з {num}: {math.sqrt(num)}")
except Exception as e:
    print("Помилка у math:", e)

# 2. random
try:
    print("Випадкове число від 1 до 10:", random.randint(1, 10))
except Exception as e:
    print("Помилка у random:", e)

# 3. datetime
try:
    now = datetime.datetime.now()
    print("Поточна дата і час:", now.strftime("%Y-%m-%d %H:%M:%S"))
except Exception as e:
    print("Помилка у datetime:", e)

# 4. requests
try:
    response = requests.get("https://api.github.com")
    print("Статус код запиту:", response.status_code)
except Exception as e:
    print("Помилка у requests:", e)

# 5. numpy
try:
    arr = np.array([1, 2, 3, 4, 5])
    print("Середнє значення:", np.mean(arr))
except Exception as e:
    print("Помилка у numpy:", e)