def getMinCost(crew_id, job_id):
    crew_id.sort()
    job_id.sort()
    return sum(abs(c - j) for c, j in zip(crew_id, job_id))
