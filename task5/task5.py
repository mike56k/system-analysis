import json
import numpy as np  

def task(rankA: str, rankB:str) -> str:
    rankingA = json.loads(rankA)
    rankingB = json.loads(rankB)
    def rank_len(ranking) -> int:
        length = 0
        for i in ranking:
            if type(i) is str:
                length += 1
            else:
                length += len(i)
        return length

    def rel_mat(ranking):
        ranks = dict()
        rank_l = rank_len(ranking)
        for i, rank in enumerate(ranking):
            if type(rank) is str:
                ranks[int(rank)] = i
            else:
                for r in rank:
                    ranks[int(r)] = i

        result = []
        for i in range(rank_l):
            result.append([1 if ranks[i+1] <= ranks[j+1] else 0 for j in range(rank_l)])
        return np.matrix(result)



    y_a, y_b = rel_mat(rankingA), rel_mat(rankingB)
    y_a_t, y_b_t = y_a.transpose(), y_b.transpose()
    y_a_b, y_a_b_t = np.multiply(y_a, y_b), np.multiply(y_a_t, y_b_t)
    conflicts = []

    for i in range(y_a_b.shape[0]):
        for j in range(y_a_b[i].shape[1]):
            if int(y_a_b[i,j]) == 0 and int(y_a_b_t[i,j]) == 0:
                if (str(j + 1), str(i + 1)) not in conflicts:
                    conflicts.append((str(i + 1),str(j + 1)))

    return json.dumps(conflicts)

print(task("[\"1\", [\"2\",\"3\"],\"4\", [\"5\", \"6\", \"7\"], \"8\", \"9\", \"10\"]",
            "[[\"1\",\"2\"], [\"3\",\"4\",\"5\"], \"6\", \"7\", \"9\", [\"8\",\"10\"]]"))