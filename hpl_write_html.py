def writeHeader(file):
    file.write("<!DOCTYPE html>\n")
    file.write("<head>\n")
    file.write("<meta charset=\"UTF-8\">\n")
    file.write("<title>title</title>\n")
    file.write("</head>\n")

def writeBody(file , textName):
    file.write("<body>")
    title = "Analysis of " + textName
    
