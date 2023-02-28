import re


class Regex:

    def __init__(self):
        pass


    @staticmethod
    def convert_to_date(iso_date):
        match = re.match(r"^PT(\d+H)?(\d+M)?(\d+S)?$", iso_date)
        if match:
            hours = int(match.group(1)[:-1]) if match.group(1) else 0
            minutes = int(match.group(2)[:-1]) if match.group(2) else 0
            seconds = int(match.group(3)[:-1]) if match.group(3) else 0
        total_seconds = hours * 3600 + minutes * 60 + seconds

        # Output the duration in seconds
        return total_seconds