# Overview

## Loaders
- loaders are used to upload document data into your application
- Langchain provides its own document loaders and interfaces for using third party loaders, which allows you to
stay in the LangChain ecosystem even if a third party solution is required to interact with a specific document type
    - its **inputs** are:
        - loader: the specific loader needed for your data type
        - document: one or more documents to be loaded into your app
    - the **output** is:
        - a list of all documents loaded into the app
            - the structure of these documents will vary depending on the kind of data loaded (csv documents will be saved in a different structure than pdf documents)

# Document Loaders Lab

### Files to modify
- you will be directly modifying ```src/main/lab.py```
    - look for the "TODO" comments, which will specify the requirements for completing the lab
- DO NOT modify ```src/tests/test_lab.py```, as it contains the tests that you must pass to complete the lab
    - you can consider your lab complete when every test passes
- DO NOT modify any content in ```resources```: the documents are needed to complete the lab

### Notes and resources
- LangChain documentation on document loaders can be found [here](https://python.langchain.com/docs/modules/data_connection/document_loaders/): look through the documentation if you need more assistance