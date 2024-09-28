from django.core.management.base import BaseCommand
from inventory.models import Item
from faker import Faker


class Command(BaseCommand):
    help = 'Create 10,000 random items'

    def handle(self, *args, **kwargs):
        fake = Faker()
        items = []

        for i in range(10000):
            item = Item(
                name=f"{fake.word()}_{i+1}",  # Combine word with an index
                description=fake.text(),
                quantity=fake.random_int(min=1, max=100),
                price=fake.random_number(digits=5) / 100  # Price with two decimal places
            )
            items.append(item)

        # Bulk create items to reduce the number of database hits
        Item.objects.bulk_create(items)

        self.stdout.write(self.style.SUCCESS('Successfully created 10,000 items.'))
