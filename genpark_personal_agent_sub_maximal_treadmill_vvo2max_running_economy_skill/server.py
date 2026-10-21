# -*- coding: utf-8 -*-
"""MCP Server for Sub-Maximal Treadmill Running Economy & vVO2max Skill."""
import sys
import json
import logging
from typing import Dict, Any

from .core import RunningEconomyVVO2MaxModel

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

TOOLS_SCHEMA = [
    {
        "name": "calculate_running_economy_and_vvo2max",
        "description": "Compute running economy and velocity at VO2 max (vVO2max km/h) from treadmill oxygen uptake telemetry.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "steady_state_vo2": {
                    "type": "number"
                },
                "running_speed_km_h": {
                    "type": "number"
                },
                "vo2_max": {
                    "type": "number"
                }
            },
            "required": [
                "steady_state_vo2",
                "running_speed_km_h",
                "vo2_max"
            ]
        }
    },
    {
        "name": "predict_marathon_finish_time",
        "description": "Predict marathon finish time based on vVO2max and fractional aerobic utilization (80-85%).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "vvo2max_km_h": {
                    "type": "number"
                },
                "fractional_utilization_pct": {
                    "type": "number"
                }
            },
            "required": [
                "vvo2max_km_h"
            ]
        }
    }
]

def handle_rpc(line: str) -> str:
    try:
        req = json.loads(line)
        method = req.get("method")
        msg_id = req.get("id")

        if method == "initialize":
            res = {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-personal-agent-sub-maximal-treadmill-vvo2max-running-economy-skill", "version": "1.0.0"}
            }
            return json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": res})

        elif method == "tools/list":
            return json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"tools": TOOLS_SCHEMA}})

        elif method == "tools/call":
            params = req.get("params", {})
            tool_name = params.get("name")
            args = params.get("arguments", {})

            target_func = getattr(RunningEconomyVVO2MaxModel, tool_name, None)
            if not target_func:
                return json.dumps({"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": f"Method not found: {tool_name}"}})

            result = target_func(**args)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "content": [{"type": "text", "text": json.dumps(result, indent=2)}]
                }
            })

        else:
            return json.dumps({"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": f"Method not found: {method}"}})

    except Exception as e:
        return json.dumps({"jsonrpc": "2.0", "id": req.get("id") if "req" in locals() else None, "error": {"code": -32000, "message": str(e)}})

def run_test():
    init_req = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
    init_res = json.loads(handle_rpc(init_req))
    assert init_res.get("result", {}).get("serverInfo", {}).get("name") == "genpark-personal-agent-sub-maximal-treadmill-vvo2max-running-economy-skill"

    list_req = json.dumps({"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
    list_res = json.loads(handle_rpc(list_req))
    assert len(list_res.get("result", {}).get("tools", [])) == 2
    return True

if __name__ == "__main__":
    if "--test" in sys.argv:
        if run_test():
            sys.exit(0)
        sys.exit(1)

    for line in sys.stdin:
        if not line.strip():
            continue
        out = handle_rpc(line)
        sys.stdout.write(out + "\n")
        sys.stdout.flush()
