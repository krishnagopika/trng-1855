import unittest
from chromadb.api.models.Collection import Collection
from src.main.app import (
    get_chromadb_collection,
    get_embeddings_from_csv,
    read_file_from_folder,
    get_collection_query
)


class ChromaDBTests(unittest.TestCase):
    
    def test_get_embeddings_from_csv(self):
        file_data = read_file_from_folder("./resources/menu_items.csv")
        documents, metadatas, ids = get_embeddings_from_csv(file_data)
        self.assertEqual(len(documents), 201)
        self.assertEqual(len(metadatas), 201)
        self.assertEqual(len(ids), 201)
    
    def test_get_chromadb_collection(self):
        file_data = read_file_from_folder("./resources/menu_items.csv")
        documents, metadatas, ids = get_embeddings_from_csv(file_data)
        collection = get_chromadb_collection(documents, metadatas, ids)
        self.assertIsInstance(collection, Collection, "collection variable should be a ChromaDB Collection")
        self.assertIsNotNone(collection.get("semantic-lab"), "semantic-lab not found")
        
    def test_get_collection_query(self):
        file_data = read_file_from_folder("./resources/menu_items.csv")
        documents, metadatas, ids = get_embeddings_from_csv(file_data)
        collection = get_chromadb_collection(documents, metadatas, ids)
        results = get_collection_query("rice")
        self.assertEqual(len(results["documents"][0]), 5)
        for doc in results["documents"][0]:
            is_rice = "rice" in doc.lower()
            self.assertTrue(is_rice)

if __name__ == "__main__":
    unittest.main()
