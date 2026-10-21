# -*- coding: utf-8 -*-
"""Sub-Maximal Running Economy & vVO2max for GenPark Personal Agent."""
import json
from typing import Dict, Any

class RunningEconomyVVO2MaxModel:
    @staticmethod
    def calculate_running_economy_and_vvo2max(steady_state_vo2: float, running_speed_km_h: float, vo2_max: float) -> Dict[str, Any]:
        oxygen_cost = round((steady_state_vo2 * 60.0) / (running_speed_km_h * 1000.0) * 1000.0, 1)
        vvo2max = round((vo2_max / (steady_state_vo2 / running_speed_km_h)), 2)
        return {"oxygen_cost_ml_kg_km": oxygen_cost, "vvo2max_km_h": vvo2max, "economy_tier": "ELITE" if oxygen_cost < 190 else ("GOOD" if oxygen_cost < 210 else "MODERATE")}

    @staticmethod
    def predict_marathon_finish_time(vvo2max_km_h: float, fractional_utilization_pct: float = 82.0) -> Dict[str, Any]:
        marathon_speed = vvo2max_km_h * (fractional_utilization_pct / 100.0)
        hours = 42.195 / marathon_speed
        h = int(hours); m = int((hours - h) * 60); s = int((((hours - h) * 60) - m) * 60)
        return {"predicted_time": f"{h:02d}:{m:02d}:{s:02d}", "marathon_pace_min_km": round(60.0 / marathon_speed, 2)}
