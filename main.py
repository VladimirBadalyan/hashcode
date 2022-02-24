import os

def read_input_file(file_name):
    contributors = []
    projects = []
    with open(file=file_name) as f:
        first_line = f.readline().split(' ')
        contributors_number, projects_number = int(first_line[0]), int(first_line[1])
        print(contributors_number, projects_number)

        def parse_contributer():
            contributor_info = f.readline().split(' ')
            name, skills_number = contributor_info[0], int(contributor_info[1])
            skills = dict()
            for i in range(skills_number):
                skill_info = f.readline().split(' ')
                skills[skill_info[0]] = int(skill_info[1])
            return name, skills

        for i in range(contributors_number):
            contributors.append(parse_contributer())
        print(contributors)

        def parse_project():
            project_info = f.readline().split(' ')
            skills = []
            for i in range(int(project_info[-1])):
                skill = f.readline().split(' ')
                skills.append((skill[0], int(skill[1])))
            return project_info[0], int(project_info[1]), int(project_info[2]), int(project_info[3]), skills


        for i in range(projects_number):
            projects.append(parse_project())
        print(projects)
    return contributors, projects


def write_output_file(projects_info, file_name):
    line = str(len(projects_info)) + '\n'
    for project_name, contributers in projects_info:
        line += project_name + '\n'
        for contributer in contributers:
            line += contributer + ' '
        line += '\n'
    os.makedirs('outputs', exist_ok=True)
    with open(file=file_name, mode='w') as f:
        f.write(line)


def most_relevant_developrs(project, developers):
    return developers

# RELEVANT PROJECTS ------------------------------------------


def most_relevent_projects_0(day, projects):
    projects_cpy = projects.copy()
    projects_cpy.sort(key=lambda p: p[2] / p[1], reverse=True)
    return projects_cpy


def most_relevent_projects_1(day, projects):
    projects_cpy = projects.copy()
    projects_cpy.sort(key=lambda p: p[3] - (p[1] + day))
    return projects_cpy


def most_relevent_projects_2(day, projects):
    projects = [p for p in projects if p[2] + min((p[3] - (p[1] + day), 0)) > 0]
    projects_cpy = projects.copy()
    projects_cpy.sort(key=lambda p: (p[3] - (p[1] + day)), reverse=True)
    return projects_cpy

# RELEVANT PROJECTS ------------------------------------------


def solve(contributers, projects):
    contributers

    # for i in range(100):

data_file_names = [
    # 'inputs/a_an_example.in.txt',
    'inputs/b_better_start_small.in.txt',
    # 'inputs/c_collaboration.in.txt',
    # 'inputs/d_dense_schedule.in.txt',
    # 'inputs/e_exceptional_skills.in.txt',
    # 'f_find_great_mentors.in.txt'
]


def process(data_file_name):
    contributors, projects = read_input_file(data_file_name)

    result = []
    # write_output_file(ingredients, 'outputs/' + data_file_name.split('/')[1].split("_")[0] + '_out.txt')

for data_file_name in data_file_names:
    process(data_file_name)