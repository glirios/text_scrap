import pdfplumber
import string

def main():
	counter = {}

	pdf = pdfplumber.open("Resume Giovanni Lirios.pdf")
	page = pdf.pages[0]

	# print(type(first_page.extract_text()))
	for word in page.extract_text().split(" "):
		text = word.strip(string.punctuation + "\n")
		if text != '':
			if text in counter:
				counter[text] += 1
			else:
				counter[text] = 1

	print(counter)

if __name__ == "__main__":
	main()
