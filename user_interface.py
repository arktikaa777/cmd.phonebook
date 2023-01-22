import data_provider as prov
import logger as log

def phonebook_view():
    data = prov.get_phonebook()
    log.phonebook_logger(data)
    return data