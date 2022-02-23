import os



def read_input_file(file_name):
    res = []
    with open(file=file_name) as f:
        for i in range(0, int(f.readline())):
            def parse_line(line):
                res = []
                for i in range(1, int(line.split(' ')[0]) + 1):
                    res.append(line.split(' ')[i].replace('\n', ''))
                return res
            likes = parse_line(f.readline())
            dislikes = parse_line(f.readline())
            res.append((likes, dislikes))
    return res


def write_output_file(ingrideints, file_name):
    line = str(len(ingrideints)) + ' '
    for ingrideint in ingrideints:
        line += ingrideint + ' '

    os.makedirs('outputs', exist_ok=True)
    with open(file=file_name, mode='w') as f:
        f.write(line)


def all_ingredients(client_infos):
    ingredients = []
    for likes, dislikes in client_infos:
        [ingredients.append(like) for like in likes]
        [ingredients.append(dislike) for dislike in dislikes]
    return list(set(ingredients))

def find_valid_client_indexes(client_infos, ingridentes):
    valid_client_indexes = []
    for i in range(len(client_infos)):
        likes, dislikes = client_infos[i]
        check = not any(item in ingridentes for item in dislikes) and all(item in ingridentes for item in likes)
        if check:
            valid_client_indexes.append(i)
    return valid_client_indexes


data_file_names = ['inputs/a_an_example.in.txt', 'inputs/b_basic.in.txt', 'inputs/c_coarse.in.txt', 'inputs/d_difficult.in.txt', 'inputs/e_elaborate.in.txt']
# data_file_names = ['./a_an_example.in.txt']

def find_ingridents(client_infos):
    ingredients = all_ingredients(client_infos)

    return ingredients

def process(data_file_name):
    client_infos = read_input_file(data_file_name)
    ingredients = find_ingridents(client_infos)
    print(data_file_name, len(find_valid_client_indexes(client_infos, ingredients)))
    write_output_file(ingredients, 'outputs/' + data_file_name.split('/')[1].split("_")[0] + '_out.txt')


for data_file_name in data_file_names:
    process(data_file_name)