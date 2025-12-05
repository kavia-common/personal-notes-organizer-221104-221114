from django.core.management.base import BaseCommand
from api.models import Note


class Command(BaseCommand):
    help = "Seeds the database with sample notes"

    def handle(self, *args, **options):
        samples = [
            {"title": "Welcome to Notes", "content": "This is your first note!"},
            {"title": "Ocean Professional Theme", "content": "Blue primary, amber accents."},
            {"title": "Next Steps", "content": "Edit, create, and delete notes."},
        ]
        created = 0
        for s in samples:
            obj, was_created = Note.objects.get_or_create(title=s["title"], defaults={"content": s["content"]})
            created += 1 if was_created else 0
        self.stdout.write(self.style.SUCCESS(f"Seeded {created} new notes."))
