contents = ['''            <p class="text-center paginationContent1stPageText">print(<span style="color: orange;">'Hello World'</span>) <span style="color: red;">!=</span> print(<span style="color: orange;">'Hello'<span style="color: black;">+</span>'World'</span>)</p>
            <img class="imgPag" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Earth_Western_Hemisphere_transparent_background.png/1200px-Earth_Western_Hemisphere_transparent_background.png"></img>''','''
<span class="paginationContent2ndPageText">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Amet delectus dolor odit voluptatibus, labore temporibus eveniet officia. Quas, labore ipsam. Repudiandae expedita obcaecati, eveniet officia enim qui perferendis. Dolores, consectetur.
</span>''','''<span style="font-size:200%;">L</span>''']
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
    updateBtns()

def backPage(*ags, **kws):
    global currentPage
    currentPage = currentPage - 1
    changePage(currentPage)
    console.log('DEBUG - CURRENT USER PAGE = ' + str(currentPage))
    updateBtns()

def updateBtns():
    if contents[currentPage] == contents[-1]:
        Element('fowardBtn').element.style.visibility = 'Hidden'
        Element('backBtn').element.style.visibility = ''
    elif contents[currentPage] == contents[0]:
        Element('backBtn').element.style.visibility = 'Hidden'
        Element('fowardBtn').element.style.visibility = ''
    else:
        Element('backBtn').element.style.visibility = ''
        Element('fowardBtn').element.style.visibility = ''
