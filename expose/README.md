# 문서 핵심 데이터 추출 시스템

다양한 문서 형식(PDF, Word, HWP)에서 핵심 내용을 추출하고 구조화된 형식으로 출력하는 시스템입니다.

## 현재 구현 상태

### 1. 파일 읽기 모듈
- PDF 파일 읽기 (`PDFReader`)
- Word 문서 읽기 (`WordReader`)
- 한글 문서 읽기 (`HWPReader`)

### 2. 파일 내보내기 모듈
- Excel 파일 내보내기 (`ExcelWriter`)
- PDF 파일 내보내기 (`PDFWriter`)

### 3. 핵심 내용 추출 모듈
- 기본 추출기 (`BaseExtractor`)
  - TextRank 알고리즘
  - BERT 기반 의미적 분석
  - 위치 기반 가중치
  - 도메인 특화 점수
- PDF 특화 추출기 (`PDFExtractor`)
  - 페이지 번호 제거
  - 헤더/푸터 제거
  - 표 구조 분석
- Word 특화 추출기 (`WordExtractor`)
  - 스타일 태그 처리
  - 특수 문자 정규화
  - 목차 분석
- 한글 특화 추출기 (`HWPExtractor`)
  - 한글 특수 문자 처리
  - 각주/미주 제거
  - 단락 구조 분석

### 4. 추출기 팩토리
- 파일 확장자에 따른 적절한 추출기 선택
- 확장 가능한 구조

## 남은 작업

### 1. OCR 통합
- [ ] Tesseract OCR을 활용한 스캔본 문서 처리
- [ ] 이미지 기반 텍스트 추출 최적화
- [ ] 다국어 OCR 지원

### 2. 성능 최적화
- [ ] 병렬 처리 구현
- [ ] 캐싱 시스템 도입
- [ ] 메모리 사용량 최적화

### 3. 사용자 경험 개선
- [ ] 사용자 정의 패턴 등록 기능
- [ ] 추출 결과 실시간 미리보기
- [ ] 사용자 피드백 기반 학습

### 4. 기능 확장
- [ ] 실시간 협업 기능
- [ ] 다국어 지원 강화
- [ ] 도메인 특화 모델 추가

## 향후 방향성

### 1. AI/ML 기반 고도화
- 딥러닝 모델을 활용한 더 정교한 내용 추출
- 사용자 피드백 기반 지속적 학습
- 도메인 특화 모델 개발

### 2. 확장성 강화
- 새로운 문서 형식 지원
- 클라우드 기반 확장
- 마이크로서비스 아키텍처 도입

### 3. 보안 강화
- 문서 암호화 지원
- 접근 제어 구현
- 감사 로그 시스템 구축

### 4. 통합성 향상
- API 서비스 제공
- 다양한 플랫폼 연동
- 표준 형식 지원 확대

## 설치 및 사용 방법

1. 의존성 설치:
```bash
pip install -r requirements.txt
```

2. 기본 사용 예시:
```python
from document_processor import DocumentProcessor

processor = DocumentProcessor()
extracted_data = processor.process_file("input.pdf")
processor.export_file(extracted_data, "output.xlsx")
```

## 라이선스
MIT License

## 기여 방법
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request 