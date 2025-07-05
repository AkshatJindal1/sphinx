import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables (including your API key)
load_dotenv()

# Configure the Gemini API with your API key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def extract_hr_info(job_description_text, cv_text):
    """
    Extracts key HR information using Gemini 1.5 Pro.
    """
    model = genai.GenerativeModel('gemini-1.5-flash-latest')

    prompt = f"""
    You are an expert HR Technology Analyst. Your task is to extract key information from a Job Description and a Candidate's CV and return it as a single, well-formed JSON object.

    Adhere to these rules strictly:
    1.  Analyze the full text of both documents to understand the context.
    2.  The output MUST be only the JSON object, with no introductory text, explanations, or markdown formatting.
    3.  For skill extraction, capture the context in which the skill is mentioned (e.g., "5+ years experience", "familiarity with", "led a project using").
    4.  Infer seniority level based on keywords like "Senior", "Lead", "II", "Junior", or years of experience requested. If not specified, default to "Not Specified".
    5.  If a field or section is not found in the documents, use an empty array `[]` for lists or an empty string `""` for text fields. Do not invent information.

    Here is the JSON schema you must follow:
    {{
      "job_description": {{
        "role_title": "string",
        "seniority_level": "string (e.g., Junior, Mid-level, Senior, Staff/Principal, Not Specified)",
        "required_skills": [{{ "skill": "string", "context": "string" }}],
        "optional_skills": [{{ "skill": "string", "context": "string" }}]
      }},
      "candidate_cv": {{
        "extracted_name": "string",
        "contact_info": {{ "email": "string", "phone": "string" }},
        "skills_mentioned": [{{ "skill": "string", "context": "string" }}],
        "external_links": {{ "github": "url", "linkedin": "url", "portfolio": "url" }},
        "work_experience": [{{ "role": "string", "company": "string", "duration": "string", "summary": "string" }}]
      }}
    }}

    --- JOB DESCRIPTION TEXT ---
    {job_description_text}
    --- END JOB DESCRIPTION ---
    --- CV TEXT ---
    {cv_text}
    --- END CV TEXT ---
    """

    try:
        response = model.generate_content(prompt)
        # Assuming the model returns valid JSON directly.
        # You might need to strip markdown ```json...``` if the model adds it.
        response_text = response.text.strip()
        if response_text.startswith("```json") and response_text.endswith("```"):
            response_text = response_text[7:-3].strip()
        
        return json.loads(response_text)
    except Exception as e:
        print(f"Error extracting info: {e}")
        print(f"Model raw output: {response.text}")
        return None

# Example Usage (using your provided input)
job_desc = """
{Development:
Develop robust, scalable, and efficient data pipelines.
Manage platform solutions to support data engineering needs to ensure seamless integration and performance.
Write clean, efficient, and maintainable code.
Data Management and Optimization:
Ensure data quality, integrity, and security across all data pipelines.
Optimize data processing workflows for performance and cost-efficiency.
Develop and maintain comprehensive documentation for data pipelines and related processes.
Innovation and Continuous Improvement:
Stay current with emerging technologies and industry trends in big data and cloud computing.
Propose and implement innovative solutions to improve data processing and analytics capabilities.
Continuously evaluate and improve existing data infrastructure and processes.
Qualifications

Bachelor’s or Master’s degree in Computer Science, Engineering, or a related field.
2+ years of experience in software engineering with a focus on data engineering and building data platform
Strong programming experience using Python or Java.
Experience of the Big data technologies like Apache Spark, Amazon EMR, Apache Iceberg, Amazon Redshift, etc or Similar technologies
Experience in RDBMS(Postgres, MySql, etc) and NoSQL(MongoDB, DynamoDB, etc) database
Experience in AWS cloud services (e.g., Lambda, S3, Athena, Glue) or comparable cloud technologies.
Experience in CI/CD.
Experience working in Event driven and Serverless Architecture
Experience with platform solutions and containerization technologies (e.g., Docker, Kubernetes).
Excellent problem-solving skills and the ability to work in a fast-paced, dynamic environment.
Strong communication skills, both written and verbal.
}
"""

cv_text = """
{"Vivek Pal
ƒ +918630670454
# vivekpal2407@gmail.com
ï Vivek Pal
§ vivekpal24
Ð LeetCode
Ð CodeChef
Ð Codeforces
Education
Indian Institute of Information Technology, Una
Nov 2022 — June 2026
Bachelor of Technology in Information Technology
CGPA: 7.55
Experience
Redux Corporation
Sept 2023 — Dec 2023
Android Development Intern
Remote,UttarPradesh,India
• Transformed backend integration and database connectivity via REST APIs, elevating data sync efficiency by 30%.
• Optimized data retrieval speeds by 25% by refining the database setup and optimizing maintenance with Firebase
Realtime Database and Firebase Console.
• Minimized codebase complexity by 40% through the implementation of MVP architecture, improving organization
and readability.
• Accelerated revenue growth by 20% by integrating AdMob for effective app monetization and ad management.
Sky Trade
Dec 2023 — Feb 2024
Research & Development Intern
Remote,Delaware,U.S.
• Improved location accuracy by 35% through integration of real-time GPS tracking and coordinates.
• Revamped user interface responsiveness by 40% through advanced Flutter app features.
• Strengthened flight stability by 25% through analysis and fine-tuning of drone dynamics.
Broverg Corporation
Apr 2024 — Sept 2024
Software Developer Engineer Intern
Remote,Karnataka,India
• Increased user productivity by 30% through enhanced app functionality, emphasizing time tracking and performance
optimization.
• Reduced bug occurrences by 40% by implementing automated testing for Android apps using Katalon Studio.
• Boosted user engagement by 20% through deep linking integration, ensuring seamless connectivity between the
website and the app.
Projects
Mymedicos — Java, Firebase, Node.js, React.js
• Led the development of a live medical education platform on the Play Store, achieving 100+ downloads and boosting
engagement by 50%.
• Increased retention by 30% through quizzes, study materials, and a user-friendly library interface.
Nutri Kid— MERN stack, Rest APIs, ChatGPT API
• Developed an AI-powered platform leveraging Artificial Intelligence and Information Retrieval techniques to help
children find nutritious food, increasing user interaction by 40%.
• Engineered APIs to access data from 100+dishes ,enabling personalized recommendations and ingredient alternatives.
Tweet Box — Flutter, Firebase, Dart
• Built the Tweet Box app, increasing user engagement by 45% with community features, content sharing, and secure
Google login.
• Designed a content-sharing platform with Instagram-like photo posting via Cloud Firestore and Genix calling, boosting
interactions by 35%.
Achievements
• Codeforces (Boosted 123): Highest Rating: 1668 (Expert). Top 1000 out of 82K+ participants in India.
• CodeChef (main flag 47): Highest Rating: 2234 (6-Star). Top 150 out of 200K+ users in India.
• Secured Global Rank 408 out of 30K+ participants in Codeforces Round 1027 (Div. 3).
• Achieved peak rating of 1905 (Knight) on LeetCode and solved 1000+ problems across platforms.
Relevant Coursework
• Data Structures and Algorithms
• Database Management Systems
• OOPS
• Operating Systems
• Computer Networks
• Software Engineering
Skills
Programming Languages: C, C++, Java, Python, Kotlin, Dart, JavaScript, SQL.
Developer Tools: VS Code, Android Studio, Git, Docker, Google Cloud Platform (GCP), Microsoft Azure.
Technologies & Frameworks: FullStack (MongoDB, Express.js, React.js, Node.js), Flutter, Firebase, AWS, PostgreSQL,
NoSQL, Azure Storage, Unix/Linux Environments.
Systems & Concepts: Distributed Systems, Cloud Storage, Scalability, System Design, Microservices, Machine
Learning, Natural Language Processing (NLP), Information Retrieval, Data Storage Solutions, Data
Compression, TCP/IP Networking, Fault Tolerance, High Availability, Security.
Additional Skills: UI Development, Android App Development, REST APIs, Agile Methodologies, CI/CD.
"""

if __name__ == "__main__":
    extracted_data = extract_hr_info(job_desc, cv_text)
    if extracted_data:
        print(json.dumps(extracted_data, indent=2))
    else:
        print("Failed to extract data.")