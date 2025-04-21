from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from typing import Dict, List, Any

class PDFWriter:
    @staticmethod
    def write_file(data: Dict[str, Any], output_path: str):
        """
        데이터를 PDF 파일로 내보냅니다.
        
        Args:
            data (Dict[str, Any]): 내보낼 데이터
            output_path (str): 출력 파일 경로
        """
        try:
            c = canvas.Canvas(output_path, pagesize=letter)
            width, height = letter
            
            # PDF에 데이터 작성
            y = height - 50  # 시작 위치
            for key, value in data.items():
                if y < 50:  # 페이지 끝에 도달하면 새 페이지 생성
                    c.showPage()
                    y = height - 50
                
                c.drawString(50, y, f"{key}: {value}")
                y -= 20
            
            c.save()
        except Exception as e:
            raise Exception(f"PDF 파일 내보내기 오류: {str(e)}") 