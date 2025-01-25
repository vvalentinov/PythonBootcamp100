def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            # Error: Not 4000, but 400
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False