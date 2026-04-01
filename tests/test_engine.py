import math

from antimatter_phenomenology import (
    AntimatterAsymmetryContext,
    AntimatterConfinementContext,
    AntimatterInventory,
    SakharovProxyInputs,
    annihilation_energy_j,
    assess_annihilation_energy,
    assess_antimatter_foundation,
    assess_asymmetry_model,
    assess_trap_transport,
    baryon_asymmetry_open_questions,
    observed_baryon_to_photon_ratio,
    confinement_length_scale_m,
    screen_claim,
    TrapTransportScenario,
    why_antimatter_is_rare_axes,
)
from antimatter_phenomenology.screening import (
    PlausibilityTier,
    payload_from_news_style_summary,
)
from antimatter_phenomenology.transport import mean_free_path_in_matter_m


def test_rarity_axes_non_empty():
    axes = why_antimatter_is_rare_axes()
    assert len(axes) >= 3
    names = {a.name for a in axes}
    assert "annihilation" in names
    assert "cosmological_asymmetry" in names


def test_open_questions():
    q = baryon_asymmetry_open_questions()
    assert any("η" in x or "eta" in x.lower() or "baryon" in x.lower() for x in q)


def test_mfp_positive():
    lam = mean_free_path_in_matter_m(density_kg_m3=1000.0, sigma_m2=1e-28)
    assert lam > 0 and math.isfinite(lam)


def test_confinement_radius():
    r = confinement_length_scale_m(b_tesla=3.0, kinetic_ev=1.0, species="positron")
    assert 1e-8 < r < 1e-2


def test_screen_news_payload():
    good = payload_from_news_style_summary(moved_trapped_sample=True)
    res = screen_claim(good)
    assert res.tier in (
        PlausibilityTier.CONSISTENT_WITH_KNOWN_PHYSICS,
        PlausibilityTier.NEEDS_ENGINEERED_CONFINEMENT,
    )

    bad = payload_from_news_style_summary(moved_trapped_sample=False)
    res_bad = screen_claim(bad)
    assert res_bad.tier == PlausibilityTier.CONTRADICTS_ORDER_OF_MAGNITUDE


def test_observed_eta_b_positive():
    assert observed_baryon_to_photon_ratio() > 0.0


def test_asymmetry_assessment_alignment():
    result = assess_asymmetry_model(
        SakharovProxyInputs(
            cp_violation_strength_0_1=0.7,
            baryon_violation_strength_0_1=0.8,
            out_of_equilibrium_strength_0_1=0.9,
            model_eta_b=6.0e-10,
        )
    )
    assert result.sakharov_score_0_1 > 0.0
    assert result.eta_alignment_ratio_0_1 > 0.5


def test_trap_transport_assessment():
    assessment = assess_trap_transport(
        TrapTransportScenario(
            particle_count=92,
            magnetic_field_t=1.2,
            vacuum_pa=5e-10,
            cryogenic_temperature_k=6.0,
            peak_acceleration_ms2=1.5,
            transfer_time_s=1200.0,
        )
    )
    assert assessment.confinement_score_0_1 > 0.5
    assert assessment.survival_probability_proxy_0_1 > 0.5


def test_annihilation_energy_positive():
    energy = annihilation_energy_j(antimatter_mass_kg=1e-12)
    assert energy > 0.0
    assessed = assess_annihilation_energy(antimatter_mass_kg=1e-12)
    assert assessed.total_annihilation_energy_kwh > 0.0


def test_foundation_report():
    report = assess_antimatter_foundation(
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
    assert report.omega_foundation_0_1 > 0.0
    assert report.summary
