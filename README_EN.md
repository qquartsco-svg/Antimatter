> **English.** Korean (정본): [README.md](README.md)

# Antimatter_Phenomenology_Engine v0.3.0

**A foundation layer for antimatter topics, starting from phenomenology and engineering screening**

**Umbrella hub (layer map + unified API):** [_staging/Antimatter_Foundation/README_EN.md](../Antimatter_Foundation/README_EN.md) — `layer_manifest()`, `run_unified_antimatter_stack()`.

Headlines about **moving trapped antimatter** usually refer to **laboratory** transport between **vacuum systems and magnetic traps**, not bulk shipment through air.  
This package is **not** telescope/radar software that localizes antimatter in the wild.

It structures:

- **Why antimatter is rare** — annihilation with matter, **cosmological baryon asymmetry (open)**, and accelerator/trap economics
- **Confinement intuition** — gyro-radius and mean-free-path **order-of-magnitude** helpers
- **Trap transport feasibility** — UHV, cryogenic temperature, magnetic confinement, mechanical shock margins
- **Asymmetry framing** — observed `eta_B`, Sakharov-condition proxy, model-vs-observation comparison
- **Energetics framing** — rest-mass annihilation energy scale
- **Narrative claim screening** — tiers for agent payloads (not truth adjudication)

## Identity (00_BRAIN style)

| Does | Does not |
|------|----------|
| Decompose phenomena for **education / design / storyboards** | Replace detector DAQ or experiment pipelines |
| List **mainstream open questions** | Assert new physics |
| Score **payload completeness** (`omega_structure`) | Prove non-human technology |

## Modules

| Module | Role |
|--------|------|
| `rarity.py` | `why_antimatter_is_rare_axes()`, `baryon_asymmetry_open_questions()` |
| `transport.py` | `mean_free_path_in_matter_m`, `confinement_length_scale_m`, `assess_trap_transport()` |
| `asymmetry.py` | `observed_baryon_to_photon_ratio()`, `sakharov_viability_score()`, `assess_asymmetry_model()` |
| `energetics.py` | `annihilation_energy_j()`, `assess_annihilation_energy()` |
| `contracts.py` | common foundation-level contracts |
| `foundation.py` | unified summary via `assess_antimatter_foundation()` |
| `screening.py` | `screen_claim()`, `payload_from_news_style_summary()` |
| `constants.py` | SI constants for scaling |

## Quick start

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

## Why antimatter is scarce (skeleton)

1. **Annihilation** — contact with ordinary matter removes antimatter quickly without engineered vacuum + fields.  
2. **Cosmological asymmetry** — the visible universe is **matter-dominated**; the dynamical origin of η_B remains an **open problem** in particle cosmology.  
3. **Lab scale** — production and storage are **tiny** by macroscopic standards.

## Formulas in scope

- mean free path: `lambda ~= 1 / (n sigma)`
- non-relativistic gyroradius: `r = m v_perp / (|q| B)`
- observed baryon asymmetry scale: `eta_B ~= 6.1e-10`
- annihilation energy: `E = (m_antimatter + m_matter)c^2`

These are **screening-level** formulas, not a detector or early-universe simulator.

## Requirements

- Python **3.10+**, **stdlib-only** at runtime

## License

MIT

---

*Screening and narrative alignment — not a substitute for lab safety or particle-physics adjudication.*
