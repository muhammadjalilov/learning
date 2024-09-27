from django.core.exceptions import ValidationError


def validate_start_date_less_than_end_date(start_date, end_date):
    if start_date >= end_date:
        raise ValidationError('Start date must be earlier than the end date.')
