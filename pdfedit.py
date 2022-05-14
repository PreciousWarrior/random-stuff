import pypdf2

file_object = open("pdftoedit.pdf", "rb")
reader = pypdf2.PdfFileReader(file_object, strict=False)
writer = pypdf2.PdfFileWriter()

months = {"January":31, "February":28, "March":31, "April":30, "May":31, "June":30, "July":31, "August":31, "September":30, "October":31,
"November":30, "December":31}

for page in range(reader.numPages):
    writer.addPage(reader.getPage(page))


saved_month = ""
saved_month_counter = 1

parent = None
for destination_page in range(0, 365):
    i=0
    for month in months:
        i+=months[month]
        if i>=destination_page+1:
            if month!=saved_month:
                parent = writer.addBookmark(month, i)
                saved_month_counter = 1
                saved_month = month
            else:
                saved_month_counter += 1
            break
    writer.addBookmark(str(saved_month_counter), destination_page, parent)

newFile = open("saved.pdf", "wb")
writer.write(newFile)

