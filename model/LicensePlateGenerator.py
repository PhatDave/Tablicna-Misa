import os
import requests as re
import random
from bs4 import BeautifulSoup as bs
from tqdm import tqdm


class Plate:
    def __init__(self, region="", digString="", finLetters=""):
        self.region = region
        self.digString = digString
        self.finLetters = finLetters

    def __str__(self):
        return f'{self.region}  {self.digString}-{self.finLetters}'


def Pad(i, n):
    i = str(i)
    return '0' * (n - len(i)) + i


def PadInt(string, length):
    string = str(string)
    while len(string) < length:
        string += '0'
    return string


regions = [
    'BJ',
    'BM',
    'ČK',
    'DA',
    'DE',
    'DJ',
    'DU',
    'GS',
    'IM',
    'KA',
    'KC',
    'KR',
    'KT',
    'KŽ',
    'MA',
    'NA',
    'NG',
    'OG',
    'OS',
    'PS',
    'PU',
    'PŽ',
    'RI',
    'SB',
    'ŠI',
    'SK',
    'SL',
    'ST',
    'VK',
    'VT',
    'VU',
    'VŽ',
    'ZD',
    'ZG',
    'ŽU',
]
regionStart = 22951
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = [i for i in range(10)]
repeats = 12

print(regions, letters, digits)

plates = []
for i in regions:
    for j in range(repeats):
        newPlate = Plate(i)

        digString = ""
        for k in range(random.randint(3, 4)):
            digString += str(random.choice(digits))
        newPlate.digString = digString

        letterString = ""
        for k in range(2):
            letterString += random.choice(letters)
        newPlate.finLetters = letterString

        plates.append(newPlate)
# print(newPlate)
print(len(plates))

for slot in range(2):
    for i in letters:
        for j in range(repeats):
            newPlate = Plate(random.choice(regions))

            digString = ""
            for k in range(random.randint(3, 4)):
                digString += str(random.choice(digits))
            newPlate.digString = digString

            letterString = ""
            if slot == 0:
                letterString += i
                letterString += random.choice(letters)
            else:
                letterString += random.choice(letters)
                letterString += i
            newPlate.finLetters = letterString

            plates.append(newPlate)
    # print(newPlate)
print(len(plates))

for slot in range(4):
    for i in digits:
        for j in range(repeats):
            newPlate = Plate(random.choice(regions))

            digString = ""
            for k in range(random.randint(3, 4)):
                if k == slot:
                    digString += str(i)
                    continue
                digString += str(random.choice(digits))
            newPlate.digString = digString

            letterString = ""
            for k in range(2):
                letterString += random.choice(letters)
            newPlate.finLetters = letterString

            plates.append(newPlate)
    # print(newPlate)
print(len(plates))

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

pbar = tqdm(enumerate(plates), total=len(plates))
for i, plate in pbar:
    data = {
        'ctype' : '1',
        'fon'   : '2',
        'posted': '1',
        'Submit': '',
        'region': str(regionStart + regions.index(plate.region)),
        'digit' : plate.digString,
        'b1'    : plate.finLetters[0],
        'b2'    : plate.finLetters[1],
    }
    pbar.desc = str(plate)
    pbar.refresh()
    reply = re.post(r'http://platesmania.com/hr/informer', headers=header, data=data)
    soup = bs(reply.content, 'html.parser')
    link = soup.find('img', {'class': 'img-responsive vcenter'})['src']

    result = re.get(link, headers=header)
    with open(f'output\\{str(plate)}.png', 'wb') as f:
        f.write(result.content)
    # with open('output.txt', 'a') as f:
    # 	f.write(link + '\n')