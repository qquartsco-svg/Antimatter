from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Tuple


class AntimatterDomain(str, Enum):
    PHENOMENOLOGY = "phenomenology"
    CONFINEMENT = "confinement"
    TRANSPORT = "transport"
    ASYMMETRY = "asymmetry"
    ENERGETICS = "energetics"
    CLAIM_SCREENING = "claim_screening"


class AntimatterAssessmentStage(str, Enum):
    POSITIVE = "positive"
    NEUTRAL = "neutral"
    CAUTIOUS = "cautious"
    NEGATIVE = "negative"


class AntimatterConfidence(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class AntimatterProvenance(str, Enum):
    LAB_CONSTRAINTS = "lab_constraints"
    COSMOLOGY_PRIOR = "cosmology_prior"
    ORDER_OF_MAGNITUDE_SCREENING = "order_of_magnitude_screening"
    NARRATIVE_PAYLOAD = "narrative_payload"


@dataclass(frozen=True)
class AntimatterInventory:
    antiparticle_count: int = 0
    estimated_mass_kg: float = 0.0
    species: str = "antiproton"


@dataclass(frozen=True)
class AntimatterConfinementContext:
    magnetic_field_t: float
    vacuum_pa: float
    cryogenic_temperature_k: float
    peak_acceleration_ms2: float = 0.0
    transfer_time_s: float = 0.0


@dataclass(frozen=True)
class AntimatterAsymmetryContext:
    cp_violation_strength_0_1: float
    baryon_violation_strength_0_1: float
    out_of_equilibrium_strength_0_1: float
    model_eta_b: Optional[float] = None


@dataclass(frozen=True)
class AntimatterFoundationReport:
    domain: AntimatterDomain
    omega_foundation_0_1: float
    stage: AntimatterAssessmentStage
    confidence: AntimatterConfidence
    provenance: Tuple[AntimatterProvenance, ...]
    rarity_score_0_1: float
    transport_score_0_1: float
    asymmetry_score_0_1: float
    inventory_score_0_1: float
    evidence_tags: Tuple[str, ...]
    summary: str
    key_risk: str
    recommendation: str
