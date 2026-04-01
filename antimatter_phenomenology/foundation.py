"""
Unified antimatter foundation view.

This is a common entrypoint for the package when the caller wants a single
screening-style summary across rarity, confinement, asymmetry, and energetics.
"""
from __future__ import annotations

from .asymmetry import assess_asymmetry_model
from .contracts import (
    AntimatterAsymmetryContext,
    AntimatterConfinementContext,
    AntimatterDomain,
    AntimatterFoundationReport,
    AntimatterInventory,
)
from .energetics import assess_annihilation_energy
from .transport import TrapTransportScenario, assess_trap_transport


def assess_antimatter_foundation(
    *,
    inventory: AntimatterInventory,
    confinement: AntimatterConfinementContext,
    asymmetry: AntimatterAsymmetryContext,
) -> AntimatterFoundationReport:
    transport = assess_trap_transport(
        TrapTransportScenario(
            particle_count=inventory.antiparticle_count,
            magnetic_field_t=confinement.magnetic_field_t,
            vacuum_pa=confinement.vacuum_pa,
            cryogenic_temperature_k=confinement.cryogenic_temperature_k,
            peak_acceleration_ms2=confinement.peak_acceleration_ms2,
            transfer_time_s=confinement.transfer_time_s,
        )
    )
    asym = assess_asymmetry_model(asymmetry)
    energy = assess_annihilation_energy(antimatter_mass_kg=inventory.estimated_mass_kg)

    omega = (
        0.40 * transport.survival_probability_proxy_0_1
        + 0.35 * asym.sakharov_score_0_1
        + 0.25 * (1.0 if inventory.antiparticle_count > 0 else 0.0)
    )

    if inventory.antiparticle_count <= 0:
        summary = "No trapped antimatter inventory is present; this remains a conceptual foundation state."
        risk = "no_inventory"
        recommendation = "Start from phenomenology and confinement requirements before transport claims."
    elif transport.survival_probability_proxy_0_1 < 0.5:
        summary = "Confinement margins are weak; laboratory transport stability is the dominant bottleneck."
        risk = "trap_instability"
        recommendation = "Increase UHV, magnetic-field margin, cryogenic stability, and shock isolation."
    else:
        summary = "Micro-sample confinement and transport look structurally plausible within laboratory assumptions."
        risk = "cosmological_asymmetry_unsolved"
        recommendation = (
            "Treat transport success and matter-antimatter asymmetry as separate questions: "
            "engineering may work while baryogenesis remains unresolved."
        )

    if energy.total_annihilation_energy_j > 0.0:
        summary += f" Rest-energy proxy is {energy.total_annihilation_energy_j:.3e} J."

    return AntimatterFoundationReport(
        domain=AntimatterDomain.PHENOMENOLOGY,
        omega_foundation_0_1=max(0.0, min(1.0, omega)),
        summary=summary,
        key_risk=risk,
        recommendation=recommendation,
    )
