# Копируем из папки и подпапок START_DIRECTORY все mp3 и wav файлы, в имени которых есть телефоны,
# указанные в XLSX_PHONE_LIST

import os
import shutil
from datetime import datetime
#import openpyxl
import hashlib
START_DIRECTORY = '/media/da3/audio/'
XLSX_PHONE_LIST = '/home/da3/Downloads/прислать_записи.xlsx'

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

walking = list(os.walk(START_DIRECTORY))

#numbers = tuple()
numbers = (79637346407,)
#wb = openpyxl.load_workbook(filename=XLSX_PHONE_LIST)
#ws = wb[wb.sheetnames[0]]
#for i, row in enumerate(ws.values):
#    if i:
#        numbers += (int(row[0]),)

wav_files = []
wav_files_md5 = {}
wav_doubles = {}
wav_list = open(datetime.now().strftime('%Y-%m-%d') + 'mp3wav_list.csv', 'wt')
for root, dirs, files in walking:
    wav_files += [[root, name] for name in files if name.endswith('.mp3') or name.endswith('.wav')]

writed =tuple()

for wav_file in wav_files:
    for number in numbers:
        if str(wav_file[1]).find(str(number)[1:]) > -1 and wav_file[1] not in writed:
              shutil.copy(os.path.join(wav_file[0], wav_file[1]),'/home/da3/-/')



