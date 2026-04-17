def match_resume(resume_text, job_desc):
    resume_text = resume_text.lower()
    job_desc = job_desc.lower()

    job_keywords = job_desc.split()

    matched = 0

    for word in job_keywords:
        if word in resume_text:
            matched += 1

    if len(job_keywords) == 0:
        return 0

    score = (matched / len(job_keywords)) * 100
    return round(score, 2)