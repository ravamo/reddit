import csv


def load (a,b):
    with open('/tmp/text.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows([a,b])
    quit()