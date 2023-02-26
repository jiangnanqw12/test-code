# importing the ilovepdf api
from pylovepdf.ilovepdf import ILovePdf

# public key
public_key = 'paste_your_public_key_here'

# creating a ILovePdf object
ilovepdf = ILovePdf(public_key, verify_ssl=True)

# assigning a new compress task
task = ilovepdf.new_task('compress')

# adding the pdf file to the task
task.add_file('my_pdf.pdf')

# setting the output folder directory
# if no folder exist it will create one
task.set_output_folder('output_folder')

# execute the task
task.execute()

# download the task
task.download()

# delete the task
task.delete_current_task()
