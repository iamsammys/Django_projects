#!/usr/bin/python3
"""module to implement model form for restaurant
"""

from django.forms import ModelForm
from .models import Booking


class BookingForm(ModelForm):
    """bookingform class"""
    class Meta:
        """class Meta
        
        Attributes:
            model: the model used to implement the form
            fields: fields of the model
        """
        model = Booking
        fields = "__all__"