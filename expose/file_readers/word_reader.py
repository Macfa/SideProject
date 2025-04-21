from docx import Document
from typing import List

class WordReader:
    @staticmethod
    def read_file(file_path: str) -> List[str]:
        """
        Word 문서를 읽고 텍스트를 반환합니다.
        
        Args:
            file_path (str): Word 파일 경로
            
        Returns:
            List[str]: 각 단락의 텍스트 리스트
        """
        try:
            doc = Document(file_path)
            paragraphs = []
            for para in doc.paragraphs:
                if para.text.strip():
                    paragraphs.append(para.text)
            return paragraphs
        except Exception as e:
            raise Exception(f"Word 파일 읽기 오류: {str(e)}") 