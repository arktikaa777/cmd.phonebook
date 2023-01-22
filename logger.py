from datetime import datetime as dt

def phonebook_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; phonebook;{}\n'
                   .format(time, data))