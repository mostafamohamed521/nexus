# NEXUS — Production Django Web Application

A complete, professional full-stack web app built with Django.

---

## 🗂 Project Structure

```
nexus_project/
├── core/                    # Django project config
│   ├── settings.py          # Settings (all environments)
│   ├── urls.py              # Root URL config
│   └── wsgi.py              # WSGI entry point
│
├── accounts/                # Auth + user management
│   ├── models.py            # CustomUser model
│   ├── forms.py             # Register / Login / Profile forms
│   ├── views.py             # Auth views + dashboard
│   ├── urls.py
│   └── admin.py
│
├── pages/                   # Static pages (Home, About)
│   ├── views.py
│   └── urls.py
│
├── services_app/            # Services & testimonials
│   ├── models.py            # Service, Testimonial, TeamMember
│   ├── views.py
│   ├── admin.py
│   └── management/
│       └── commands/
│           └── seed_data.py # Demo data seeder
│
├── contacts/                # Contact form submissions
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── admin.py
│
├── templates/               # All HTML templates
│   ├── base.html            # Master layout with nav + footer
│   ├── pages/
│   │   ├── home.html
│   │   └── about.html
│   ├── accounts/
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   └── profile.html
│   ├── services_app/
│   │   ├── list.html
│   │   └── detail.html
│   ├── contacts/
│   │   └── contact.html
│   └── errors/
│       ├── 404.html
│       └── 500.html
│
├── static/
│   ├── css/
│   │   ├── design-tokens.css   # CSS custom properties (design system)
│   │   ├── base.css            # Reset, typography, utilities, components
│   │   ├── nav.css             # Navigation
│   │   └── pages.css           # Page-specific styles
│   └── js/
│       └── main.js             # Nav scroll, animations, form UX
│
├── requirements.txt
├── .env.example
├── .gitignore
├── Procfile                 # Heroku/Railway deploy
└── README.md
```

---

## 🚀 Local Setup

### 1. Clone and enter the project
```bash
git clone <your-repo>
cd nexus_project
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply database migrations
```bash
python manage.py migrate
```

### 5. Seed demo data
```bash
python manage.py seed_data
```

### 6. Create a superuser (admin panel)
```bash
python manage.py createsuperuser
```
Or use the seeded admin:
- **Email:** `admin@nexus.io`
- **Password:** `Admin1234!`

### 7. Run the development server
```bash
python manage.py runserver
```
Open: **http://127.0.0.1:8000**

---

## 🌐 Pages

| URL | Description |
|-----|-------------|
| `/` | Home — hero, services, testimonials, CTA |
| `/about/` | About — mission, team, stats |
| `/services/` | Services list |
| `/services/<slug>/` | Service detail |
| `/contact/` | Contact form |
| `/accounts/register/` | Registration |
| `/accounts/login/` | Login |
| `/accounts/dashboard/` | User dashboard (auth required) |
| `/accounts/profile/` | Profile editor (auth required) |
| `/admin/` | Django admin panel |

---

## 🏗 Production Deployment

### Option A — Railway (Recommended, free tier)
```bash
railway login
railway init
railway up
```
Set env vars in Railway dashboard from `.env.example`.

### Option B — Heroku
```bash
heroku create your-app-name
heroku config:set SECRET_KEY="..." DEBUG=False ALLOWED_HOSTS="your-app.herokuapp.com"
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py seed_data
```

### Option C — VPS (Ubuntu/Nginx/Gunicorn)
1. Install Python, nginx, pip
2. Clone repo, create venv, install deps
3. Configure gunicorn as systemd service
4. Configure nginx as reverse proxy
5. Set up SSL with Let's Encrypt (certbot)

### Production checklist
- [ ] Set `SECRET_KEY` to a long random value (50+ chars)
- [ ] Set `DEBUG=False`
- [ ] Set `ALLOWED_HOSTS` to your domain(s)
- [ ] Add `whitenoise` to MIDDLEWARE for static files
- [ ] Run `python manage.py collectstatic`
- [ ] Switch to PostgreSQL (add `psycopg2-binary`, `dj-database-url`)
- [ ] Configure email SMTP (not console backend)
- [ ] Enable HTTPS (SECURE_SSL_REDIRECT, HSTS)

---

## 🔐 Security

- CSRF protection on all forms (Django middleware)
- Login required decorator on dashboard/profile
- Custom user model with email-as-username
- Password validation (length, commonality, similarity)
- Form-level and model-level validation
- IP address logging on contact submissions

---

## 📄 License
MIT
