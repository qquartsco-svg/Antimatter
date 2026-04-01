"""
Claim plausibility for narrative / design pipelines — **not** a truth oracle.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Mapping, Optional


class PlausibilityTier(str, Enum):
    CONSISTENT_WITH_KNOWN_PHYSICS = "consistent_with_known_physics"
    NEEDS_ENGINEERED_CONFINEMENT = "needs_engineered_confinement"
    CONTRADICTS_ORDER_OF_MAGNITUDE = "contradicts_order_of_magnitude"
    SPECULATIVE_BEYOND_SM = "speculative_beyond_standard_model"


@dataclass(frozen=True)
class ClaimScreeningResult:
    tier: PlausibilityTier
    notes: List[str]
    omega_structure: float  # 0–1 structural completeness of claim payload (not physical truth)


def screen_claim(payload: Mapping[str, Any]) -> ClaimScreeningResult:
    """
    Screen a **structured** claim dict (e.g. from an agent or scenario JSON).

    Expected optional keys:
      - ``bulk_kg`` (float): claimed macroscopic antimatter mass — almost always OOM wrong in air
      - ``environment`` (str): 'vacuum_trap' | 'atmosphere' | 'interstellar'
      - ``confinement_T`` (float): magnetic field Tesla order (if asserted)
      - ``hypothesis_tags`` (list[str]): e.g. 'dark_sector', 'wormhole'

    Returns a **tier** for orchestration / Ω decomposition, not experimental validation.
    """
    notes: List[str] = []
    bulk = float(payload.get("bulk_kg") or 0.0)
    env = str(payload.get("environment") or "unspecified")
    b_t = payload.get("confinement_T")
    tags = list(payload.get("hypothesis_tags") or [])

    omega_bits = 0
    max_bits = 4
    if payload.get("environment") is not None:
        omega_bits += 1
    if payload.get("bulk_kg") is not None:
        omega_bits += 1
    if b_t is not None:
        omega_bits += 1
    if tags:
        omega_bits += 1
    omega_structure = omega_bits / max_bits

    if any(t.lower() in ("wormhole", "ftl", "alchemy") for t in tags):
        notes.append("Tags invoke mechanisms outside validated phenomenology for this engine.")
        return ClaimScreeningResult(
            tier=PlausibilityTier.SPECULATIVE_BEYOND_SM,
            notes=notes,
            omega_structure=omega_structure,
        )

    if env == "atmosphere" and bulk > 1e-12:
        notes.append("Macroscopic antimatter in atmosphere contradicts annihilation time/density scales.")
        return ClaimScreeningResult(
            tier=PlausibilityTier.CONTRADICTS_ORDER_OF_MAGNITUDE,
            notes=notes,
            omega_structure=omega_structure,
        )

    if env == "vacuum_trap" and bulk <= 1e-18:
        notes.append("Trapped micro/nano-scale samples align with laboratory antimatter programs.")
        tier = PlausibilityTier.CONSISTENT_WITH_KNOWN_PHYSICS
        if b_t is None:
            notes.append("Missing asserted |B|; confinement not structurally specified.")
            tier = PlausibilityTier.NEEDS_ENGINEERED_CONFINEMENT
        return ClaimScreeningResult(tier=tier, notes=notes, omega_structure=omega_structure)

    if env == "interstellar":
        notes.append("Cosmic-ray antiparticles exist; bulk antimatter astrophysics is tightly constrained.")
        return ClaimScreeningResult(
            tier=PlausibilityTier.NEEDS_ENGINEERED_CONFINEMENT,
            notes=notes,
            omega_structure=omega_structure,
        )

    notes.append("Insufficient environment tag for screening; treat as underspecified.")
    return ClaimScreeningResult(
        tier=PlausibilityTier.NEEDS_ENGINEERED_CONFINEMENT,
        notes=notes,
        omega_structure=omega_structure,
    )


def payload_from_news_style_summary(*, moved_trapped_sample: bool) -> Dict[str, Any]:
    """
    Map a **boolean** news abstraction to a demo payload (no real telemetry).

    ``moved_trapped_sample=True`` ~ headlines about moving confined antihydrogen between traps.
    """
    if moved_trapped_sample:
        return {
            "environment": "vacuum_trap",
            "bulk_kg": 1e-27,  # order-of-magnitude ~ few nucleon masses scale (illustrative)
            "confinement_T": 1.0,
            "hypothesis_tags": [],
        }
    return {"environment": "atmosphere", "bulk_kg": 1.0, "hypothesis_tags": []}
