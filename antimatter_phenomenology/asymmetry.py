"""
Matter–antimatter asymmetry helpers.

This module does not solve baryogenesis. It provides structured proxies for:
- the observed baryon-to-photon ratio eta_B,
- whether a candidate mechanism satisfies Sakharov-style ingredients,
- whether a proposed model prediction is in the right order of magnitude.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import List, Optional


OBSERVED_ETA_B = 6.1e-10


@dataclass(frozen=True)
class SakharovProxyInputs:
    cp_violation_strength_0_1: float
    baryon_violation_strength_0_1: float
    out_of_equilibrium_strength_0_1: float
    model_eta_b: Optional[float] = None


@dataclass(frozen=True)
class AsymmetryAssessment:
    observed_eta_b: float
    model_eta_b: Optional[float]
    sakharov_score_0_1: float
    eta_alignment_ratio_0_1: float
    plausibility_notes: List[str]


def observed_baryon_to_photon_ratio() -> float:
    """Return the observed order-of-magnitude baryon asymmetry eta_B."""
    return OBSERVED_ETA_B


def sakharov_viability_score(
    *,
    cp_violation_strength_0_1: float,
    baryon_violation_strength_0_1: float,
    out_of_equilibrium_strength_0_1: float,
) -> float:
    """
    Geometric-mean style proxy for the three Sakharov ingredients.

    This is a screening score only; it is not a derivation from finite-temperature QFT.
    """
    terms = [
        max(0.0, min(1.0, cp_violation_strength_0_1)),
        max(0.0, min(1.0, baryon_violation_strength_0_1)),
        max(0.0, min(1.0, out_of_equilibrium_strength_0_1)),
    ]
    if any(term == 0.0 for term in terms):
        return 0.0
    return math.prod(terms) ** (1.0 / 3.0)


def assess_asymmetry_model(inputs: SakharovProxyInputs) -> AsymmetryAssessment:
    """
    Assess whether a candidate asymmetry explanation is at least structurally aligned.

    `model_eta_b` is optional; when omitted, the result remains an "open-problem" proxy.
    """
    score = sakharov_viability_score(
        cp_violation_strength_0_1=inputs.cp_violation_strength_0_1,
        baryon_violation_strength_0_1=inputs.baryon_violation_strength_0_1,
        out_of_equilibrium_strength_0_1=inputs.out_of_equilibrium_strength_0_1,
    )
    notes: List[str] = []
    if score < 0.3:
        notes.append("Sakharov ingredients are too weak to support a compelling asymmetry scenario.")
    elif score < 0.7:
        notes.append("Sakharov ingredients are present but not strongly aligned.")
    else:
        notes.append("Sakharov ingredients are structurally strong enough to motivate further study.")

    alignment = 0.0
    if inputs.model_eta_b is None:
        notes.append("No model eta_B supplied; this remains an open-problem framing only.")
    else:
        if inputs.model_eta_b <= 0.0:
            alignment = 0.0
            notes.append("Non-positive eta_B prediction is incompatible with the observed matter excess.")
        else:
            ratio = min(inputs.model_eta_b, OBSERVED_ETA_B) / max(inputs.model_eta_b, OBSERVED_ETA_B)
            alignment = max(0.0, min(1.0, ratio))
            if alignment > 0.5:
                notes.append("Model eta_B is within the same order of magnitude as the observed value.")
            else:
                notes.append("Model eta_B misses the observed value by more than an order-of-magnitude proxy.")

    return AsymmetryAssessment(
        observed_eta_b=OBSERVED_ETA_B,
        model_eta_b=inputs.model_eta_b,
        sakharov_score_0_1=score,
        eta_alignment_ratio_0_1=alignment,
        plausibility_notes=notes,
    )
