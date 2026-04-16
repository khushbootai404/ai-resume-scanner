import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def match_resume(job_desc, resume_text):
    try:
        text = job_desc + " " + resume_text
        vec = vectorizer.transform([text])

        # probability score (0 to 1)
        prob = model.predict_proba(vec)[0][1]

        return round(prob * 100, 2)

    except Exception as e:
        print("Error:", e)
        return 0