from typing import List, Dict, Any
import re
from .base_extractor import BaseExtractor

class WordExtractor(BaseExtractor):
    def preprocess_text(self, text: str) -> str:
        """
        Word 문서 텍스트 전처리
        - 스타일 태그 제거
        - 특수 문자 정규화
        - 표 내용 처리
        """
        # 스타일 태그 제거
        text = re.sub(r'<[^>]+>', '', text)
        
        # 특수 문자 정규화
        text = re.sub(r'[\u200b-\u200f\u202a-\u202e]', '', text)  # 제어 문자 제거
        text = re.sub(r'[\u2018\u2019]', "'", text)  # 스마트 따옴표 정규화
        text = re.sub(r'[\u201c\u201d]', '"', text)  # 스마트 따옴표 정규화
        
        # 표 내용 처리 (표 셀 구분자 정규화)
        text = re.sub(r'\|\s*', ' | ', text)
        text = re.sub(r'\s*\|\s*', ' | ', text)
        
        return text.strip()
    
    def extract_structure(self, text: str) -> Dict[str, Any]:
        """
        Word 문서의 구조를 추출합니다.
        - 스타일 기반 제목 식별
        - 표 내용 추출
        - 목차 식별
        """
        structure = {
            'headings': [],
            'tables': [],
            'toc': [],
            'content': []
        }
        
        lines = text.split('\n')
        current_content = []
        
        for line in lines:
            # 제목 패턴 (숫자로 시작하는 경우)
            if re.match(r'^\d+\.\s+', line):
                if current_content:
                    structure['content'].append('\n'.join(current_content))
                    current_content = []
                structure['headings'].append(line.strip())
            
            # 목차 패턴 (점선이나 탭으로 구분된 경우)
            elif re.match(r'.*\.{3,}\s*\d+$', line) or '\t' in line:
                structure['toc'].append(line.strip())
            
            # 표 내용 (|로 구분된 경우)
            elif '|' in line:
                structure['tables'].append(line.strip())
            
            # 일반 텍스트
            else:
                current_content.append(line)
        
        if current_content:
            structure['content'].append('\n'.join(current_content))
        
        return structure 