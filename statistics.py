import os
import re

score = ['map', 'hits']
number = ['10', '50', '100']

data_list = ['Training', 'Validation']

pattern = re.compile(r'(?<=accuracy: )\d+\.?\d*')

def cal_best_scores(path):
    best_scores = {}
    for a in score:
        for b in number:
            key = '{}@{}'.format(a, b)
            best_scores[key] = 0
            with open(path) as f:
                for line in f.readlines():
                    if key + ' ' in line:
                        value = eval(line.strip().split()[1])
                        if value > best_scores[key]:
                            best_scores[key] = value
    
    for c in data_list:
        key = c
        best_scores[key] = 0
        with open(path) as f:
            for line in f.readlines():
                if key in line:
                    value = pattern.findall(line)[0]
                    value = eval(value)
                    if value > best_scores[key]:
                        best_scores[key] = value
            
        
    return best_scores


files = os.listdir('log')
for file_name in files:
    print(file_name)
    best_scores = cal_best_scores('log/' + file_name)
    for key in best_scores:
        print("{}: {}".format(key, best_scores[key]))
    print('')