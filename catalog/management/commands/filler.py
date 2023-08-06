from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.objects.all().delete()

        category_list = [
            {'name_category': 'Cмартфоны', 'description_category': 'телефоны'},
            {'name_category': 'ПК и периферия', 'description_category': 'всё для пк'},
        ]

        category_create = []
        for category_item in category_list:
            category_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(category_create)
