from typing import List, Dict, Any
import re
from .base_extractor import BaseExtractor

class HWPExtractor(BaseExtractor):
    def preprocess_text(self, text: str) -> str:
        """
        한글 문서 텍스트 전처리
        - 한글 특수 문자 처리
        - 표 내용 정규화
        - 각주/미주 제거
        """
        # 한글 특수 문자 처리
        text = re.sub(r'[\u1100-\u11FF\u3130-\u318F\uA960-\uA97F\uD7B0-\uD7FF]', '', text)  # 한글 자모 제거
        text = re.sub(r'[\uFF00-\uFFEF]', '', text)  # 반각 문자 제거
        
        # 각주/미주 패턴 제거
        text = re.sub(r'\[각주\d+\].*?\[/각주\]', '', text)
        text = re.sub(r'\[미주\d+\].*?\[/미주\]', '', text)
        
        # 표 내용 정규화
        text = re.sub(r'┌[─┬┐]+┐', '', text)  # 표 상단 테두리 제거
        text = re.sub(r'├[─┼┤]+┤', '', text)  # 표 중간 테두리 제거
        text = re.sub(r'└[─┴┘]+┘', '', text)  # 표 하단 테두리 제거
        text = re.sub(r'│', '|', text)  # 세로선 정규화
        
        return text.strip()
    
    def extract_structure(self, text: str) -> Dict[str, Any]:
        """
        한글 문서의 구조를 추출합니다.
        - 한글 스타일 기반 제목 식별
        - 표 내용 추출
        - 단락 구조 분석
        """
        structure = {
            'headings': [],
            'tables': [],
            'paragraphs': [],
            'content': []
        }
        
        lines = text.split('\n')
        current_paragraph = []
        
        for line in lines:
            # 제목 패턴 (한글 제목 스타일)
            if re.match(r'^[가-힣]+\s*[0-9]*\.?\s*$', line.strip()):
                if current_paragraph:
                    structure['paragraphs'].append('\n'.join(current_paragraph))
                    current_paragraph = []
                structure['headings'].append(line.strip())
            
            # 표 내용 (|로 구분된 경우)
            elif '|' in line:
                structure['tables'].append(line.strip())
            
            # 단락 구분 (빈 줄)
            elif not line.strip():
                if current_paragraph:
                    structure['paragraphs'].append('\n'.join(current_paragraph))
                    current_paragraph = []
            
            # 일반 텍스트
            else:
                current_paragraph.append(line)
        
        if current_paragraph:
            structure['paragraphs'].append('\n'.join(current_paragraph))
        
        # 내용 추출 (단락을 문장 단위로 분리)
        for para in structure['paragraphs']:
            sentences = re.split(r'[.!?]+', para)
            structure['content'].extend([s.strip() for s in sentences if s.strip()])
        
        return structure 