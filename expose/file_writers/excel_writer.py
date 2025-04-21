import pandas as pd
from typing import Dict, List, Any

class ExcelWriter:
    @staticmethod
    def write_file(data: Dict[str, Any], output_path: str):
        """
        데이터를 Excel 파일로 내보냅니다.
        
        Args:
            data (Dict[str, Any]): 내보낼 데이터
            output_path (str): 출력 파일 경로
        """
        try:
            # 데이터가 딕셔너리인 경우 DataFrame으로 변환
            if isinstance(data, dict):
                df = pd.DataFrame(list(data.items()), columns=['Key', 'Value'])
            # 데이터가 리스트인 경우 그대로 DataFrame으로 변환
            elif isinstance(data, list):
                df = pd.DataFrame(data)
            else:
                raise ValueError("지원하지 않는 데이터 형식입니다.")
            
            df.to_excel(output_path, index=False)
        except Exception as e:
            raise Exception(f"Excel 파일 내보내기 오류: {str(e)}") 