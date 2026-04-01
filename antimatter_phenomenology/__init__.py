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
    AntimatterAsymmetryContext,
    AntimatterConfinementContext,
    AntimatterDomain,
    AntimatterFoundationReport,
    AntimatterInventory,
)
from .energetics import (
    AnnihilationEnergyAssessment,
    annihilation_energy_j,
    assess_annihilation_energy,
)
from .foundation import assess_antimatter_foundation
from .rarity import baryon_asymmetry_open_questions, why_antimatter_is_rare_axes
from .transport import (
    TrapTransportAssessment,
    TrapTransportScenario,
    assess_trap_transport,
    confinement_length_scale_m,
    mean_free_path_in_matter_m,
)
from .screening import ClaimScreeningResult, screen_claim

__all__ = [
    "baryon_asymmetry_open_questions",
    "why_antimatter_is_rare_axes",
    "SakharovProxyInputs",
    "AsymmetryAssessment",
    "AntimatterDomain",
    "AntimatterInventory",
    "AntimatterConfinementContext",
    "AntimatterAsymmetryContext",
    "AntimatterFoundationReport",
    "AnnihilationEnergyAssessment",
    "observed_baryon_to_photon_ratio",
    "sakharov_viability_score",
    "assess_asymmetry_model",
    "annihilation_energy_j",
    "assess_annihilation_energy",
    "TrapTransportScenario",
    "TrapTransportAssessment",
    "assess_trap_transport",
    "assess_antimatter_foundation",
    "confinement_length_scale_m",
    "mean_free_path_in_matter_m",
    "ClaimScreeningResult",
    "screen_claim",
]

__version__ = "0.3.0"
