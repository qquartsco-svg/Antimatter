"""
Basic antimatter energetics.

This module is intentionally conservative:
- it estimates rest-mass annihilation energy,
- it does not model directed conversion efficiency,
- it should not be read as a propulsion design engine.
"""
from __future__ import annotations

from dataclasses import dataclass

from .constants import C_LIGHT_MS


@dataclass(frozen=True)
class AnnihilationEnergyAssessment:
    antimatter_mass_kg: float
    matter_mass_kg: float
    total_annihilation_energy_j: float
    total_annihilation_energy_kwh: float
    engineering_note: str


def annihilation_energy_j(*, antimatter_mass_kg: float, matter_mass_kg: float | None = None) -> float:
    """
    E = (m_antimatter + m_matter) c^2

    If `matter_mass_kg` is omitted, assume equal ordinary matter is available.
    """
    if antimatter_mass_kg <= 0.0:
        return 0.0
    matter = antimatter_mass_kg if matter_mass_kg is None else max(0.0, matter_mass_kg)
    return (antimatter_mass_kg + matter) * (C_LIGHT_MS ** 2)


def assess_annihilation_energy(*, antimatter_mass_kg: float, matter_mass_kg: float | None = None) -> AnnihilationEnergyAssessment:
    energy_j = annihilation_energy_j(
        antimatter_mass_kg=antimatter_mass_kg,
        matter_mass_kg=matter_mass_kg,
    )
    energy_kwh = energy_j / 3.6e6
    if antimatter_mass_kg <= 0.0:
        note = "No antimatter inventory supplied."
    elif antimatter_mass_kg < 1e-18:
        note = "Energy release is real but still at trapped micro-sample scale."
    elif antimatter_mass_kg < 1e-9:
        note = "Energy density is large in principle, but storage and controlled use dominate feasibility."
    else:
        note = "Macroscopic antimatter mass quickly moves from phenomenology into severe engineering infeasibility."
    return AnnihilationEnergyAssessment(
        antimatter_mass_kg=antimatter_mass_kg,
        matter_mass_kg=antimatter_mass_kg if matter_mass_kg is None else matter_mass_kg,
        total_annihilation_energy_j=energy_j,
        total_annihilation_energy_kwh=energy_kwh,
        engineering_note=note,
    )
