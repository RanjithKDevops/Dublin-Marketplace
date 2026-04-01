# Dublin Marketplace

A simple classifieds web application where people can post items to sell and browse what others are offering. Built with Flask, deployed to AWS EC2, with a fully automated CI/CD pipeline using GitHub Actions.

---

## What This Project Does

- **Create** listings with title, price, description, category, email, and location
- **View** all current listings sorted by newest first
- **Edit** existing listings
- **Delete** listings when items are sold

Includes input validation for email format, price range, and required fields. All listings stored in SQLite.

---

## Live Application

🔗 [http://3.236.201.10:5000](http://3.236.201.10:5000)

---

## CI/CD Pipeline

Automated pipeline using GitHub Actions that runs on every push to `main`:

| Stage | Tool |
|-------|------|
| Security Scan | Bandit |
| Code Quality | Pylint |
| Static Analysis | SonarCloud |
| Deployment | AWS EC2 |

**Pipeline Flow:**  
Push → GitHub Actions → Bandit → Pylint → SonarCloud → Deploy to EC2

---

## Tools Used

| Tool | Purpose |
|------|---------|
| Flask | Web framework |
| WTForms | Form validation |
| SQLAlchemy | Database ORM |
| GitHub Actions | CI/CD automation |
| Bandit | Security scanning |
| Pylint | Code quality |
| SonarCloud | Static analysis |
| AWS EC2 | Cloud hosting |

---

## Project Structure

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

---

## Local Development

```bash
# Clone the repository
git clone https://github.com/RanjithKDevops/Dublin-Marketplace.git
cd Dublin-Marketplace

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

Visit http://127.0.0.1:5000 to view locally.
