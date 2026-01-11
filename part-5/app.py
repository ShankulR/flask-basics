"""
Part 5: Mini Project - Personal Website with Flask
===================================================
A complete personal website using everything learned in Parts 1-4.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template

app = Flask(__name__)

# =============================================================================
# YOUR DATA - Customize this section with your own information!
# =============================================================================

PERSONAL_INFO = {
    'name': 'Shankul Pravin Rathod',
    'title': 'Full Stack Developer',
    'bio': 'A passionate full stack developer with experience in building web application using Java,Spring Boot ,and a problem solver at heart solving DSA problems on leetcode and GFG daily.',
    'email': 'shankulpravinrathod@gmail.com',
    'github': 'https://github.com/ShankulR',
    'linkedin': 'www.linkedin.com/in/shankul-pravin-rathod-788722375',
}

SKILLS = [
    {'name': 'Python', 'level': 50},
    {'name': 'HTML/CSS', 'level': 75},
    {'name': 'JDBC', 'level': 60},
    {'name': 'C++', 'level': 90},
    {'name': 'SQL', 'level': 75},
    {'name': 'JAVA', 'level': 80},
    {'name': 'Spring Boot', 'level': 45},
    {'name': 'Hibernate', 'level': 80},
    {'name': 'Junit ', 'level': 60}
]

PROJECTS = [
    {'id': 1, 'name': 'Personal Portfolio', 'description': 'A Flask-powered personal portfolio website.', 'tech': ['Python', 'Flask', 'HTML', 'CSS'], 'status': 'Completed'},
    {'id': 2, 'name': 'AI-Based Crop Advisory System', 'description': 'A Frontend and Backend Based Crop Advisory System for Farmers based on AI which uses the API key of Gemini .', 'tech': ['Java','Firebase', 'SpringBoot', 'Hibernate', 'REST API', 'ReactJS', 'HTML/CSS'], 'status': 'Completed'},
    {'id': 3, 'name': 'Water Measuring Gauge', 'description': 'Display Water level data by using an Arduino Sensory it demonstrates the water density and its level in a particular container. This setup is portable in nature', 'tech': ['Java', 'SpringBoot', 'Gemini-API','Arduino Sensor'], 'status': 'Completed'},
    {'id': 4, 'name': 'Inventory Management System', 'description': 'A portable and easy use system for managing the inventory for any type of business which also demonstrates the pending bookings, and payments.', 'tech': ['Java', 'SpringBoot', 'DOCKER', 'REST API', 'HTML/CSS'], 'status': 'Completed'},
    {'id': 5, 'name': 'Android based Finance Management System', 'description': 'A simple system for managing finances of large business use or for personal use for an individual to maintain a balance between its expenditure & Savings', 'tech': ['Android Studio(IDE)', 'Android Emulator', 'SDK', 'Gradle', 'XML/C++',], 'status': 'Planned'},
]


# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO)


@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS)


@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)


@app.route('/project/<int:project_id>')  # Dynamic route for individual project
def project_detail(project_id):
    project = None
    for p in PROJECTS:
        if p['id'] == project_id:
            project = p
            break
    return render_template('project_detail.html', info=PERSONAL_INFO, project=project, project_id=project_id)


@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)

#exercise 5.2
BLOG_POSTS = [
    {
        'id': 1,
        'title': 'Why I Started Learning Flask',
        'content': 'Flask is lightweight, flexible, and great for beginners.'
    },
    {
        'id': 2,
        'title': 'My Backend Journey',
        'content': 'Learning Flask after Java and Spring Boot.'
    }
]


@app.route('/blog')
def blog():
    return render_template(
        'blog.html',
        info=PERSONAL_INFO,   # REQUIRED for base.html
        posts=BLOG_POSTS      # REQUIRED for blog.html
    )


#exercise 5.4
@app.route('/skill/<skill_name>')
def skill_detail(skill_name):
    related_projects = []

    for project in PROJECTS:
        if skill_name.lower() in [t.lower() for t in project['tech']]:
            related_projects.append(project)

    return render_template(
        'skill_detail.html',
        info=PERSONAL_INFO,
        skill_name=skill_name,
        projects=related_projects
    )

if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# PROJECT STRUCTURE:
# =============================================================================
#
# part-5/
# ├── app.py              <- You are here
# ├── static/
# │   └── style.css       <- CSS styles
# └── templates/
#     ├── base.html       <- Base template (inherited by all pages)
#     ├── index.html      <- Home page
#     ├── about.html      <- About page
#     ├── projects.html   <- Projects list
#     ├── project_detail.html <- Single project view
#     └── contact.html    <- Contact page
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 5.1: Personalize your website
#   - Update PERSONAL_INFO with your real information
#   - Add your actual skills and projects
#
# Exercise 5.2: Add a new page
#   - Create a /blog route
#   - Add blog posts data structure
#   - Create blog.html template
#
# Exercise 5.3: Enhance the styling
#   - Modify static/style.css
#   - Add your own color scheme
#   - Make it responsive for mobile
#
# Exercise 5.4: Add more dynamic features
#   - Create a /skill/<skill_name> route
#   - Show projects that use that skill
#
# =============================================================================