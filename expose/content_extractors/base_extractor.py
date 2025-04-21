from abc import ABC, abstractmethod
from typing import List, Dict, Any
import re
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from transformers import BertModel, BertTokenizer
import torch

class BaseExtractor(ABC):
    def __init__(self):
        # 다국어 BERT 모델 초기화
        self.model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')
        self.bert_model = BertModel.from_pretrained('klue/bert-base')
        self.tokenizer = BertTokenizer.from_pretrained('klue/bert-base')
        
        # 도메인별 전문 용어 사전
        self.domain_keywords = {
            'legal': ['제1조', '당사자', '계약기간', '의무', '권리'],
            'medical': ['투여량', '부작용', '진단코드', '처방', '증상'],
            'technical': ['사양', '구성', '설치', '운영', '관리']
        }
    
    @abstractmethod
    def preprocess_text(self, text: str) -> str:
        """문서 타입별 전처리 메서드"""
        pass
    
    def calculate_sentence_importance(self, sentence: str, position: int, total_sentences: int) -> float:
        """
        문장의 중요도를 계산합니다.
        
        Args:
            sentence (str): 분석할 문장
            position (int): 문장의 위치
            total_sentences (int): 전체 문장 수
            
        Returns:
            float: 문장 중요도 점수
        """
        # TextRank 점수
        textrank_score = self._calculate_textrank_score(sentence)
        
        # BERT 임베딩 기반 의미적 중요도
        semantic_score = self._calculate_semantic_score(sentence)
        
        # 위치 기반 가중치 (문서의 시작과 끝 부분에 더 높은 가중치)
        position_weight = self._calculate_position_weight(position, total_sentences)
        
        # 도메인 특화 점수
        domain_score = self._calculate_domain_score(sentence)
        
        # 종합 점수 계산 (가중치: TextRank 0.3, BERT 0.3, 위치 0.2, 도메인 0.2)
        total_score = (textrank_score * 0.3 + 
                      semantic_score * 0.3 + 
                      position_weight * 0.2 + 
                      domain_score * 0.2)
        
        return total_score
    
    def _calculate_textrank_score(self, sentence: str) -> float:
        """TextRank 알고리즘을 적용한 중요도 점수 계산"""
        # 구현은 기존 코드와 동일
        pass
    
    def _calculate_semantic_score(self, sentence: str) -> float:
        """BERT 기반 의미적 중요도 점수 계산"""
        inputs = self.tokenizer(sentence, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = self.bert_model(**inputs)
        
        # [CLS] 토큰의 임베딩을 문장 표현으로 사용
        sentence_embedding = outputs.last_hidden_state[:, 0, :].numpy()
        
        # 의미적 중요도 점수 계산 (예: 다른 문장들과의 평균 유사도)
        return np.mean(cosine_similarity(sentence_embedding, self.sentence_embeddings))
    
    def _calculate_position_weight(self, position: int, total: int) -> float:
        """문장 위치 기반 가중치 계산"""
        # 문서의 시작과 끝 부분에 더 높은 가중치
        normalized_position = position / total
        if normalized_position < 0.1 or normalized_position > 0.9:
            return 1.0
        elif normalized_position < 0.2 or normalized_position > 0.8:
            return 0.8
        else:
            return 0.5
    
    def _calculate_domain_score(self, sentence: str) -> float:
        """도메인 특화 점수 계산"""
        max_score = 0.0
        for domain, keywords in self.domain_keywords.items():
            score = sum(1 for keyword in keywords if keyword in sentence)
            max_score = max(max_score, score / len(keywords))
        return max_score
    
    def extract_key_sentences(self, text: str, top_n: int = 5) -> List[str]:
        """
        텍스트에서 핵심 문장을 추출합니다.
        
        Args:
            text (str): 원본 텍스트
            top_n (int): 추출할 문장 수
            
        Returns:
            List[str]: 핵심 문장 리스트
        """
        # 문장 분리
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if len(s.strip()) > 0]
        
        # 문장 임베딩 생성
        self.sentence_embeddings = self.model.encode(sentences)
        
        # 각 문장의 중요도 계산
        sentence_scores = []
        for i, sentence in enumerate(sentences):
            score = self.calculate_sentence_importance(sentence, i, len(sentences))
            sentence_scores.append((sentence, score))
        
        # 중요도 순으로 정렬
        ranked_sentences = sorted(sentence_scores, key=lambda x: x[1], reverse=True)
        return [sentence for sentence, _ in ranked_sentences[:top_n]]
    
    def extract_keywords(self, text: str, top_n: int = 10) -> Dict[str, float]:
        """
        텍스트에서 키워드를 추출합니다.
        
        Args:
            text (str): 원본 텍스트
            top_n (int): 추출할 키워드 수
            
        Returns:
            Dict[str, float]: 키워드와 중요도 점수
        """
        # 단어 분리 및 정규화
        words = re.findall(r'\w+', text.lower())
        word_freq = {}
        
        # 단어 빈도수 계산
        for word in words:
            if len(word) > 1:  # 1글자 단어 제외
                word_freq[word] = word_freq.get(word, 0) + 1
        
        # TF-IDF 스타일 점수 계산
        max_freq = max(word_freq.values())
        keywords = {word: freq/max_freq for word, freq in word_freq.items()}
        
        # 도메인 특화 키워드 가중치 적용
        for word in keywords:
            for domain_keywords in self.domain_keywords.values():
                if word in domain_keywords:
                    keywords[word] *= 1.5  # 도메인 키워드 가중치 증가
        
        # 상위 키워드 선택
        return dict(sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:top_n]) 