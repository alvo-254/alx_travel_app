from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        sample_data = [
            {
                "title": "Ocean View Apartment",
                "description": "A beautiful apartment overlooking the ocean.",
                "location": "Mombasa, Kenya",
                "price_per_night": 150.00,
                "available": True,
            },
            {
                "title": "Mountain Cabin",
                "description": "A cozy cabin in the mountains, perfect for hiking trips.",
                "location": "Mount Kenya, Kenya",
                "price_per_night": 95.00,
                "available": True,
            },
            {
                "title": "City Center Studio",
                "description": "Modern studio apartment in the heart of Nairobi.",
                "location": "Nairobi, Kenya",
                "price_per_night": 120.00,
                "available": False,
            },
        ]

        # Clear previous data
        Listing.objects.all().delete()

        for item in sample_data:
            listing = Listing.objects.create(
                title=item["title"],
                description=item["description"],
                location=item["location"],
                price_per_night=item["price_per_night"],
                available=item["available"],
            )
            self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
