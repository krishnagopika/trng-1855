import unittest

from src.main.lab import load_a_pdf_file, load_a_text_file, load_csv_files_only_from_directory

class LangChainDocumentLoaderTest(unittest.TestCase):
    
    def test_load_a_text_file(self):
        doc = load_a_text_file("src/resources/lab_docs/lab_txt.txt")
        self.assertEqual(len(doc), 1)
        self.assertEqual(doc[0].page_content, "This is the text document for the lab")
        
    def test_load_a_pdf_file(self):
        doc = load_a_pdf_file("src/resources/lab_docs/lab_pdf.pdf")
        self.assertEqual(len(doc), 1)
        self.assertEqual(doc[0].page_content, "This is the pdf for the lab  ")
        
    def test_load_csv_files_only_from_directory(self):
        doc = load_csv_files_only_from_directory("src/resources/lab_docs")
        self.assertEqual(len(doc), 1)
        self.assertEqual(doc[0].page_content, "this: for\nis: the\nthe csv: lab")