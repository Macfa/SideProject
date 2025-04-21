from typing import Type
from .base_extractor import BaseExtractor
from .pdf_extractor import PDFExtractor
from .word_extractor import WordExtractor
from .hwp_extractor import HWPExtractor

class ExtractorFactory:
    @staticmethod
    def get_extractor(file_extension: str) -> Type[BaseExtractor]:
        """
        파일 확장자에 따라 적절한 추출기를 반환합니다.
        
        Args:
            file_extension (str): 파일 확장자 (예: '.pdf', '.docx', '.hwp')
            
        Returns:
            Type[BaseExtractor]: 해당 파일 형식에 맞는 추출기 클래스
            
        Raises:
            ValueError: 지원하지 않는 파일 형식인 경우
        """
        extractors = {
            '.pdf': PDFExtractor,
            '.docx': WordExtractor,
            '.hwp': HWPExtractor
        }
        
        if file_extension.lower() not in extractors:
            raise ValueError(f"지원하지 않는 파일 형식입니다: {file_extension}")
        
        return extractors[file_extension.lower()] 