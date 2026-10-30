import streamlit as st
import pandas as pd

# PAGE CONFIGURATION
# CUSTOM CSS
st.markdown("""
<style>
    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    h1 {
        font-weight: 800;
        letter-spacing: -1px;
    }

    h2, h3 {
        font-weight: 700;
    }

    [data-testid="stMetric"] {
        background-color: rgba(128, 128, 128, 0.08);
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.2);
    }

    [data-testid="stMetricValue"] {
        font-size: 25px;
    }

    div.stButton > button {
        border-radius: 8px;
        font-weight: 600;
        padding: 8px 20px;
    }

    div[data-testid="stForm"] {
        border-radius: 12px;
        padding: 20px;
    }
</style>
""", unsafe_allow_html=True)

# SESSION STATE
if "feedback_submitted" not in st.session_state:
    st.session_state.feedback_submitted = False

# SIDEBAR NAVIGATION
st.sidebar.title("👨‍💻 Rocky's Portfolio")
st.sidebar.write("Personal Website and Portfolio")
st.sidebar.divider()

page = st.sidebar.radio(
    "Navigate",
    ["Home", "About Me", "Skills", "Projects", "Contact"]
)

st.sidebar.divider()
st.sidebar.caption("BSIT Student | CIT University")

# HOME PAGE
if page == "Home":

    st.title("👋 Hello, I'm Rocky Decretales Jr.")
    st.subheader("BSIT Student | Aspiring Software Developer")

    st.write(
        """
        Welcome to my personal portfolio!

        I am an Information Technology student interested in software
        development, web technologies, and learning how technology
        can solve real-world problems.
        """
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Academic Program", "BSIT")

    with col2:
        st.metric("University", "CIT-U")

    with col3:
        st.metric("Career Goal", "Developer")

    st.divider()

    st.subheader("Explore My Portfolio")
    st.write(
        "Use the navigation menu on the left to learn more about "
        "my background, skills, projects, and contact information."
    )

    if st.button("View My Projects"):
        st.session_state.feedback_submitted = False
        st.info("Select Projects from the navigation menu.")

# ABOUT ME PAGE

# ABOUT ME PAGE
elif page == "About Me":

    st.title("About Me")
    st.write("Get to know more about my background, education, and interests.")

    st.divider()

    # PERSONAL INTRODUCTION
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown(
            """
            <div style="
                background-color: rgba(128,128,128,0.10);
                border: 1px solid rgba(128,128,128,0.25);
                border-radius: 15px;
                padding: 45px 15px;
                text-align: center;
            ">
                <div style="font-size: 75px;">👨‍💻</div>
                <h3>Rocky Decretales Jr.</h3>
                <p>BSIT Student</p>
                <p>CIT University</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.subheader("Hello! I'm Rocky.")

        st.write(
            """
            I am an Information Technology student at CIT University
            with an interest in software development and technology.

            Throughout my academic journey, I have explored different
            areas of programming, web development, database management,
            and application development.

            I enjoy learning new technologies, working on practical
            projects, and improving my problem-solving skills.
            """
        )

        st.info(
            "My goal is to become a skilled software developer "
            "and build applications that solve real-world problems."
        )

    st.divider()

    # ABOUT ME TABS
    tab1, tab2, tab3, tab4 = st.tabs([
        "Background",
        "Education",
        "Interests",
        "Goals & Milestones"
    ])

    with tab1:
        st.subheader("My Background")

        st.write(
            """
            My interest in technology developed through my experience
            as a student and my exposure to programming and software
            development.

            I started exploring programming through academic activities
            and gradually gained experience in creating applications
            using different programming languages and frameworks.

            Each project gives me an opportunity to learn, solve
            problems, and understand how software is developed.
            """
        )

    with tab2:
        st.subheader("Educational Background")

        st.markdown("### 🎓 CIT University")

        st.write("**Program:** Bachelor of Science in Information Technology")
        st.write("**Academic Level:** Upcoming 4th Year")
        st.write("**Academic Year:** 2026–2027")

        st.divider()

        st.write("**Areas of Academic Learning:**")

        education_areas = [
            "Programming and Software Development",
            "Database Management",
            "Web Application Development",
            "Data Analytics",
            "Systems Integration and Architecture",
            "Cybersecurity and Quality Assurance"
        ]

        for area in education_areas:
            st.write(f"• {area}")

    with tab3:
        st.subheader("My Interests and Hobbies")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 💻 Technology")
            st.write(
                """
                - Programming
                - Web Development
                - Learning new technologies
                - Building applications
                """
            )

            st.markdown("### 🎵 Entertainment")
            st.write(
                """
                - Listening to music
                - Watching movies
                - Spending time with friends
                """
            )

        with col2:
            st.markdown("### 🏃 Lifestyle")
            st.write(
                """
                - Working out
                - Cooking
                - Outdoor activities
                """
            )

            st.markdown("### 🌊 Adventures")
            st.write(
                """
                - Skating
                - Surfing
                - Camping
                """
            )

    with tab4:
        st.subheader("My Goals")

        st.write(
            """
            I want to continue improving my technical knowledge
            and gain more practical experience in software development.
            """
        )

        st.markdown("### Short-Term Goals")

        st.write(
            """
            - Complete my Information Technology degree.
            - Improve my React.js and Python programming skills.
            - Build more functional and practical applications.
            - Strengthen my problem-solving abilities.
            """
        )

        st.markdown("### Long-Term Goals")

        st.write(
            """
            - Pursue a career in software development.
            - Gain professional experience in the IT industry.
            - Continue learning modern software technologies.
            - Develop applications that provide meaningful solutions.
            """
        )

        st.divider()

        st.subheader("Academic and Project Milestones")

        milestones = [
            ("Programming Foundation", "Started developing programming and problem-solving skills."),
            ("Web Development", "Worked with Django, React.js, and other web technologies."),
            ("Academic Projects", "Developed applications such as EduBridge, DineDiscover, and QREntry."),
            ("Current Journey", "Continuing my BSIT studies and improving my development skills.")
        ]

        for title, description in milestones:
            st.markdown(f"**✓ {title}**")
            st.caption(description)


# SKILLS PAGE

# SKILLS PAGE
elif page == "Skills":

    st.title("My Technical Skills")

    st.write(
        """
        This section presents the programming languages, frameworks,
        databases, and development tools I have explored through
        academic activities and personal projects.
        """
    )

    st.divider()

    # SKILL CATEGORIES
    tab1, tab2, tab3, tab4 = st.tabs([
        "Programming",
        "Frameworks",
        "Databases",
        "Development Tools"
    ])

    with tab1:
        st.subheader("Programming Languages")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🐍 Python")
            st.caption("Used in programming exercises and Django development.")

            st.markdown("### ☕ Java")
            st.caption("Used in object-oriented programming and Java Swing.")

        with col2:
            st.markdown("### 🌐 JavaScript")
            st.caption("Used in interactive web application development.")

            st.markdown("### 🎨 HTML and CSS")
            st.caption("Used in structuring and styling web pages.")

    with tab2:
        st.subheader("Frameworks and Libraries")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### ⚛️ React.js")
            st.caption("Used for building interactive user interfaces.")

            st.markdown("### 🐍 Django")
            st.caption("Used for backend development and web applications.")

        with col2:
            st.markdown("### 🎨 Tailwind CSS")
            st.caption("Used for styling responsive web interfaces.")

            st.markdown("### ⚡ Vite")
            st.caption("Used as a frontend development and build tool.")

    with tab3:
        st.subheader("Database Technologies")

        st.markdown("### 🗄️ MySQL")
        st.caption("Relational database management and SQL queries.")

        st.markdown("### 🗄️ PostgreSQL / Supabase")
        st.caption("Database storage and backend integration.")

        st.markdown("### 📁 SQLite")
        st.caption("Lightweight relational database for application development.")

    with tab4:
        st.subheader("Development Tools")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 💻 Visual Studio Code")
            st.caption("Code editing and development.")

            st.markdown("### 🔧 Git and GitHub")
            st.caption("Version control and source code management.")

        with col2:
            st.markdown("### 📓 Jupyter Notebook")
            st.caption("Python programming and data analysis.")

            st.markdown("### 🧪 Postman / CURL")
            st.caption("Testing and checking API endpoints.")

    st.divider()

    # INTERACTIVE SKILL ASSESSMENT
    st.subheader("Interactive Skill Assessment")

    st.write(
        """
        Assess your current proficiency in each technology.
        Use the sliders to select your actual skill level.
        """
    )

    skill_levels = {
        "Python": 3,
        "JavaScript": 3,
        "React.js": 3,
        "HTML / CSS": 3,
        "Django": 3,
        "SQL / Database": 3,
        "Git and GitHub": 3
    }

    st.caption(
        "The initial values are placeholders. Adjust them honestly "
        "based on your current experience."
    )

    col1, col2 = st.columns(2)

    skill_names = list(skill_levels.keys())

    for index, skill in enumerate(skill_names):

        with col1 if index % 2 == 0 else col2:

            skill_levels[skill] = st.slider(
                skill,
                min_value=1,
                max_value=5,
                value=skill_levels[skill],
                key=f"skill_{skill}"
            )

    st.divider()

    # SKILL LEVEL GUIDE
    st.subheader("Proficiency Level Guide")

    level_guide = pd.DataFrame({
        "Level": [1, 2, 3, 4, 5],
        "Description": [
            "Beginner",
            "Basic",
            "Intermediate",
            "Advanced",
            "Expert"
        ]
    })

    st.table(level_guide)

    # SKILL DATA TABLE
    st.subheader("My Skills Overview")

    skill_data = pd.DataFrame({
        "Technology": skill_levels.keys(),
        "Proficiency Level": skill_levels.values()
    })

    st.dataframe(
        skill_data,
        use_container_width=True,
        hide_index=True
    )

    # SKILL CHART
    st.subheader("Visual Skill Assessment")

    st.bar_chart(
        skill_data.set_index("Technology"),
        y="Proficiency Level",
        y_label="Proficiency Level (1–5)"
    )

    average_level = sum(skill_levels.values()) / len(skill_levels)

    st.metric(
        "Average Self-Assessed Skill Level",
        f"{average_level:.2f} / 5"
    )

    st.caption(
        "Note: This chart represents personal self-assessment, "
        "not a formal technical examination."
    )

    st.divider()

    # OTHER PROFESSIONAL SKILLS
    st.subheader("Additional Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.write("✓ Problem-solving")
        st.write("✓ Team collaboration")
        st.write("✓ Project development")

    with col2:
        st.write("✓ Technical research")
        st.write("✓ Database management")
        st.write("✓ Continuous learning")


# PROJECTS PAGE

# PROJECTS PAGE
elif page == "Projects":

    st.title("My Projects")

    st.write(
        """
        A collection of academic and personal development projects
        that demonstrate my experience in programming, web development,
        database management, and application development.
        """
    )

    st.divider()

    # PROJECT DATA
    projects = [
        {
            "name": "EduBridge",
            "category": "Web Development",
            "role": "Student Developer",
            "description": (
                "A Parent-Teacher Mobile Bridge for Basic Education "
                "designed to improve communication between parents "
                "and teachers."
            ),
            "tools": [
                "React.js",
                "Vite",
                "Tailwind CSS"
            ],
            "outcome": (
                "Developed a web application prototype and deployed "
                "the frontend using Vercel."
            ),
            "link": "https://edubridge01.vercel.app/",
            "link_type": "live"
        },
        {
            "name": "DineDiscover",
            "category": "Web Development",
            "role": "Student Developer",
            "description": (
                "A restaurant discovery and food ordering application "
                "that allows users to browse restaurants, view menus, "
                "manage their shopping cart, and confirm orders."
            ),
            "tools": [
                "React.js",
                "Vite",
                "Tailwind CSS"
            ],
            "outcome": (
                "Developed an interactive frontend application "
                "with restaurant browsing, menu viewing, cart "
                "functionality, and order confirmation."
            ),
            "link": "https://github.com/Gongz024/dine-discover",
            "link_type": "github"
        },
        {
            "name": "QREntry",
            "category": "Full-Stack Development",
            "role": "Student Developer",
            "description": (
                "An event ticketing system designed to support "
                "event registration and QR-based ticket management."
            ),
            "tools": [
                "Python",
                "Django",
                "Supabase PostgreSQL",
                "SendGrid"
            ],
            "outcome": (
                "Developed application features involving event "
                "ticketing, database integration, and email functionality."
            ),
            "link": "https://github.com/Gongz024/CSIT327-G2-QREntry",
            "link_type": "github"
        }
    ]

    # PROJECT SUMMARY
    st.subheader("Project Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Projects", len(projects))

    with col2:
        st.metric("Development Areas", "2")

    with col3:
        st.metric("Project Types", "Academic")

    st.divider()

    # PROJECT CATEGORY FILTER
    st.subheader("Explore My Work")

    selected_category = st.selectbox(
        "Filter projects by category",
        [
            "All Projects",
            "Web Development",
            "Full-Stack Development"
        ]
    )

    # FILTER LOGIC
    if selected_category == "All Projects":
        filtered_projects = projects
    else:
        filtered_projects = [
            project for project in projects
            if project["category"] == selected_category
        ]

    st.caption(
        f"Showing {len(filtered_projects)} project(s)"
    )

    # DISPLAY PROJECT CARDS
    for index, project in enumerate(filtered_projects):

        with st.container(border=True):

            col1, col2 = st.columns([3, 1])

            with col1:
                st.subheader(
                    f"{index + 1}. {project['name']}"
                )

                st.caption(project["category"])

            with col2:
                st.write("**My Role**")
                st.write(project["role"])

            st.write(project["description"])

            st.markdown("**Technologies Used**")

            # DISPLAY TECHNOLOGY TAGS
            st.write(" | ".join(project["tools"]))

            st.markdown("**Project Outcome**")

            st.write(project["outcome"])

            st.divider()

            # PROJECT LINKS
            if project["link_type"] == "live":

                st.link_button(
                    "🌐 Visit Live Project",
                    project["link"]
                )

            else:

                st.link_button(
                    "💻 View GitHub Repository",
                    project["link"]
                )

    st.divider()

    # PROJECT FEEDBACK
    st.subheader("Project Feedback")

    st.write(
        "Which of my projects interests you the most?"
    )

    project_choice = st.selectbox(
        "Select a project",
        [project["name"] for project in projects],
        key="project_feedback"
    )

    st.success(
        f"You selected {project_choice}. "
        "Thank you for exploring my work!"
    )

    st.info(
        """
        These projects represent my learning experience,
        technical development, and continuous improvement
        as an Information Technology student.
        """
    )

# CONTACT PAGE

# CONTACT PAGE
elif page == "Contact":

    st.title("Contact Me")

    st.write(
        """
        Thank you for visiting my portfolio!

        If you have questions, suggestions, or feedback about my
        projects, feel free to send me a message using the form below.
        """
    )

    st.divider()

    # CONTACT INFORMATION
    st.subheader("Get in Touch")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 👨‍💻 Student Developer")
        st.write("Rocky Decretales Jr.")
        st.write("BSIT Student | CIT University")

    with col2:
        st.markdown("### 🔗 Online Portfolio")
        st.write("Explore my projects and development work.")
        st.link_button(
            "Visit EduBridge",
            "https://edubridge01.vercel.app/"
        )

    st.divider()

    # INITIALIZE SESSION STATE
    if "feedback_messages" not in st.session_state:
        st.session_state.feedback_messages = []

    # CONTACT FORM
    st.subheader("Send Me a Message")

    with st.form("contact_form"):

        name = st.text_input(
            "Full Name",
            placeholder="Enter your name"
        )

        email = st.text_input(
            "Email Address",
            placeholder="Enter your email address"
        )

        message_type = st.selectbox(
            "Message Category",
            [
                "General Inquiry",
                "Project Feedback",
                "Collaboration",
                "Suggestion",
                "Other"
            ]
        )

        rating = st.radio(
            "How would you rate my portfolio?",
            [
                "Excellent",
                "Very Good",
                "Good",
                "Needs Improvement"
            ],
            horizontal=True
        )

        message = st.text_area(
            "Your Message",
            placeholder="Write your message or feedback here..."
        )

        subscribe = st.checkbox(
            "I am interested in receiving project updates."
        )

        submitted = st.form_submit_button(
            "Submit Feedback",
            use_container_width=True
        )

        if submitted:

            if not name.strip() or not message.strip():

                st.warning(
                    "Please enter your name and message before submitting."
                )

            elif email.strip() and (
                "@" not in email or "." not in email.split("@")[-1]
            ):

                st.warning(
                    "Please enter a valid email address."
                )

            else:

                feedback = {
                    "Name": name,
                    "Email": email,
                    "Category": message_type,
                    "Rating": rating,
                    "Message": message,
                    "Project Updates": (
                        "Yes" if subscribe else "No"
                    )
                }

                st.session_state.feedback_messages.append(feedback)

                st.success(
                    f"Thank you, {name}! Your feedback has been submitted."
                )

    st.divider()

    # SUBMISSION SUMMARY
    st.subheader("Feedback Submission")

    total_feedback = len(st.session_state.feedback_messages)

    st.metric(
        "Messages Submitted This Session",
        total_feedback
    )

    if total_feedback > 0:

        st.write("**Your submitted feedback:**")

        for index, feedback in enumerate(
            st.session_state.feedback_messages
        ):

            with st.expander(
                f"Feedback {index + 1} - {feedback['Name']}"
            ):

                st.write(f"**Name:** {feedback['Name']}")
                st.write(f"**Email:** {feedback['Email']}")
                st.write(f"**Category:** {feedback['Category']}")
                st.write(f"**Portfolio Rating:** {feedback['Rating']}")
                st.write(f"**Message:** {feedback['Message']}")
                st.write(
                    f"**Project Updates:** {feedback['Project Updates']}"
                )

    else:

        st.info(
            "No feedback has been submitted yet. "
            "Your messages will appear here after submission."
        )

    st.divider()

    st.caption(
        "Thank you for taking the time to explore my portfolio!"
    )
