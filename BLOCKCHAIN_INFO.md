# Antimatter_Phenomenology_Engine Blockchain Info

이 저장소의 “블록체인 서명”은 공개 블록체인 네트워크가 아니라,
루트 [SIGNATURE.sha256](/Users/jazzin/Desktop/00_BRAIN/_staging/Antimatter_Phenomenology_Engine/SIGNATURE.sha256)에 기록되는
**SHA-256 파일 매니페스트**를 뜻합니다.

목적:
- 공개 정본 파일 목록 고정
- 릴리스 검증 시 해시 무결성 확인
- 문서/코드/테스트가 같은 시점의 묶음인지 점검
- 반물질처럼 민감한 주제에서 설명 문서와 코드 판정축이 어긋나지 않도록 릴리스 시점 정본 고정

기본 절차:
1. `python3 scripts/cleanup_generated.py`
2. `python3 scripts/generate_signature.py`
3. `python3 scripts/verify_signature.py`
4. `python3 scripts/release_check.py`

주의:
- 이 매니페스트는 분산 합의나 스마트 컨트랙트를 제공하지 않습니다.
- 의미는 “릴리스 묶음의 무결성 증명”에 가깝습니다.
