"""
Why antimatter is scarce — structured axes (no new physics claims).

References (conceptual): Sakharov conditions for baryogenesis; matter–antimatter
asymmetry as an open Standard-Model + cosmology problem.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List

from .contracts import (
    AntimatterAssessmentStage,
    AntimatterConfidence,
    AntimatterProvenance,
)


@dataclass(frozen=True)
class RarityAxis:
    """One explanatory axis; `detail` is screening-level text, not a proof."""

    name: str
    summary: str
    detail: str


@dataclass(frozen=True)
class RarityAssessment:
    score_0_1: float
    stage: AntimatterAssessmentStage
    confidence: AntimatterConfidence
    provenance: AntimatterProvenance
    unresolved_question_count: int
    summary: str
    evidence_tags: List[str]


def why_antimatter_is_rare_axes() -> List[RarityAxis]:
    """
    Human-visible universe is matter-dominated; antimatter is rare because:

    1) **Annihilation** — charge-conjugate partners in contact annihilate to photons
       (and other products at high energy). Macroscopic amounts cannot persist in
       ordinary matter environments without extreme isolation.

    2) **Cosmological asymmetry** — the Big Bang produced a tiny **baryon–antibaryon
       imbalance** (observed today as all visible baryons). The *mechanism* that
       produced this asymmetry is still an **open problem** (Sakharov conditions
       are necessary but not sufficient to pick the correct model).

    3) **Production cost** — laboratory antiparticles are made at accelerators with
       enormous energy expenditure per stored ion; storage uses electromagnetic traps
       under ultra-high vacuum.

    This function returns **pedagogical** axes for decomposition / Ω-style reasoning,
    not experimental abundances.
    """
    return [
        RarityAxis(
            name="annihilation",
            summary="Contact with ordinary matter removes antimatter rapidly.",
            detail=(
                "Low-energy e+ in solids annihilate within microscopic distances; "
                "high-Z targets shorten effective penetration. Macroscopic 'chunks' "
                "require vacuum confinement."
            ),
        ),
        RarityAxis(
            name="cosmological_asymmetry",
            summary="Observed universe is baryon-dominated; antibaryons are not a bulk component.",
            detail=(
                "CMB and large-scale structure fit ΛCDM with negligible relic "
                "antimatter density. The *why* of η_B (baryon-to-photon ratio) vs "
                "symmetric early universe is open (baryogenesis / leptogenesis "
                "candidates beyond minimal thermal history)."
            ),
        ),
        RarityAxis(
            name="laboratory_scale",
            summary="Trapped antimatter is produced and held in engineered traps, not mined.",
            detail=(
                "ALPHA/CERN-class experiments use Penning/Ioffe traps, magnetic "
                "minimums, and cryogenic UHV. 'Transport' news refers to moving "
                "confined samples between apparatus — not bulk shipping through air."
            ),
        ),
    ]


def baryon_asymmetry_open_questions() -> List[str]:
    """Bullet list of mainstream open questions (screening metadata)."""
    return [
        "Which beyond-equilibrium process generated the observed η_B?",
        "Are Standard Model CP violation sources sufficient in early universe kinetics?",
        "Role of neutrino sector (leptogenesis) vs electroweak baryogenesis?",
        "Gravitational or higher-dimension effects — speculative until constrained by data.",
    ]


def assess_rarity_foundation() -> RarityAssessment:
    """
    Summarize how mature the engine's *framing* of antimatter rarity is.

    This is intentionally conservative: the structure is mainstream and useful,
    but the cosmological origin of the asymmetry remains unresolved.
    """
    axes = why_antimatter_is_rare_axes()
    open_questions = baryon_asymmetry_open_questions()
    structural_completeness = min(1.0, len(axes) / 3.0)
    unresolved_penalty = min(0.35, 0.05 * len(open_questions))
    score = max(0.0, min(1.0, 0.85 * structural_completeness - unresolved_penalty))

    if score >= 0.75:
        stage = AntimatterAssessmentStage.POSITIVE
    elif score >= 0.55:
        stage = AntimatterAssessmentStage.CAUTIOUS
    elif score >= 0.35:
        stage = AntimatterAssessmentStage.NEUTRAL
    else:
        stage = AntimatterAssessmentStage.NEGATIVE

    return RarityAssessment(
        score_0_1=score,
        stage=stage,
        confidence=AntimatterConfidence.MEDIUM,
        provenance=AntimatterProvenance.COSMOLOGY_PRIOR,
        unresolved_question_count=len(open_questions),
        summary=(
            "Antimatter rarity is structurally framed by annihilation, cosmological asymmetry, "
            "and laboratory scarcity, but the baryogenesis mechanism remains unresolved."
        ),
        evidence_tags=[
            "annihilation_axis",
            "cosmological_asymmetry_open",
            "laboratory_scale_limit",
        ],
    )
