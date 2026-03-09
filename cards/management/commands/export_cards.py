from django.core.management.base import BaseCommand
from cards.models import Card
import csv


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        cards = Card.objects.all()

        with open("cards.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "card_number",
                "phone",
                "status",
                "expire",
                "balance"
            ])

            for card in cards:
                writer.writerow([
                    card.card_number,
                    card.phone,
                    card.status,
                    card.expire,
                    card.balance
                ])

