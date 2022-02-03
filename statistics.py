import os
import re
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from collections import defaultdict

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
                    if 'Epoch' in line:
                        num = line.strip().split()[2]
                    if key + ' ' in line:
                        value = eval(line.strip().split()[1])
                        if value > best_scores[key]:
                            best_scores[key] = value
                            best_scores[key + '@num'] = num

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


def draw(standard, path, dataset):
    num_list = []  # 4*3

    files = sorted(os.listdir(path))
    for file_name in files:
        print(file_name)
        best_scores = cal_best_scores(path + '/' + file_name)
        num_list.append([])
        for key in best_scores:
            if standard in key and 'num' not in key:
                num_list[-1].append(best_scores[key])
                print(key + ':', best_scores[key + '@num'])
                # print("{}: {}".format(key, best_scores[key]))
        # print('')

    label_list = [standard + '@10', standard + '@50', standard + '@100']  # 横坐标刻度显示值
    x = range(len(num_list[0]))

    colors = ['blue', 'green', 'orange', 'red', 'yellow', 'pink', 'purple']

    for i, item in enumerate(num_list):
        plt.bar(x=[j + 0.1 * i for j in x], height=item, width=0.08, alpha=1, color=colors[i], label=files[i])
        # plt.bar(x=[i + 0.4 for i in x], height=item, width=0.4, color='green', label="GRU")

    plt.yticks(np.arange(0, 0.6, 0.05))
    plt.ylabel(standard)

    plt.xticks([index + 0.3 for index in x], label_list)
    plt.title(dataset)
    plt.legend(loc=2)
    plt.grid(axis='y')
    plt.show()


def draw_hit_map(path, dataset):
    draw('hits', path, dataset)
    draw('map', path, dataset)


def draw_baseline(path):
    datasets = ['Twitter', 'Douban', 'MemeTracker']
    label_hits = ['Hits@10', 'Hits@50', 'Hits@100']
    label_map = ['MAP@10', 'MAP@50', 'MAP@100']
    models = []

    hits_data = {}
    map_data = {}

    # Twitter@DeepDiffuse
    f = open(path)
    for k, line in enumerate(f.readlines()):
        model, standard, res = line.strip().split('\t')
        if model not in models:
            models.append(model)
        res = eval(res)
        print(res)
        if standard == 'Hits':
            for i, item_list in enumerate(res):
                hits_data[datasets[i] + '@' + model] = item_list
        else:
            for i, item_list in enumerate(res):
                map_data[datasets[i] + '@' + model] = item_list
    print(hits_data)
    print(map_data)

    x = range(3)
    colors = ['blue', 'green', 'red', 'orange', 'pink', 'purple', 'yellow', 'grey', 'black']

    for dataset in datasets:
        count = 0
        for i, model in enumerate(models):  # dataset@model
            if dataset + '@' + model not in hits_data:
                continue

            if dataset == 'MemeTracker':
                plt.bar(x=[j + 0.20 * count for j in x],
                        height=hits_data[dataset + '@' + model],
                        width=0.16, alpha=1,
                        color=colors[i],
                        label=models[i])
            else:
                plt.bar(x=[j + 0.13 * count for j in x],
                        height=hits_data[dataset + '@' + model],
                        width=0.11, alpha=1,
                        color=colors[i],
                        label=models[i])
            count += 1

        if dataset == 'Twitter' or dataset == 'MemeTracker':
            ran = np.arange(0, 0.65, 0.05)
        else:
            ran = np.arange(0, 0.45, 0.05)
        plt.yticks(ran)
        plt.ylabel('Hits')

        if dataset == 'MemeTracker':
            plt.xticks([index + 0.3 for index in x], label_hits)
        else:
            plt.xticks([index + 0.325 for index in x], label_hits)
        plt.title(dataset)
        plt.legend(loc=2)
        plt.grid(axis='y')
        plt.savefig(dataset + '_Hits.jpg')
        plt.show()

    for dataset in datasets:
        count = 0
        for i, model in enumerate(models):  # dataset@model
            if dataset + '@' + model not in map_data:
                continue

            if dataset == 'MemeTracker':
                plt.bar(x=[j + 0.20 * count for j in x],
                        height=map_data[dataset + '@' + model],
                        width=0.16, alpha=1,
                        color=colors[i],
                        label=models[i])
            else:
                plt.bar(x=[j + 0.13 * count for j in x],
                        height=map_data[dataset + '@' + model],
                        width=0.11, alpha=1,
                        color=colors[i],
                        label=models[i])
            count += 1

        if dataset == 'Twitter':
            ran = np.arange(0, 0.22, 0.02)
        elif dataset == 'MemeTracker':
            ran = np.arange(0, 0.20, 0.02)
        else:
            ran = np.arange(0, 0.11, 0.01)

        plt.yticks(ran)
        plt.ylabel('MAP')

        if dataset == 'MemeTracker':
            plt.xticks([index + 0.3 for index in x], label_map)
        else:
            plt.xticks([index + 0.325 for index in x], label_map)
        plt.title(dataset)
        # plt.legend(loc=2)
        plt.grid(axis='y')
        plt.savefig(dataset + '_MAP.jpg')
        plt.show()


def write_res(standard):

    datasets = ['twitter', 'douban', 'memetracker']
    files = ['_emb_0_attn_0', '_emb_0_attn_1', '_emb_0_attn_2', '_emb_1_attn_0', '_emb_1_attn_1', '_emb_1_attn_2']
    models = ['GRU', 'GRU-A1', 'GRU-A2', 'GRU-E', 'GRU-EA1', 'GRU-EA2']

    f = open('res/result.txt', 'a+')

    for i, file_name in enumerate(files):
        num_list = []  # 4*3
        for dataset in datasets:
            if file_name.startswith('_emb_1') and dataset == 'memetracker':
                continue
            best_scores = cal_best_scores('log2/' + dataset + '/' + dataset + file_name + '.log')
            num_list.append([])
            for key in best_scores:
                if standard in key and 'num' not in key:
                    num_list[-1].append(best_scores[key])
        print(models[i], standard, num_list, sep='\t', file=f)

    f.close()

    # files = sorted(os.listdir(path))
    # for file_name in files:
    #     # print(file_name)
    #     best_scores = cal_best_scores(path + '/' + file_name)
    #     num_list.append([])
    #     for key in best_scores:
    #         if standard in key and 'num' not in key:
    #             num_list[-1].append(best_scores[key])
    #             # print(key + ':', best_scores[key + '@num'])
    #             # print("{}: {}".format(key, best_scores[key]))
    #     # print('')
    #     print(num_list)


# draw_hit_map('log/memetracker', 'memetracker')
draw_baseline('res/baseline.txt')
# write_res('hits')
# write_res('map')