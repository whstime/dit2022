contents = ['''            <p class="text-center">print(<span style="color: orange;">'Hello World'</span>) <span style="color: red;">!=</span> print(<span style="color: orange;">'Hello'<span style="color: black;">+</span>'World'</span>)</p>
            <img class="imgPag" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Earth_Western_Hemisphere_transparent_background.png/1200px-Earth_Western_Hemisphere_transparent_background.png"></img>
''','''Hello!''']
currentPage = 0

def changePage(pgNmber):
    content = document.getElementById('paginationContent')
    console.log('DEBUG - CURRENT HTML BEING SERVED = ' + contents[pgNmber])
    content.innerHTML = contents[pgNmber]

def nextPage(*ags, **kws):
    global currentPage
    currentPage = currentPage + 1
    changePage(currentPage)
    console.log('DEBUG - CURRENT USER PAGE = ' + str(currentPage))
    if contents[currentPage] == contents[-1]:
        Element('fowardBtn').element.style.visibility = 'Hidden'
        Element('backBtn').element.style.visibility = ''
    elif contents[currentPage] != contents[-1]:
        Element('fowardBtn').element.style.visibility = ''
        Element('backBtn').element.style.visibility = 'Hidden'
    elif contents[currentPage] == contents[0]:
        Element('backBtn').element.style.visibility = 'Hidden'
        Element('fowardBtn').element.style.visibility = ''
    elif contents[currentPage] != contents[0]:
        Element('backBtn').element.style.visibility = ''
        Element('fowardBtn').element.style.visibility = 'Hidden'

def backPage(*ags, **kws):
    global currentPage
    currentPage = currentPage - 1
    changePage(currentPage)
    console.log('DEBUG - CURRENT USER PAGE = ' + str(currentPage))
    if contents[currentPage] == contents[-1]:
        Element('fowardBtn').element.style.visibility = 'Hidden'
        Element('backBtn').element.style.visibility = ''
    elif contents[currentPage] != contents[-1]:
        Element('fowardBtn').element.style.visibility = ''
        Element('backBtn').element.style.visibility = 'Hidden'
    elif contents[currentPage] == contents[0]:
        Element('backBtn').element.style.visibility = 'Hidden'
        Element('fowardBtn').element.style.visibility = ''
    elif contents[currentPage] != contents[0]:
        Element('backBtn').element.style.visibility = ''
        Element('fowardBtn').element.style.visibility = 'Hidden'