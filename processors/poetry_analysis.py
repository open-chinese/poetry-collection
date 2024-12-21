import os
import matplotlib.pyplot as plt
from file_util import FileUtil
from dict_util import DictUtil
from matplotlib import rcParams
import json

plt.rcParams['font.sans-serif'] = ['SimHei']  # to show Chinese
plt.rcParams['axes.unicode_minus'] = False  # to show minus

data_dir = '../volumes'


def load_file(file):
    with open(file, 'r', encoding='utf-8') as rf:
        data = json.load(rf)
        return data


def plot_pie_chart(data, title):
    categories = list(data.keys())
    counts = list(data.values())
    font_size = 20
    colors = plt.cm.Paired(range(len(categories)))

    plt.figure(figsize=(20, 20))

    # wedges, texts, autotexts = plt.pie(
    #     counts,
    #     labels=by_forms,
    #     autopct='%1.1f%%',
    #     textprops={'fontsize': font_size},
    #     startangle=90,
    #     colors=colors,
    #     wedgeprops={'edgecolor': 'white'}
    # )
    # plt.legend(wedges, by_forms, title=title, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=font_size)
    # plt.title(title, fontsize=font_size)
    # plt.tight_layout()
    # plt.savefig('../images/poets_count_by_dynasty.png', format='png')

    plt.pie(counts,
            labels=categories,
            autopct='%1.1f%%',
            startangle=90,
            counterclock=False,
            colors=colors,
            textprops={'fontsize': font_size})
    plt.title(title, fontsize=font_size + 4)
    plt.savefig('../images/poets_count_by_dynasty.png', format='png')

    # plt.show()


def plot_horizontal_bar_chart(data, title, x_label, y_label, file_name):
    categories = list(data.keys())
    counts = list(data.values())

    font_size = 16
    plt.figure(figsize=(20, 30))
    colors = plt.cm.tab10.colors[:len(categories)]
    # colors = plt.cm.Paired(range(len(by_forms)))

    plt.barh(categories, counts, color=colors)
    plt.xlabel(x_label, fontsize=font_size)
    plt.ylabel(y_label, fontsize=font_size)
    plt.title(title, fontsize=font_size + 4)
    plt.yticks(fontsize=font_size)
    plt.tight_layout()

    plt.savefig(file_name, format='png')
    # plt.show()


def load_all_poets():
    files = FileUtil.get_files(data_dir)
    poems = []
    for file in files:
        items = load_file(file)
        poems.extend(items)
    return poems


def analysis_top_poets_by_poems_count(poems):
    # analysis by poets
    poems_by_poets = {}
    for poem in poems:
        d = poem.get('dynasty', '朝代未知')
        if not d or d == 'None':
            d = '朝代未知'
        key = '{0}-{1}'.format(d, poem.get('author'))
        if key not in poems_by_poets:
            poems_by_poets[key] = [poem]
        else:
            poems_by_poets[key].append(poem)

    poems_by_poets_count = {k: len(v) for k, v in poems_by_poets.items()}
    poems_by_poets_count = DictUtil.sort_dict_by_value(poems_by_poets_count, reverse=True)
    poems_by_poets_top100 = {}
    for k, v in list(poems_by_poets_count.items())[:100]:
        print(k, v)
        poems_by_poets_top100[k] = v

    poems_by_poets_top100 = DictUtil.sort_dict_by_value(poems_by_poets_top100, reverse=False)
    plot_horizontal_bar_chart(poems_by_poets_top100,
                              title='诗人作品数量',
                              x_label='诗词数量',
                              y_label='诗人',
                              file_name='../images/poets_works_count_all.png')


def analysis_poems_by_dynasty(poems):
    poems_by_dynasty = {}
    for poem in poems:
        d = poem.get('dynasty', '朝代未知')
        if not d or d == 'None':
            d = '朝代未知'
        if d not in poems_by_dynasty:
            poems_by_dynasty[d] = 1
        else:
            poems_by_dynasty[d] += 1

    poems_by_dynasty = {k: v for k, v in poems_by_dynasty.items() if v / sum(poems_by_dynasty.values()) > 0.001}
    plot_pie_chart(poems_by_dynasty, title='按朝代诗词数量')


def analysis_poems_tang_dynasty(poems):
    poems_by_poets = {}
    for poem in poems:
        d = poem.get('dynasty', '朝代未知')
        poet = poem.get('author')
        if d != '唐':
            continue
        if poet not in poems_by_poets:
            poems_by_poets[poet] = 1
        else:
            poems_by_poets[poet] += 1

    poems_by_poets_count = {k: v for k, v in poems_by_poets.items()}
    poems_by_poets_count = DictUtil.sort_dict_by_value(poems_by_poets_count, reverse=True)
    poems_by_poets_top100 = {}
    for k, v in list(poems_by_poets_count.items())[:100]:
        print(k, v)
        poems_by_poets_top100[k] = v

    poems_by_poets_top100 = DictUtil.sort_dict_by_value(poems_by_poets_top100, reverse=False)
    plot_horizontal_bar_chart(poems_by_poets_top100,
                              title='诗人作品数量',
                              x_label='诗词数量',
                              y_label='诗人',
                              file_name='../images/poets_works_count_tang.png')


if __name__ == '__main__':
    poems = load_all_poets()
    #analysis_top_poets_by_poems_count(poems)
    #analysis_poems_by_dynasty(poems)
    analysis_poems_tang_dynasty(poems)
