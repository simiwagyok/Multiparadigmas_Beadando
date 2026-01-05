import pytest
from backend.logic import szamol_bevetel
from backend.schemas import AutoJobResponse
from datetime import datetime
def test_ures(): assert szamol_bevetel([]) == 0.0
