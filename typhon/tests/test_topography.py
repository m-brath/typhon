"""Testing interfaces to digital elevation models.
"""
import os
import pytest
import numpy as np
from typhon.topography import SRTM30

class TestEnvironment:
    """Testing the environment handler."""
    def setup_method(self):
        """No setup required."""
        pass

    def teardown_method(self):
        """No teardown required"""
        pass

    def test_srtm30_grids(self):
        for t, _, _, _, _ in SRTM30._tiles:
            lat_min, lon_min, lat_max, lon_max = SRTM30.get_bounds(t)
            lats_r, lons_r = SRTM30.get_grids(t)
            lats, lons = SRTM30.get_native_grids(lat_min, lon_min, lat_max, lon_max)
            print(t)
            assert(np.allclose(lats, lats_r))
            assert(np.allclose(lons, lons_r))

    def test_elevation(self):
        lat_min = 30
        lat_max = 50
        lon_min = 10
        lon_max = 30
        lats, lons, z = SRTM30.elevation(lat_min, lon_min, lat_max, lon_max)