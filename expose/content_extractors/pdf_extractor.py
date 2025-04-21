from typing import List, Dict, Any
import re
from .base_extractor import BaseExtractor

class PDFExtractor(BaseExtractor):
    def preprocess_text(self, text: str) -> str:
        """
        PDF 텍스트 전처리
        - 페이지 번호 제거
        - 헤더/푸터 제거
        - 불필요한 공백 정규화
        """
        # 페이지 번호 패턴 제거 (예: "1", "Page 1", "1/10" 등)
        text = re.sub(r'(?m)^\s*\d+\s*$', '', text)
        text = re.sub(r'(?m)^\s*Page\s+\d+\s*$', '', text)
        text = re.sub(r'(?m)^\s*\d+\s*/\s*\d+\s*$', '', text)
        
        # 헤더/푸터 패턴 제거 (반복되는 텍스트)
        lines = text.split('\n')
        header_footer = set()
        for line in lines:
            if lines.count(line) > 1:
                header_footer.add(line)
        
        cleaned_lines = [line for line in lines if line not in header_footer]
        text = '\n'.join(cleaned_lines)
        
        # 공백 정규화
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    def extract_structure(self, text: str) -> Dict[str, Any]:
        """
        PDF 문서의 구조를 추출합니다.
        - 제목, 부제목, 본문 구분
        - 목록 항목 식별
        """
        structure = {
            'titles': [],
            'sections': [],
            'lists': []
        }
        
        lines = text.split('\n')
        current_section = []
        
        for line in lines:
            # 제목 패턴 (대문자로 시작하고 짧은 문장)
            if re.match(r'^[A-Z][a-z]*\s*[A-Za-z]*$', line.strip()):
                if current_section:
                    structure['sections'].append('\n'.join(current_section))
                    current_section = []
                structure['titles'].append(line.strip())
            
            # 목록 항목 패턴
            elif re.match(r'^\s*[-•*]\s+', line) or re.match(r'^\s*\d+\.\s+', line):
                structure['lists'].append(line.strip())
            
            # 일반 텍스트
            else:
                current_section.append(line)
        
        if current_section:
            structure['sections'].append('\n'.join(current_section))
        
        return structure 