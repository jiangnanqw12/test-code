# public key
from pylovepdf.ilovepdf import ILovePdf
public_key = 'paste your code here'

# importing the ilovepdf api

# creating a ILovePdf object
ilovepdf = ILovePdf(public_key, verify_ssl=True)

# assigning a new split task task
task = ilovepdf.new_task('split')

# adding the pdf file to the task
task.add_file('04-float.pdf')


# setting the output folder directory
# if no folder exist it will create one
task.set_output_folder('output_folder')

# execute the task
task.execute()

# download the task
task.download()

# delete the task
task.delete_current_task()
