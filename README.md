> **한국어 (정본).** English: [README_EN.md](README_EN.md)

# Antimatter_Phenomenology_Engine v0.3.0

**반물질 전반을 다루기 위한 기초 레이어이되, 출발점은 여전히 phenomenology와 engineering screening**

**우산 허브(층위·통합 API):** [_staging/Antimatter_Foundation/README.md](../Antimatter_Foundation/README.md) — `layer_manifest()`, `run_unified_antimatter_stack()`.

## 이번 버전의 목표

이 패키지는 “반물질의 모든 것”을 완성하는 최종 엔진은 아닙니다.
대신 반물질 문제를 최소한 아래 5개 층으로 분해해
다른 엔진이나 연구 시나리오가 그 위에 올라갈 수 있게 하는
**기초 레이어**를 만듭니다.

1. `rarity` — 왜 우주에서 반물질이 희귀한가
2. `confinement / transport` — trap 안에서 어떻게 보관·이동할 수 있는가
3. `asymmetry` — 왜 물질이 더 많이 남았는가
4. `energetics` — 소멸 에너지 밀도는 어느 정도인가
5. `screening` — 뉴스/주장/서사를 어떤 층위로 읽을 것인가

최근 언론의 **저장된 반물질 샘플 이동·운반**(트랩 간 이송 등)은 **가속기·초고진공·자기 포획** 같은 **실험실 조건**에서의 성과에 가깝다.  
이 패키지는 **천문·레이더로 반물질을 잡아 추적**하는 소프트웨어가 **아니다**.

대신 다음을 **구조화**한다.

- **왜 우주에서 반물질이 극히 적은가** — 소멸(annihilation), **바리온 비대칭(미해결)**, 실험실 생산·저장 비용
- **차폐·운반의 물리 직관** — 자기장·회전반경·평균자유행정의 **차수 추정**
- **trap transport feasibility** — 반물질을 실제로 움직일 때 필요한 UHV·극저온·자기장·진동 여유
- **asymmetry 접근 프레임** — 관측된 `η_B`와 Sakharov 조건 proxy를 분리해서 보기
- **서사/에이전트용 Claim 스크리닝** — “대기 중 매크로 반물질” 같은 주장의 **서술 계층** 분류 (진리 판정 아님)

## 핵심 정체성 (00_BRAIN 정렬)

| 이 엔진이 하는 일 | 하지 않는 일 |
|------------------|----------------|
| 교육·설계·스토리보드용 **현상 분해** | 실제 검출기 DAQ·트래킹 대체 |
| 미해결 문제(바리온 생성 등) **질문 목록** | 새 물리 법칙 단정 |
| JSON/에이전트 **claim 구조**에 대한 Ω형 완성도 | “외계 반물질 함선” 입증 |

## 모듈

| 모듈 | 역할 |
|------|------|
| `rarity.py` | `why_antimatter_is_rare_axes()`, `baryon_asymmetry_open_questions()` |
| `transport.py` | `mean_free_path_in_matter_m`, `confinement_length_scale_m`, `assess_trap_transport()` |
| `asymmetry.py` | `observed_baryon_to_photon_ratio()`, `sakharov_viability_score()`, `assess_asymmetry_model()` |
| `energetics.py` | `annihilation_energy_j()`, `assess_annihilation_energy()` |
| `contracts.py` | foundation-level 공통 계약 (`Inventory`, `ConfinementContext`, `AsymmetryContext`) |
| `foundation.py` | `assess_antimatter_foundation()` — 희소성/이동/비대칭/에너지를 한 번에 요약 |
| `screening.py` | `screen_claim()`, `payload_from_news_style_summary()` |
| `constants.py` | SI 상수 (차수용) |

## 빠른 실행

```bash
cd _staging/Antimatter_Phenomenology_Engine
python -m pip install -e ".[dev]"
python -m pytest tests/ -q
```

```python
from antimatter_phenomenology import (
    AntimatterAsymmetryContext,
    AntimatterConfinementContext,
    AntimatterInventory,
    SakharovProxyInputs,
    assess_antimatter_foundation,
    TrapTransportScenario,
    assess_asymmetry_model,
    assess_trap_transport,
    screen_claim,
    why_antimatter_is_rare_axes,
)
from antimatter_phenomenology.screening import payload_from_news_style_summary

for ax in why_antimatter_is_rare_axes():
    print(ax.name, "—", ax.summary)

r = screen_claim(payload_from_news_style_summary(moved_trapped_sample=True))
print(r.tier, r.notes)

transport = assess_trap_transport(
    TrapTransportScenario(
        particle_count=92,
        magnetic_field_t=1.2,
        vacuum_pa=5e-10,
        cryogenic_temperature_k=6.0,
        peak_acceleration_ms2=1.5,
        transfer_time_s=1200.0,
    )
)
print(transport.confinement_score_0_1)

asym = assess_asymmetry_model(
    SakharovProxyInputs(
        cp_violation_strength_0_1=0.6,
        baryon_violation_strength_0_1=0.7,
        out_of_equilibrium_strength_0_1=0.8,
        model_eta_b=6.0e-10,
    )
)
print(asym.sakharov_score_0_1, asym.eta_alignment_ratio_0_1)

foundation = assess_antimatter_foundation(
    inventory=AntimatterInventory(
        antiparticle_count=92,
        estimated_mass_kg=1.5e-25,
        species="antiproton",
    ),
    confinement=AntimatterConfinementContext(
        magnetic_field_t=1.2,
        vacuum_pa=5e-10,
        cryogenic_temperature_k=6.0,
        peak_acceleration_ms2=1.5,
        transfer_time_s=1200.0,
    ),
    asymmetry=AntimatterAsymmetryContext(
        cp_violation_strength_0_1=0.6,
        baryon_violation_strength_0_1=0.7,
        out_of_equilibrium_strength_0_1=0.8,
        model_eta_b=6.0e-10,
    ),
)
print(foundation.omega_foundation_0_1, foundation.summary)
```

## 이번 확장 핵심

### 1. 반물질 이동은 무엇이 성공한 것인가

이 엔진은 “반물질이 자유공간에서 쉽게 이동했다”가 아니라,
**trap 안의 극소량 반입자를 실험실 조건에서 안전하게 운반할 수 있었는가**를 봅니다.

즉 핵심은:
- ultra-high vacuum
- cryogenic temperature
- magnetic confinement
- low mechanical shock

입니다.

### 2. 왜 반물질이 극히 적은가

이 엔진은 답을 단정하지 않고, 최소한 아래 3개를 분리합니다.

1. **annihilation**
2. **cosmological asymmetry**
3. **laboratory scale / production cost**

그리고 비대칭 문제는 `η_B`와 Sakharov 조건 proxy로 구조화합니다.

### 3. 다루는 수식

- 평균자유행정: `λ ≈ 1 / (nσ)`
- 비상대론적 gyroradius: `r = m v_perp / (|q| B)`
- baryon asymmetry observed scale: `η_B ≈ 6.1 × 10^-10`
- 소멸 에너지: `E = (m_antimatter + m_matter)c^2`

여기서 중요한 점은:
이 수식들은 **정밀 입자 수송 시뮬레이터**가 아니라,
`order-of-magnitude screening`과 `engineering intuition`용입니다.

## “반물질이 극히 미량인 이유” (엔진이 담는 답의 뼈대)

1. **접촉 소멸** — 통상 물질과 만나면 광자 등으로 바뀌며, 거시적 덩어리는 **진공·자기 포획** 없이 유지되기 어렵다.  
2. **우주론적 비대칭** — 관측 우주는 **바리온 과잉**; 초기 우주에서 그 비율(η_B)을 만든 **동역학 메커니즘은 아직 열린 문제**(표준모형만으로는 불충분한 부분이 논의됨).  
3. **실험 규모** — 가속기에서 만들고 트랩에 담는 **극소량**이 현재 기술의 현실.

## 버전·의존성

- Python **3.10+**, 런타임 **표준 라이브러리만**

## 라이선스

MIT

---

*관측·스크리닝·서사 정렬용 — 실험실 안전·입자물리 판정을 대체하지 않는다.*
