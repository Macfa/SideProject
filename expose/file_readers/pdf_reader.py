from PyPDF2 import PdfReader
from typing import List

class PDFReader:
    @staticmethod
    def read_file(file_path: str) -> List[str]:
        """
        PDF 파일을 읽고 텍스트를 반환합니다.
        
        Args:
            file_path (str): PDF 파일 경로
            
        Returns:
            List[str]: 각 페이지의 텍스트 리스트
        """
        try:
            reader = PdfReader(file_path)
            text_pages = []
            for page in reader.pages:
                text_pages.append(page.extract_text())
            return text_pages
        except Exception as e:
            raise Exception(f"PDF 파일 읽기 오류: {str(e)}") 