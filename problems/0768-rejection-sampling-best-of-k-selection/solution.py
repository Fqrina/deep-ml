
def rejection_sampling_best_of_k(candidates, scores):
    """
    Select the highest-scoring candidate per prompt.

    Args:
        candidates: list of N lists, each containing K candidate outputs.
        scores: list of N lists, each containing K reward scores.

    Returns:
        List of N selected candidates.
    """
    ans = []
    for row in range(len(candidates)):
        mx = -1e9
        item = ""
        for column in range(len(candidates[row])):
            if scores[row][column] > mx:
                mx = scores[row][column]
                item = candidates[row][column]
        ans.append(item)
    return ans
    