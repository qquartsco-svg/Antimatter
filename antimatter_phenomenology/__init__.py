"""
Antimatter phenomenology — educational screening, not a detector.

This package does **not** ingest telescope or lab telemetry to “find” antimatter.
It encodes **order-of-magnitude** constraints and **open-problem** framing from
mainstream physics (annihilation, cosmological asymmetry, confinement).
"""

from .asymmetry import (
    AsymmetryAssessment,
    SakharovProxyInputs,
    assess_asymmetry_model,
    observed_baryon_to_photon_ratio,
    sakharov_viability_score,
)
from .contracts import (
    AntimatterAssessmentStage,
    AntimatterAsymmetryContext,
    AntimatterConfidence,
    AntimatterConfinementContext,
    AntimatterDomain,
    AntimatterFoundationReport,
    AntimatterInventory,
    AntimatterProvenance,
)
from .energetics import (
    AnnihilationEnergyAssessment,
    annihilation_energy_j,
    assess_annihilation_energy,
)
from .foundation import assess_antimatter_foundation
from .rarity import (
    RarityAssessment,
    assess_rarity_foundation,
    baryon_asymmetry_open_questions,
    why_antimatter_is_rare_axes,
)
from .transport import (
    TrapTransportAssessment,
    TrapTransportScenario,
    assess_trap_transport,
    confinement_length_scale_m,
    cyclotron_radius_m,
    mean_free_path_in_matter_m,
    relativistic_larmor_radius_m,
)
from .screening import ClaimScreeningResult, screen_claim

__all__ = [
    "baryon_asymmetry_open_questions",
    "why_antimatter_is_rare_axes",
    "SakharovProxyInputs",
    "AsymmetryAssessment",
    "AntimatterAssessmentStage",
    "AntimatterDomain",
    "AntimatterConfidence",
    "AntimatterInventory",
    "AntimatterConfinementContext",
    "AntimatterAsymmetryContext",
    "AntimatterFoundationReport",
    "AntimatterProvenance",
    "RarityAssessment",
    "AnnihilationEnergyAssessment",
    "observed_baryon_to_photon_ratio",
    "sakharov_viability_score",
    "assess_rarity_foundation",
    "assess_asymmetry_model",
    "annihilation_energy_j",
    "assess_annihilation_energy",
    "TrapTransportScenario",
    "TrapTransportAssessment",
    "assess_trap_transport",
    "assess_antimatter_foundation",
    "confinement_length_scale_m",
    "cyclotron_radius_m",
    "mean_free_path_in_matter_m",
    "relativistic_larmor_radius_m",
    "ClaimScreeningResult",
    "screen_claim",
]

__version__ = "0.3.1"
