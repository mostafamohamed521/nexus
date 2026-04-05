"""
Management command: python manage.py seed_data
Seeds the database with demo content for development.
"""
from django.core.management.base import BaseCommand
from services_app.models import Service, Testimonial, TeamMember
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Seeds the database with demo data'

    def handle(self, *args, **kwargs):
        self.seed_services()
        self.seed_testimonials()
        self.seed_team()
        self.stdout.write(self.style.SUCCESS('✅ Database seeded successfully!'))

    def seed_services(self):
        services = [
            ('Product Strategy', 'rocket', 'We craft data-driven strategies that align product vision with business goals.', True, 2499),
            ('UI/UX Design', 'eye', 'Human-centered design that converts visitors into loyal customers.', True, 1999),
            ('Backend Engineering', 'code', 'Scalable, secure APIs and systems built to handle millions of requests.', True, 3499),
            ('Cloud & DevOps', 'cloud', 'CI/CD pipelines, container orchestration, and zero-downtime deployments.', True, 2999),
            ('Security Audit', 'shield', 'End-to-end penetration testing and compliance for enterprise standards.', False, 1499),
            ('Analytics & BI', 'chart', 'Turn raw data into actionable insights with live dashboards.', True, 1799),
        ]
        for title, icon, desc, featured, price in services:
            Service.objects.get_or_create(
                slug=slugify(title),
                defaults=dict(title=title, icon=icon, short_description=desc,
                              description=desc + ' Our team of experts will work closely with you to deliver exceptional results.',
                              is_featured=featured, price=price)
            )
        self.stdout.write('  → Services seeded')

    def seed_testimonials(self):
        testimonials = [
            ('Sarah Chen', 'CTO', 'Meridian Labs', 'Nexus transformed our entire product architecture. Delivery was on time, on budget, and exceeded every expectation.', 5),
            ('Marcus Rivera', 'Founder', 'Volta Systems', 'The engineering team is world-class. Our platform now handles 10× the traffic with half the infrastructure cost.', 5),
            ('Aisha Patel', 'VP Product', 'Clearwave', 'From strategy to launch in 8 weeks. Absolutely exceptional work across design and engineering.', 5),
            ('Tom Bergman', 'CEO', 'Stackr Inc', 'We\'ve worked with many agencies. Nexus is the first that genuinely acts like a partner, not a vendor.', 5),
        ]
        for name, title, company, content, rating in testimonials:
            Testimonial.objects.get_or_create(
                name=name, company=company,
                defaults=dict(job_title=title, content=content, rating=rating)
            )
        self.stdout.write('  → Testimonials seeded')

    def seed_team(self):
        team = [
            ('Alex Morgan', 'Chief Executive Officer', 'Visionary leader with 15 years in enterprise software.', 0),
            ('Priya Nakamura', 'Head of Design', 'Former lead designer at Stripe and Figma.', 1),
            ('Jordan Ellis', 'Lead Engineer', 'Distributed systems expert, ex-Google SRE.', 2),
            ('Camille Dubois', 'Product Director', 'Shipped products used by 50M+ users globally.', 3),
        ]
        for name, role, bio, order in team:
            TeamMember.objects.get_or_create(name=name, defaults=dict(role=role, bio=bio, order=order))
        self.stdout.write('  → Team seeded')
