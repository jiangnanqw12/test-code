from asposepdf import Document, TextFragmentAbsorber, FontRepository

# Load the PDF document
pdf_document = Document(r"000_TP316_Operating Systems_1.10_1707140102.pdf")

# Create a TextFragmentAbsorber object to find all text fragments
absorber = TextFragmentAbsorber()

# Accept the absorber for all pages
pdf_document.pages.accept(absorber)

# Get the text fragments
text_fragments = absorber.text_fragments

# Change the font of each fragment
for text_fragment in text_fragments:
    text_fragment.text_state.font = FontRepository.find_font("Arial")

# Save the updated document
pdf_document.save("output.pdf")
