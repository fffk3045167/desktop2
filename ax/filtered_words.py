# -*-coding:utf-8-*-


def filtered_words(f_file):
    filtered_list = []
    with open(f_file, 'r') as f:
        for line in f:
            filtered_list.append(line.strip())
    return filtered_list


def filtered_or_not(input_word, f_file):
    filtered_words_list = filtered_words(f_file)
    return input_word in filtered_words_list


def print_use_input(input_word, f_file):
    if filtered_or_not(input_word, f_file):
        return 'Freedom'
    return 'Human Rights'


if __name__ == '__main__':
    input_word = input('please input your word: ')
    f_file = 'filtered_words.txt'
    print(print_use_input(input_word, f_file))
