import math
import random ,time
import pywasm

# t = int(time.time())
# t1 = int(t / 2)
# t2 = int(t / 2 - math.floor(random.random() * 50 + 1))
wasm = pywasm.load("beacdee13d73ac0e.wasm")
# sign = wasm.exec("encode", [t1, t2])
# m = f"{sign}|{t1}|{t2}"