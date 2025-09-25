'''
sample_pac/ab/__init__.py
ab 패키지를 import 할 때 자동실행되는 파일입니다.
from sample_pac.ab import *을 수행시 a모듈만 자동 import되도록 하기위해 
__all__를 셋팅
'''
__all__ = ['a']

print("sample_pac.ab 패키지 로드")

