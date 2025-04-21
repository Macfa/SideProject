import os
from typing import List, Dict, Any
import pandas as pd
from file_readers.pdf_reader import PDFReader
from file_readers.word_reader import WordReader
from file_readers.hwp_reader import HWPReader
from file_writers.excel_writer import ExcelWriter
from file_writers.pdf_writer import PDFWriter
from content_extractors.extractor_factory import ExtractorFactory

class DocumentProcessor:
    def __init__(self):
        self.readers = {
            '.pdf': PDFReader,
            '.docx': WordReader,
            '.hwp': HWPReader
        }
        self.writers = {
            '.xlsx': ExcelWriter,
            '.pdf': PDFWriter
        }
    
    def process_file(self, file_path: str) -> Dict[str, Any]:
        """
        파일을 처리하고 핵심 내용을 추출합니다.
        
        Args:
            file_path (str): 처리할 파일 경로
            
        Returns:
            Dict[str, Any]: 추출된 핵심 내용
        """
        file_ext = os.path.splitext(file_path)[1].lower()
        
        if file_ext not in self.readers:
            raise ValueError(f"지원하지 않는 파일 형식입니다: {file_ext}")
        
        # 파일 읽기
        reader = self.readers[file_ext]
        text_list = reader.read_file(file_path)
        
        # 추출기 선택 및 초기화
        extractor_class = ExtractorFactory.get_extractor(file_ext)
        extractor = extractor_class()
        
        # 텍스트 전처리 및 구조 추출
        processed_text = '\n'.join(text_list)
        processed_text = extractor.preprocess_text(processed_text)
        structure = extractor.extract_structure(processed_text)
        
        # 핵심 문장 및 키워드 추출
        key_sentences = extractor.extract_key_sentences(processed_text)
        keywords = extractor.extract_keywords(processed_text)
        
        return {
            'structure': structure,
            'key_sentences': key_sentences,
            'keywords': keywords
        }
    
    def export_file(self, data: Dict[str, Any], output_path: str):
        """
        데이터를 지정된 형식의 파일로 내보냅니다.
        
        Args:
            data (Dict[str, Any]): 내보낼 데이터
            output_path (str): 출력 파일 경로
        """
        file_ext = os.path.splitext(output_path)[1].lower()
        
        if file_ext not in self.writers:
            raise ValueError(f"지원하지 않는 출력 파일 형식입니다: {file_ext}")
        
        writer = self.writers[file_ext]
        writer.write_file(data, output_path)

def main():
    processor = DocumentProcessor()
    
    # 예시 사용법
    input_file = "example.pdf"  # 처리할 파일 경로
    output_excel = "keywords.xlsx"  # Excel 출력 파일 경로
    output_pdf = "keywords.pdf"  # PDF 출력 파일 경로
    
    try:
        # 파일 읽기 및 핵심 내용 추출
        extracted_data = processor.process_file(input_file)
        
        # Excel로 내보내기
        processor.export_file(extracted_data, output_excel)
        print(f"Excel 파일이 {output_excel}에 저장되었습니다.")
        
        # PDF로 내보내기
        processor.export_file(extracted_data, output_pdf)
        print(f"PDF 파일이 {output_pdf}에 저장되었습니다.")
        
    except Exception as e:
        print(f"오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    main() 