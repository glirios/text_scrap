import pdfplumber

def main():
	dict = {}

	pdf = pdfplumber.open("Resume Giovanni Lirios.pdf")
	page = pdf.pages[0]

	# print(type(first_page.extract_text()))
	for word in page.extract_text().split(" "):
		print(word)

if __name__ == "__main__":
	main()