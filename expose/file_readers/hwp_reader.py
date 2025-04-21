from hwp import HWP
from typing import List

class HWPReader:
    @staticmethod
    def read_file(file_path: str) -> List[str]:
        """
        한글 문서를 읽고 텍스트를 반환합니다.
        
        Args:
            file_path (str): HWP 파일 경로
            
        Returns:
            List[str]: 각 단락의 텍스트 리스트
        """
        try:
            hwp = HWP()
            hwp.open(file_path)
            paragraphs = []
            for para in hwp.paragraphs:
                if para.text.strip():
                    paragraphs.append(para.text)
            hwp.close()
            return paragraphs
        except Exception as e:
            raise Exception(f"한글 파일 읽기 오류: {str(e)}") 