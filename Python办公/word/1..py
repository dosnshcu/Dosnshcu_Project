from langchain_unstructured import UnstructuredLoader

def read_docx_content(file_path):
    try:
        # doc = Document(file_path)
        # docx_content = '\n'.join(paragraph.text for paragraph in doc.paragraphs)
        # return docx_content
        loader = UnstructuredLoader(file_path)

        # 提取文档内容并打印
        docs = loader.load()
        docx_content = ''
        for doc in docs:
            # print(doc.page_content)
            docx_content += doc.page_content + '\n'
        return docx_content
    except Exception as e:
        print(f"Error reading DOCX file {file_path}: {e}")
        raise ''  # 抛出异常，以便在主程序中处理

word_content = read_docx_content('word.docx')
print(word_content)