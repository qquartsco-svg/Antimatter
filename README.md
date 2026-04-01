> **한국어 (정본).** English: [README_EN.md](README_EN.md)

# Antimatter_Phenomenology_Engine v0.3.1

**반물질 전반을 다루기 위한 기초 레이어이되, 출발점은 여전히 phenomenology와 engineering screening**

**우산 허브(층위·통합 API):** [_staging/Antimatter_Foundation/README.md](../Antimatter_Foundation/README.md) — `layer_manifest()`, `run_unified_antimatter_stack()`.

## 한눈에 보기

이 저장소는 “반물질을 발견하는 장비”가 아닙니다.
대신 다음 질문들을 **보수적으로 구조화**하는 기초 레이어입니다.

- 반물질이란 정확히 무엇인가
- 왜 우주는 물질이 훨씬 많아 보이는가
- 실험실에서 반물질을 어떻게 가두고 옮길 수 있는가
- 반물질 관련 뉴스나 주장 중 무엇이 실험실 현실과 맞고, 무엇이 과장인가
- 앞으로 어떤 공학 엔진과 어떤 물리 엔진으로 확장할 수 있는가

즉 이 엔진의 역할은 “반물질을 크게 주장”하는 것이 아니라,
**반물질처럼 예민한 주제를 물리학·공학·서사 층으로 분리해서 조심스럽게 읽는 것**입니다.

## 물질과 반물질이란 무엇인가

현대 입자물리학에서 많은 입자는 대응되는 **반입자(antiparticle)** 를 가집니다.

- 전자 `e-` 에는 양전자 `e+`
- 양성자 구성 쿼크에는 대응 반쿼크
- 물질은 보통 이런 입자들로 구성되고
- 반물질은 그에 대응하는 반입자들로 구성됩니다

중요한 점은, **반물질이 “가짜 물질”이 아니라 물리적으로 실재하는 상태**라는 것입니다.
다만 보통 물질과 만나면 매우 빠르게 **소멸(annihilation)** 하므로,
일상적인 환경에서는 거시적 반물질이 남아 있기 어렵습니다.

## 왜 반물질이 중요한가

반물질은 단지 SF적 호기심 대상이 아니라, 현대 물리학의 핵심 질문과 연결됩니다.

1. **우주론**
   - 왜 관측 가능한 우주는 물질 우세 상태인가
   - 왜 초기 우주에서 완전 대칭이 아니라 아주 작은 바리온 비대칭이 남았는가

2. **기초 입자물리**
   - CP violation이 얼마나 충분한가
   - Sakharov 조건을 만족하는 실제 메커니즘은 무엇인가

3. **실험실 공학**
   - 극소량 반입자를 어떤 trap에 가둘 수 있는가
   - 초고진공, 극저온, 자기장, 진동 제어가 얼마나 필요한가

4. **서사/해석**
   - “반물질 이동 성공” 같은 뉴스가 실제로 무엇을 뜻하는가
   - 실험실 trap 이송과 거시적 반물질 운송을 구분해야 한다

## 왜 이 엔진이 필요한가

반물질은 개념적으로 생소하고, 대중 서사에서는 과장되기 쉬운 주제입니다.
그래서 바로 “추적”, “발견”, “응용”으로 점프하면 해석이 쉽게 흐려집니다.

이 엔진은 그 점을 막기 위해 먼저 아래를 분리합니다.

- **현상학(phenomenology)**
  - 반물질이 왜 드문가
  - 어떤 차수(order-of-magnitude)가 자연스러운가

- **공학(engineering screening)**
  - trap transport가 어떤 조건에서 가능한가
  - confinement margin이 어디서 무너지는가

- **서사/narrative screening**
  - 어떤 payload가 구조적으로 충분한가
  - 무엇이 모순인지, 무엇이 미정인지

즉 “추적 엔진” 이전에 반드시 필요한 **기초 해석 레이어**라고 보면 됩니다.

## 저장소 정합성 (contracts / `__init__`)

이 저장소의 `antimatter_phenomenology/contracts.py` 는 **반물질 계약 전용**이어야 하고, 루트 `__init__.py` 는 본 README의 공개 API만 노출해야 한다.  
다른 엔진(SNN·memory 등) 파일이 섞이면 `foundation.py` import 가 깨진다. 배포 전 확인:

```bash
python scripts/verify_package_identity.py
python -m pytest tests/test_package_integrity.py -q
```

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

그리고 지금 버전부터는 이 층들을 **공통 4단계 판정 언어**로 다시 읽습니다.

- `positive` — 알려진 물리 안에서 구조적으로 타당
- `neutral` — 정보 부족, underspecified, 판단 유보
- `cautious` — 극한 실험실 조건이나 engineered confinement 필요
- `negative` — 차수(order-of-magnitude) 수준에서 모순

중요한 점은, `beyond_standard_model`류는 위 4단계 본선과 별개로 **추가 speculation 태그**처럼 다룬다는 것입니다.

이 방식이 중요한 이유는,
반물질 영역에서는 “물리적으로 틀린 것”과 “검증되지 않은 가설”을 같은 부정으로 뭉개면 안 되기 때문입니다.

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

## 지금 실제로 다루는 질문

이 엔진은 현재 다음 질문들에 답하려고 합니다.

- “왜 반물질이 우주에 거의 안 보이는가?”
- “실험실에서 극미량 반입자를 trap에 담아 이동하는 것이 가능한가?”
- “어떤 주장이나 뉴스가 known physics 안에서 구조적으로 맞는가?”
- “어떤 부분은 아직 우주론적 미해결 문제인가?”
- “반물질의 에너지 규모를 order-of-magnitude로 보면 어느 정도인가?”

반대로 아직 직접 하지 않는 것은 이렇습니다.

- 실제 detector telemetry ingest
- accelerator control
- full Monte Carlo transport
- precision cosmology solver
- 실시간 laboratory automation

## 모듈

| 모듈 | 역할 |
|------|------|
| `rarity.py` | `why_antimatter_is_rare_axes()`, `baryon_asymmetry_open_questions()` |
| `transport.py` | `mean_free_path_in_matter_m`, `cyclotron_radius_m`, `confinement_length_scale_m`, `assess_trap_transport()` |
| `asymmetry.py` | `observed_baryon_to_photon_ratio()`, `sakharov_viability_score()`, `assess_asymmetry_model()` |
| `energetics.py` | `annihilation_energy_j()`, `assess_annihilation_energy()` |
| `contracts.py` | foundation-level 공통 계약 (`Inventory`, `ConfinementContext`, `AsymmetryContext`) |
| `foundation.py` | `assess_antimatter_foundation()` — 희소성/이동/비대칭/에너지를 한 번에 요약 |
| `screening.py` | `screen_claim()`, `payload_from_news_style_summary()` |
| `constants.py` | SI 상수 (차수용) |

## Observer / Foundation 구조

현재 이 엔진은 다음 observer들을 느슨하게 묶는 foundation 역할을 합니다.

- `rarity observer`
- `transport / confinement observer`
- `asymmetry observer`
- `energetics observer`
- `claim screening observer`
- `foundation aggregator`

`foundation.py`는 이제 단일 `omega`만 주는 것이 아니라,

- `rarity_score_0_1`
- `transport_score_0_1`
- `asymmetry_score_0_1`
- `inventory_score_0_1`
- `stage`
- `confidence`
- `provenance`
- `evidence_tags`

를 함께 내보냅니다. 즉 “좋아 보인다/아니다”보다 **왜 그렇게 판정했는가**를 보수적으로 남기는 쪽입니다.

이게 중요한 이유는, 반물질처럼 민감한 주제에서는
`결론`보다 `근거 구조`가 더 중요하기 때문입니다.

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
print(foundation.stage, foundation.evidence_tags)
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

## 왜 “추적”을 말하나

여기서 `tracking`은 레이더로 반물질을 쫓는다는 뜻이 아닙니다.
현재 이 엔진에서의 추적은 더 보수적인 의미입니다.

- 어떤 반물질 담론이 어디서 실험실 현실과 만나는가
- 어떤 반물질 claim이 어떤 층위에서 무너지는가
- 어떤 물리적 질문이 아직 unresolved 상태인가
- 어떤 공학적 조건이 trap transport를 지탱하는가

즉 이 엔진은 **반물질 객체를 추적**하기보다,
**반물질 관련 주장·조건·위험·미해결성의 구조를 추적**합니다.

## 현재 한계와 보수적 해석

- 실제 검출기 DAQ나 trap telemetry를 읽는 엔진이 아닙니다.
- Monte Carlo 수송, QED/QCD 고정밀 계산, early-universe finite-temperature simulator가 아닙니다.
- `omega_foundation_0_1`은 “안전/진실 점수”가 아니라 **구조적 정렬도**입니다.
- 반물질은 본질적으로 예민한 주제라, 이 엔진은 **긍정적 결론보다 보수적 제한 조건**을 먼저 내도록 설계했습니다.

즉 지금 엔진은 “반물질이 가능하다”를 크게 말하는 도구가 아니라,
**무엇이 실제 실험실 조건이고, 무엇이 아직 미해결이며, 무엇이 차수상 무리인지**를 정리하는 기초 레이어입니다.

## 활용성

현재 시점의 현실적인 활용성은 다음과 같습니다.

1. **교육/연구 정리**
   - 반물질 개념을 층별로 설명
   - baryogenesis / transport / annihilation을 섞지 않고 분해

2. **스토리/시나리오 검토**
   - narrative payload를 screening
   - 구조적으로 모순인지, 보수적으로 유보해야 하는지 판단

3. **상위 엔진의 사전 필터**
   - `Antimatter_Foundation` 같은 통합 허브에서 하위 observer로 사용
   - 향후 confinement / cosmology / detector layer의 foundation 역할

4. **공학 intuition 정리**
   - trap transport에서 어떤 조건이 핵심인지 가볍게 설명
   - 실험실과 대중 서사를 구분

## 확장성과 다음 단계

이 엔진은 처음부터 “최종 반물질 엔진”을 목표로 하지 않았습니다.
대신 아래로 분화될 수 있는 기반을 깔고 있습니다.

- `Antimatter_Confinement_Foundation`
  - Penning/Ioffe/minimum-B trap
  - vibration, thermal, vacuum margin

- `Antimatter_Cosmology_Foundation`
  - leptogenesis / electroweak baryogenesis 외피
  - provenance-rich asymmetry comparison

- `Antimatter_Observer_System`
  - observer harmonization
  - provenance / confidence / evidence registry

- 장기적으로는 detector-side ingestion이나 lab automation과도 연결될 수 있지만,
  그건 **이 저장소의 다음 단계가 아니라 별도 하위 엔진**이 되어야 맞습니다.

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
