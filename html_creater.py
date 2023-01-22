from user_interface import phonebook_view

def create(device = 1):
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head><head>\n <body>\n'
    html += '  <p {}> Phonebook: {} c</p>\n'\
        .format(style, phonebook_view(device))
    html += ' </body>\n</html>'
    
    with open('index.html', 'w') as page:
        page.write(html)
        
    return html    
    