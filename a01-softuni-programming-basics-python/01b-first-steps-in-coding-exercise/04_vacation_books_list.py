book_pages = int(input())
book_pages_per_min = int(input())
book_days_required = int(input())

time_needed_per_book = book_pages / book_pages_per_min
time_needed_per_day = time_needed_per_book // book_days_required

print(time_needed_per_day)
