'''
@author: Jaime Bastida
@desc: Converter from txt to HTML
'''

def convert():
    originalFile = input('Ingrese el nombre del archivo: ')
    destFile = originalFile.replace('.txt', '.html')
    print(originalFile, destFile)

    header = '''
    <html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        <h1>{title}</h1>
    '''

    footer = '''
    </body>
    </html> 
    '''

    with open('charles.txt', 'r', encoding='utf8') as origStream:
        title = origStream.readline()
        text = origStream.read()
    
    header = header.format(title = title)
    entireHtml = ''.join([header, text, footer])

    with open(destFile, 'w', encoding='utf8') as destStream:
        destStream.write(entireHtml)

if __name__ == '__main__':
    convert()