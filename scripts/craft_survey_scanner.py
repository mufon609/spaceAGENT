#!/usr/bin/env python3
import time, sys
from scripts.sm import call, sc, status_line, wait_idle

print("=== STARTING SURVEY SCANNER RETRIEVAL & CRAFTING PIPELINE ===")
print("Initial status:", status_line())

# 1. Fly to Ramen's Rest (16 jumps)
call("spacemolt", "undock", {})
wait_idle()

outbound = [
    "node_alpha", "synchrony", "the_experiment", "achernar",
    "garnet", "atlas", "intercrus", "kitalpha", "kepler_442",
    "theemin", "hollowcrest", "alathfar", "sabik", "tidewater", "last_light"
]

for dest in outbound:
    call("spacemolt", "jump", {"target_system": dest})
    wait_idle()

call("spacemolt", "travel", {"target_poi": "ramens_rest"})
wait_idle()
call("spacemolt", "dock", {})
wait_idle()

print("Docked at Ramen's Rest! Refueling...")
call("spacemolt", "refuel", {})

# Withdraw materials: 17 trade_crystal, 24 silicon_ore
print("Withdrawing crystals and silicon...")
call("spacemolt_storage", "withdraw", {"item_id": "trade_crystal", "quantity": 17, "target": "self"})
call("spacemolt_storage", "withdraw", {"item_id": "silicon_ore", "quantity": 24, "target": "self"})

# Return home to Central Nexus
call("spacemolt", "undock", {})
wait_idle()

home_route = [
    "tidewater", "sabik", "alathfar", "hollowcrest", "theemin",
    "kepler_442", "kitalpha", "intercrus", "atlas", "garnet",
    "achernar", "the_experiment", "synchrony", "node_alpha", "nexus_prime"
]

for dest in home_route:
    call("spacemolt", "jump", {"target_system": dest})
    wait_idle()

call("spacemolt", "travel", {"target_poi": "the_core"})
wait_idle()
call("spacemolt", "dock", {})
wait_idle()

print("Safely docked at Central Nexus! Status:", status_line())
call("spacemolt", "refuel", {})

# Withdraw needed carbon_ore and copper_wiring from Central Nexus storage
print("Withdrawing 144 carbon ore from storage...")
call("spacemolt_storage", "withdraw", {"item_id": "carbon_ore", "quantity": 144, "target": "self"})

# Craft 6 runs of carbon_arc_circuit_etching -> makes 18 circuit_board
print("Crafting 18 circuit boards at Workshop...")
r = call("spacemolt", "craft", {"id": "carbon_arc_circuit_etching", "quantity": 6})
print("Circuit boards craft:", r)
wait_idle()

# Craft 2 runs of facet_trade_crystal -> makes 2 focused_crystal (uses 8 trade_crystal)
print("Crafting 2 focused crystals at Workshop...")
r = call("spacemolt", "craft", {"id": "facet_trade_crystal", "quantity": 2})
print("Focused crystals craft:", r)
wait_idle()

# Craft 1 run of assemble_crystal_sensor_array -> makes 2 sensor_array (uses 6 trade_crystal + 3 circuit_board)
print("Crafting sensor arrays at Workshop...")
r = call("spacemolt", "craft", {"id": "assemble_crystal_sensor_array", "quantity": 1})
print("Sensor arrays craft:", r)
wait_idle()

# Craft 1 run of build_survey_scanner_i -> makes 1 survey_scanner_i!
print("Crafting Survey Scanner I at Workshop...")
r = call("spacemolt", "craft", {"id": "build_survey_scanner_i", "quantity": 1})
print("Survey scanner craft:", r)
wait_idle()

print("PIPELINE COMPLETE! Cargo contents:")
print(sc(call("spacemolt", "get_cargo")).get("items", []))

