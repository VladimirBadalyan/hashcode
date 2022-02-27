from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching
import numpy as np

def assign_developers(project, developers):
    roles = project[4]
    skills = roles.keys()
    adj_matrix = []
    for skl in skills:
        row = []
        for dev in developers:
            if skl in dev[1]:
                if dev[1][skl] >= roles[skl]:
                    row.append(1)
                else:
                    row.append(0)
            else:
                row.append(0)
        adj_matrix.append(row)
    graph = csr_matrix(np.array(adj_matrix))
    assign = maximum_bipartite_matching(graph, perm_type='column')
    if -1 in assign:
        return False
    for i, skl in enumerate(skills):
        dev = developers[assign[i]]
        if dev[1][skl] == roles[skl]:
            dev[1][skl] = dev[1][skl] + 1
        dev[-1] = True
        project[-1].append(dev)
    return len(assign) == len(skills)
