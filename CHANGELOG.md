# Changelog

## v0.3.1

- normalize assessment language into `positive / neutral / cautious / negative`
- add observer-style foundation metadata: `stage`, `confidence`, `provenance`, `evidence_tags`
- add `assess_rarity_foundation()` and include rarity in foundation aggregation
- add package integrity guards:
  - `scripts/verify_package_identity.py`
  - `tests/test_package_integrity.py`
- expand README and README_EN with:
  - matter vs antimatter basics
  - why antimatter matters
  - why this engine exists
  - practical use cases, extensibility, and explicit limits
- include package identity verification in `release_check.py`

## v0.3.0

- add `asymmetry.py` for `eta_B` and Sakharov proxy assessment
- add `transport` trap transport screening for laboratory antimatter movement
- add `energetics.py` for annihilation energy scale
- add `contracts.py` and `foundation.py` for unified foundation report
- fix test import boundary with `tests/conftest.py`
- expand README and README_EN for foundation-layer positioning
- add release scripts and SHA-256 manifest workflow
