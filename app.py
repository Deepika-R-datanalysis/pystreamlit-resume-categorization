def main():
    st.title("Resume Screening App")
    uploaded_file = st.file_uploader('Upload Resume', type=['txt', 'pdf'])

    if uploaded_file is not None:
        try:
            resume_bytes = uploaded_file.read()
            resume_text = resume_bytes.decode('utf-8')
        except UnicodeDecodeError:
            # If UTF-8 decoding fails, try decoding with 'latin-1'
            resume_text = resume_bytes.decode('latin-1')

        cleaned_resume = cleanresume(resume_text)
        input_features = tfidf.transform([cleaned_resume])
        prediction_id = Model1.predict(input_features)[0]
        st.write(prediction_id)

        # Map category ID to category name
        category_mapping = {
            6: "Data Science",
            12: "HR",
            0: "Advocate",
            1: "Arts",
            24: "Web Designing",
            16: "Mechanical Engineer",
            22: "Sales",
            14: "Health and fitness",
            5: "Civil Engineer",
            15: "Java Developer",
            4: "Business Analyst",
            21: "SAP Developer",
            2: "Automation Testing",
            11: "Electrical Engineering",
            18: "Operations Manager",
            20: "Python Developer",
            8: "DevOps Engineer",
            17: "Network Security Engineer",
            19: "PMO",
            7: "Database",
            13: "Hadoop",
            10: "ETL Developer",
            9: "DotNet Developer",
            3: "Blockchain",
            23: "Testing"
        }

        category_name = category_mapping.get(prediction_id, "Unknown")
        st.write("Predicted Category:", category_name)


# python main
if __name__ == "__main__":
    main()
