from typing import List, Dict
import re

class KeywordExtractor:
    @staticmethod
    def extract_keywords(text_list: List[str]) -> Dict[str, int]:
        """
        텍스트에서 키워드를 추출합니다.
        
        Args:
            text_list (List[str]): 추출할 텍스트 리스트
            
        Returns:
            Dict[str, int]: 키워드와 빈도수
        """
        # 여기에 실제 키워드 추출 로직을 구현할 수 있습니다
        # 예: NLP 라이브러리 사용, 정규식 패턴 매칭 등
        keywords = {}
        
        # 예시: 단순 단어 빈도수 계산
        for text in text_list:
            words = re.findall(r'\w+', text.lower())
            for word in words:
                if len(word) > 2:  # 2글자 이상의 단어만 고려
                    keywords[word] = keywords.get(word, 0) + 1
        
        return keywords 