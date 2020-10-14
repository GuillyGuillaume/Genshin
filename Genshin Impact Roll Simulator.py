import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#
fiveS = ["Keqing", "Mona", "Qiqi", "Diluc", "Jean"]
fiveSR = ["Venti"]
fourS = ["Sucrose", "Chongyun", "Noelle", "Bennett", 
         "Ningguang", "Xingqiu", "Beidou", "Razor",
         "Rust", "Sacrificial Bow", "The Stringless", 
         "Favonius Warbow", "Eye of Perception", 
         "Sacrificial Fragments", "The Widsith",
         "Favonius Codex", "Favonius Lance", 
         "Dragon's Bane", "Rainslasher", "Sacrificial Greatsword",
         "The Bell", "Favonius Greatsword", "Lion's Roar", 
         "Sacrificial Sword", "The Flute", "Favonius Sword"]
fourSR = ["Fischl", "Xiangling", "Barbara"]
#
fiveR = np.zeros(90)
fourR = np.zeros(10)
for i in range(0,90):
    fiveR[i] = 0.6 + (i * 1/88)
for i in range(0,10):
    fourR[i] = (5.1 + (i * 7.9/8))
fiveR[-1] = 111
fourR[-1] = 111
#
#
def roll(nroll):
    pity5 = 0
    pity4 = 0
    fiveC = 0
    fourC = 0
    for i in range(0,nroll):
        rng = np.random.randint(100) + np.random.rand()
        if (rng <= fiveR[pity5]):
            pull = name(5)
            print('\x1b[0;30;43m' + pull + '\x1b[0m')
            plt.imshow(mpimg.imread(str(pull + '.png')))
            pity5 = 0
            fiveC += 1
        elif (rng <= fourR[pity4]):
            print('\x1b[0;30;45m' + name(4) + '\x1b[0m')
            pity5 += 1
            pity4 = 0
            fourC += 1
        else:
            #print("*")
            pity5 += 1
            pity4 += 1
    print("//")
    print("you got " + str(fiveC) + " five stars and " + str(fourC) + " four stars.")
    print("You spent " + str(nroll * 160) + " Prismogems.")
def name(star):
    if (star == 5):
        if (np.random.randint(2) == 0):
            return(fiveSR[np.random.randint(len(fiveSR))])
        else:
            return(fiveS[np.random.randint(len(fiveS))])
    if (star == 4):
        if (np.random.randint(2) == 0):
            return(fourSR[np.random.randint(len(fourSR))])
        else:
            return(fourS[np.random.randint(len(fourS))])