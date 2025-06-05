import PyPDF2
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            resume_text = ''
            for page in reader.pages:
                resume_text += page.extract_text()
            return resume_text
    except Exception as e:
        peint(f"Error Reading resume: {e}")
        return ''
    
def load_job_descriptions(csv_path):
    try:
        df = pd.read_csv(csv_path)
        return df['Job Title'].tolist(), df['Description'].tolist()
    except Exception as e:
        print(f"Error reading job description: {e}")
        return [], []
    
def match_resume_to_jobs(resume_text, job_description, job_titles, top_n=3):
    try:
        documents = [resume_text] + job_description
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(documents)

        similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

        sorted_indices = similarities.argsort()[::-1][:top_n]
        top_matches = [(job_titles[i], round(similarities[i] * 100, 2)) for i in sorted_indices]

        return top_matches
    except Exception as e:
        print(f"Error during matches: {e}")
        return []
    
if __name__ == "__main__":
    resume_text = extract_text_from_pdf('sample_resume.pdf')
    job_titles, job_descriptions = load_job_descriptions('job_descriptions.csv')

    if resume_text and job_descriptions:
        matches = match_resume_to_jobs(resume_text, job_descriptions, job_titles)
        print("\nTop job Matches:")
        for title, score in matches:
            print(f"{title} - Match Score: {score}%")
    else:
        print("Resume Or Job Descriptions not loaded Properly.")
