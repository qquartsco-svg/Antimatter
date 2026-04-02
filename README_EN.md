> **English.** Korean (정본): [README.md](README.md)

# Antimatter_Phenomenology_Engine v0.3.1

**A foundation layer for antimatter topics, starting from phenomenology and engineering screening**

**Umbrella hub (layer map + unified API):** [_staging/Antimatter_Foundation/README_EN.md](../Antimatter_Foundation/README_EN.md) — `layer_manifest()`, `run_unified_antimatter_stack()`.
If you use this repository as a **standalone clone**, that local umbrella path may not exist. This README is written so the package still makes sense on its own.

## What It Is

This repository is **not** a device that detects antimatter in the wild.
It is a conservative foundation layer for structuring questions such as:

- What is antimatter, physically?
- Why does the observable universe appear matter-dominated?
- What does successful trapped-antimatter transport actually mean?
- Which claims are compatible with known physics, and which are overstated?
- Which sub-engines should exist later for confinement, cosmology, and observers?

The goal is not to make antimatter sound grand.  
The goal is to make antimatter **legible, cautious, and decomposed**.

## What Matter And Antimatter Are

In modern particle physics, many particles have corresponding **antiparticles**.

- electron `e-` ↔ positron `e+`
- quarks ↔ antiquarks
- ordinary matter is built from particles
- antimatter is built from the corresponding antiparticles

Antimatter is therefore **not fictional** or “exotic fantasy matter”.
It is physically real. The difficulty is that antimatter and ordinary matter tend to
**annihilate** when they come into contact, so macroscopic persistence requires
extreme isolation and engineered confinement.

## Why It Matters

Antimatter is important because it touches several core questions at once.

1. **Cosmology**
   - Why is the visible universe matter-dominated?
   - What generated the tiny baryon asymmetry in the early universe?

2. **Particle physics**
   - Are known CP-violation sources sufficient?
   - Which baryogenesis or leptogenesis mechanisms remain viable?

3. **Laboratory engineering**
   - How can tiny antimatter samples be trapped and transported?
   - How strict must vacuum, cryogenic, magnetic, and vibration conditions be?

4. **Narrative discipline**
   - What exactly do headlines about antimatter transport mean?
   - How do we distinguish lab-scale trapped transport from fictional bulk transport?

## Repo integrity (`contracts` / `__init__`)

`antimatter_phenomenology/contracts.py` must be the **antimatter contract module** only, and package `__init__.py` must export this README’s public API. If another engine’s files are mixed in, `foundation.py` imports break. Before release:

```bash
python scripts/verify_package_identity.py
python -m pytest tests/test_package_integrity.py -q
```

Headlines about **moving trapped antimatter** usually refer to **laboratory** transport between **vacuum systems and magnetic traps**, not bulk shipment through air.  
This package is **not** telescope/radar software that localizes antimatter in the wild.

It structures:

- **Why antimatter is rare** — annihilation with matter, **cosmological baryon asymmetry (open)**, and accelerator/trap economics
- **Confinement intuition** — gyro-radius and mean-free-path **order-of-magnitude** helpers
- **Trap transport feasibility** — UHV, cryogenic temperature, magnetic confinement, mechanical shock margins
- **Asymmetry framing** — observed `eta_B`, Sakharov-condition proxy, model-vs-observation comparison
- **Energetics framing** — rest-mass annihilation energy scale
- **Narrative claim screening** — tiers for agent payloads (not truth adjudication)

## Why This Engine Exists

Antimatter is easy to overstate.
Popular narratives often skip directly from “it exists” to “it can be moved, stored,
or used at scale”. That jump is exactly what this engine tries to prevent.

So the engine separates:

- **phenomenology**
  - why antimatter is scarce
  - which scales are natural or unnatural

- **engineering screening**
  - what trap transport requires
  - where confinement margins collapse

- **narrative screening**
  - whether a claim is underspecified
  - whether it is merely speculative or actually order-of-magnitude inconsistent

## What It Does Not Do

- detector DAQ ingestion
- accelerator control
- Monte Carlo transport
- precision cosmology solving
- laboratory automation
- field tracking of free antimatter objects

## Identity (00_BRAIN style)

| Does | Does not |
|------|----------|
| Decompose phenomena for **education / design / storyboards** | Replace detector DAQ or experiment pipelines |
| List **mainstream open questions** | Assert new physics |
| Score **payload completeness** (`omega_structure`) | Prove non-human technology |

## Four-Stage Assessment Language

The current version normalizes observer outputs into a common four-stage language:

- `positive`
  - structurally plausible within known physics
- `neutral`
  - underspecified or insufficiently constrained
- `cautious`
  - requires extreme laboratory assumptions or engineered confinement
- `negative`
  - contradicts order-of-magnitude constraints

Speculative beyond-Standard-Model content is treated as an **additional tag axis**,
not as the whole assessment language by itself.

## Modules

| Module | Role |
|--------|------|
| `rarity.py` | `why_antimatter_is_rare_axes()`, `baryon_asymmetry_open_questions()` |
| `transport.py` | `mean_free_path_in_matter_m`, `cyclotron_radius_m`, `confinement_length_scale_m`, `assess_trap_transport()` |
| `asymmetry.py` | `observed_baryon_to_photon_ratio()`, `sakharov_viability_score()`, `assess_asymmetry_model()` |
| `energetics.py` | `annihilation_energy_j()`, `assess_annihilation_energy()` |
| `contracts.py` | common foundation-level contracts |
| `foundation.py` | unified summary via `assess_antimatter_foundation()` |
| `screening.py` | `screen_claim()`, `payload_from_news_style_summary()` |
| `constants.py` | SI constants for scaling |

## Outputs

This package currently acts as a loose foundation across several observers:

- `rarity observer`
- `transport / confinement observer`
- `asymmetry observer`
- `energetics observer`
- `claim screening observer`
- `foundation aggregator`

The foundation report no longer exposes only one aggregate score. It now also carries:

- `rarity_score_0_1`
- `transport_score_0_1`
- `asymmetry_score_0_1`
- `inventory_score_0_1`
- `stage`
- `confidence`
- `provenance`
- `evidence_tags`

That is deliberate. For antimatter, the important thing is often not the headline verdict,
but **why** a cautious verdict was reached.

There is also an important distinction:

- `screening tier`
  - a **claim-level** language for a specific payload
- `foundation stage`
  - a **foundation-level** summary across rarity, transport, asymmetry, and inventory

So `tier` is claim-scoped, while `stage` is engine-scoped.

## Test Status

Current validation status:

- full test suite: `14 passed`
- package integrity tests included
- `verify_package_identity.py` included
- `release_check.py` passing
- `SIGNATURE.sha256` integrity verification passing

## Quick Start

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
    TrapTransportScenario,
    assess_antimatter_foundation,
    assess_asymmetry_model,
    assess_trap_transport,
)

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

asym = assess_asymmetry_model(
    SakharovProxyInputs(
        cp_violation_strength_0_1=0.6,
        baryon_violation_strength_0_1=0.7,
        out_of_equilibrium_strength_0_1=0.8,
        model_eta_b=6.0e-10,
    )
)

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
```

## A structure for inferring why antimatter is scarce

1. **Annihilation** — contact with ordinary matter removes antimatter quickly without engineered vacuum + fields.  
2. **Cosmological asymmetry** — the visible universe is **matter-dominated**; the dynamical origin of η_B remains an **open problem** in particle cosmology.  
3. **Lab scale** — production and storage are **tiny** by macroscopic standards.

## Why “tracking” appears in the discussion

In this repository, “tracking” does **not** mean radar-tracking free antimatter objects.
It means something more conservative:

- tracking which claims survive known-physics screening
- tracking which constraints come from lab transport reality
- tracking which questions remain cosmologically unresolved
- tracking how evidence provenance changes confidence

So this is better understood as **structure tracking** for antimatter discourse,
not object tracking in open space.

## Formulas in scope

- mean free path: `lambda ~= 1 / (n sigma)`
- non-relativistic gyroradius: `r = m v_perp / (|q| B)`
- observed baryon asymmetry scale: `eta_B ~= 6.1e-10`
- annihilation energy: `E = (m_antimatter + m_matter)c^2`

These are **screening-level** formulas, not a detector or early-universe simulator.

## Practical use cases

The most realistic uses of this engine today are:

1. **Education and research framing**
   - separating annihilation, asymmetry, and transport questions cleanly

2. **Narrative or scenario review**
   - screening payloads before they become exaggerated system assumptions

3. **Upstream foundation for later engines**
   - confinement foundation
   - cosmology foundation
   - observer harmonization layer

4. **Engineering intuition**
   - explaining why trapped transport is hard
   - clarifying why laboratory success does not solve cosmological asymmetry

## Limits and careful interpretation

- not detector telemetry ingestion
- not accelerator control software
- not Monte Carlo transport
- not a high-precision QED/QCD engine
- not a finite-temperature early-universe simulator
- `omega_foundation_0_1` is not a truth score or safety guarantee

This engine is intentionally conservative.  
Its job is to keep the discussion grounded when the topic itself is easy to mythologize.

## Extensibility

The natural next layers are:

1. `Antimatter_Confinement_Foundation`
   - Penning/Ioffe/minimum-B trap engineering
   - thermal / vacuum / shock margins

2. `Antimatter_Cosmology_Foundation`
   - leptogenesis and electroweak baryogenesis wrappers
   - richer provenance for asymmetry reasoning

3. `Antimatter_Observer_System`
   - harmonized observer outputs
   - shared confidence / provenance / evidence vocabulary

## Requirements

- Python **3.10+**, **stdlib-only** at runtime

## License

MIT

---

*Screening and narrative alignment — not a substitute for lab safety or particle-physics adjudication.*
