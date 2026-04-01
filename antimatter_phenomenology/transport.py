"""
Order-of-magnitude transport / confinement (educational).

Real trap design is experiment-specific; here we expose **scaling intuition**.
"""
from __future__ import annotations

from dataclasses import dataclass
import math

from .constants import C_LIGHT_MS, E_CHARGE_C, M_ELECTRON_KG


@dataclass(frozen=True)
class TrapTransportScenario:
    particle_count: int
    magnetic_field_t: float
    vacuum_pa: float
    cryogenic_temperature_k: float
    peak_acceleration_ms2: float
    transfer_time_s: float


@dataclass(frozen=True)
class TrapTransportAssessment:
    confinement_score_0_1: float
    survival_probability_proxy_0_1: float
    engineering_notes: list[str]


def mean_free_path_in_matter_m(*, density_kg_m3: float, sigma_m2: float) -> float:
    """
    λ ≈ 1 / (n σ) with n = ρ / m_p (order-of-magnitude nucleon target density).

    `sigma_m2` is an effective interaction cross-section placeholder; use literature
    values for specific processes — this is **not** a Monte Carlo transport code.
    """
    if density_kg_m3 <= 0 or sigma_m2 <= 0:
        return float("inf")
    n = density_kg_m3 / 1.67e-27  # ~ proton mass kg
    return 1.0 / (n * sigma_m2)


def cyclotron_radius_m(m_kg: float, q_c: float, b_tesla: float, v_perp_ms: float) -> float:
    """Non-relativistic gyroradius r = m v_perp / (|q| B)."""
    if b_tesla <= 0 or q_c == 0:
        return float("inf")
    return m_kg * abs(v_perp_ms) / (abs(q_c) * b_tesla)


def confinement_length_scale_m(*, b_tesla: float, kinetic_ev: float, species: str = "electron") -> float:
    """
    Illustrative gyroradius for a trapped lepton at given |B| and kinetic energy.

    species: 'electron' or 'positron' (same mass here).
    """
    m = M_ELECTRON_KG
    q = E_CHARGE_C
    if species not in ("electron", "positron"):
        raise ValueError("species must be 'electron' or 'positron' for this demo")
    # v from non-rel E = 1/2 m v^2
    e_j = kinetic_ev * E_CHARGE_C  # 1 eV in J
    v = math.sqrt(max(0.0, 2.0 * e_j / m))
    return cyclotron_radius_m(m, q, b_tesla, v)


def relativistic_larmor_radius_m(
    m_kg: float,
    q_c: float,
    b_tesla: float,
    gamma: float,
    beta: float,
) -> float:
    """Ultra-relativistic: r ≈ γ m v_perp / (|q| B) with v ≈ c beta."""
    if b_tesla <= 0 or q_c == 0 or gamma <= 1.0:
        return float("inf")
    v_perp = C_LIGHT_MS * beta
    return gamma * m_kg * v_perp / (abs(q_c) * b_tesla)


def assess_trap_transport(scenario: TrapTransportScenario) -> TrapTransportAssessment:
    """
    Engineering proxy for moving trapped antimatter between apparatus.

    This is not a Penning-trap simulator. It converts obvious risk drivers
    (field strength, vacuum quality, cryogenic temperature, mechanical shock)
    into a coarse screening score.
    """
    notes: list[str] = []

    field_score = max(0.0, min(1.0, scenario.magnetic_field_t / 1.0))
    if field_score < 0.7:
        notes.append("Magnetic field is weak for comfortable trap transport margins.")

    vacuum_score = 1.0
    if scenario.vacuum_pa > 1e-9:
        vacuum_score = max(0.0, min(1.0, 1e-9 / scenario.vacuum_pa))
        notes.append("Vacuum is poorer than typical ultra-high-vacuum transport conditions.")

    temperature_score = 1.0 if scenario.cryogenic_temperature_k <= 10.0 else max(
        0.0, min(1.0, 10.0 / scenario.cryogenic_temperature_k)
    )
    if temperature_score < 0.7:
        notes.append("Cryogenic margin is shallow for precision trap transport.")

    acceleration_score = 1.0 if scenario.peak_acceleration_ms2 <= 2.0 else max(
        0.0, min(1.0, 2.0 / scenario.peak_acceleration_ms2)
    )
    if acceleration_score < 0.7:
        notes.append("Mechanical acceleration is high enough to threaten trap stability.")

    time_score = 1.0 if scenario.transfer_time_s <= 1800.0 else max(
        0.0, min(1.0, 1800.0 / scenario.transfer_time_s)
    )
    if time_score < 0.7:
        notes.append("Long transfer duration increases cumulative containment risk.")

    confinement = (
        0.30 * field_score
        + 0.25 * vacuum_score
        + 0.20 * temperature_score
        + 0.15 * acceleration_score
        + 0.10 * time_score
    )
    survival = max(0.0, min(1.0, confinement))

    if scenario.particle_count <= 0:
        notes.append("No trapped antiparticles specified.")
        survival = 0.0
        confinement = 0.0
    elif scenario.particle_count < 100:
        notes.append("This is an extremely small sample; transport can still matter scientifically.")
    else:
        notes.append("Sample size is still tiny in mass, but meaningful for precision experiments.")

    return TrapTransportAssessment(
        confinement_score_0_1=confinement,
        survival_probability_proxy_0_1=survival,
        engineering_notes=notes,
    )
