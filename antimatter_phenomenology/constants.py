"""SI constants and particle scales (pedagogical precision)."""
from __future__ import annotations

# CODATA-style; sufficient for order-of-magnitude engine
C_LIGHT_MS = 299_792_458.0
E_CHARGE_C = 1.602_176634e-19
M_ELECTRON_KG = 9.109_3837015e-31
M_PROTON_KG = 1.672_62192369e-27

# Electron rest energy ~ 0.511 MeV; 2 m_e c^2 for e+ e- annihilation photons (conceptual)
E_ELECTRON_REST_J = M_ELECTRON_KG * C_LIGHT_MS**2
