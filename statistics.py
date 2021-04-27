import os
import re
import matplotlib.pyplot as plt
import matplotlib

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


# files = os.listdir('log')
# for file_name in files:
#     print(file_name)
#     best_scores = cal_best_scores('log/' + file_name)
#     for key in best_scores:
#         print("{}: {}".format(key, best_scores[key]))
#     print('')



num_list = []  # 4*3
standard = 'hits'

files = sorted(os.listdir('log/test'))
for file_name in files:
    print(file_name)
    best_scores = cal_best_scores('log/test/' + file_name)
    num_list.append([])
    for key in best_scores:
        if standard in key:
            num_list[-1].append(best_scores[key])
            # print("{}: {}".format(key, best_scores[key]))
    # print('')

label_list = [standard + '@10', standard + '@50', standard + '@100']    # 横坐标刻度显示值
x = range(len(num_list[0]))

colors = ['blue', 'green', 'orange', 'red', 'yellow', 'pink']

for i, item in enumerate(num_list):
    plt.bar(x=[j + 0.1*i for j in x], height=item, width=0.08, alpha=1, color=colors[i], label=files[i])
    # plt.bar(x=[i + 0.4 for i in x], height=item, width=0.4, color='green', label="GRU")

plt.ylim(0, 0.6)
plt.ylabel("hits")

plt.xticks([index + 0.3 for index in x], label_list)
plt.title("Twitter")
plt.legend(loc=2)
plt.show()