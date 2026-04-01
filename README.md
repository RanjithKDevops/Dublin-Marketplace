Dublin Marketplace
A simple classifieds web application where people can post items to sell and browse what others are offering. Built with Flask, deployed to AWS EC2, with a fully automated CI/CD pipeline using GitHub Actions.

What This Project Does
Dublin Marketplace is a classifieds platform where users can:

Create new listings with title, price, description, category, email, and location

View all current listings sorted by newest first

Edit existing listings if something changes

Delete listings when items are sold

The application includes input validation to make sure users enter proper information like valid email addresses and reasonable prices. All listings are stored in a SQLite database.

Live Application
The application is running live at: http://3.236.201.10:5000

CI/CD Pipeline
This project includes a complete CI/CD pipeline built with GitHub Actions. The pipeline runs automatically on every push to the main branch and includes:

Security scanning with Bandit

Code quality checks with Pylint

Static code analysis with SonarCloud

Automated deployment to AWS EC2

When code is pushed to GitHub, the pipeline:

Sets up Python and installs dependencies

Runs Bandit to check for security vulnerabilities

Runs Pylint to evaluate code quality

Sends the code to SonarCloud for deeper analysis

Packages and deploys the application to EC2

Tools Used
Flask - Python web framework

WTForms - Form validation

SQLAlchemy - Database ORM

GitHub Actions - CI/CD automation

Bandit - Security scanning

Pylint - Code quality analysis

SonarCloud - Static code analysis

AWS EC2 - Cloud hosting

dublin-marketplace/
├── app.py              # Main Flask application
├── models.py           # Database models
├── forms.py            # Form validation
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── add_listing.html
│   ├── listing_detail.html
│   └── edit_listing.html
└── .github/
    └── workflows/
        └── ci-cd.yml   # GitHub Actions pipeline


Local Development
To run this project locally:

# Clone the repository
git clone https://github.com/RanjithKDevops/Dublin-Marketplace.git

# Navigate to the project
cd Dublin-Marketplace

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py


The application will be available at http://127.0.0.1:5000

What I Learned
Building this project taught me:

Setting up a CI/CD pipeline from scratch using GitHub Actions

Integrating security scanning with Bandit

Using code quality tools like Pylint

Deploying applications to AWS EC2

Why security and quality checks need to be part of the development process from day one

Author
Ranjith Kanna Nepolean
Student ID: 25124862
MSc in Cloud Computing
National College of Ireland
