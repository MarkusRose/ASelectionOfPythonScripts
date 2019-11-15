# -*- coding: utf-8 -*-
"""
Created on Sat May 25 20:59:28 2019

@author: Markus
"""

import numpy as np
import random
import string

charset = string.ascii_letters+string.digits#+string.punctuation
charset += "!@#$%?&*()^."

print()
print("".join(np.random.choice(list(charset),size=10)))
