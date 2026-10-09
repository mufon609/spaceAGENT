# Playbooks

All commands use scripts/sm.py (see README). Setup once per shell:
```
export SM_USER='Alien_Abductee_Gemini' SM_PASS='<password from user>'
alias sm='python3 /path/to/scripts/sm.py'
```
If no shell: use MCP equivalents (spacemolt action=jump/travel/dock/mine; spacemolt_storage action=deposit).

## PB-0 Session start check
```
sm status        # credits, location, fuel, cargo, hull
sm active        # mission progress
sm storage       # storage at docked station
```

## PB-1 Acubens stockpile loop (Carbon/Tungsten/Lead/Platinum/Palladium)
Start: docked node_beta_industrial_station or node_gamma_relay_station.
```
sm jump acubens            # 60s, lands at acubens_belt, 1 fuel
sm mine 20                 # stops when cargo full (~9 cycles at 65 cargo)
sm jump node_gamma         # or node_beta
sm go node_gamma_relay_station   # or node_beta_industrial_station
sm dock
sm dump                    # deposit all cargo
```
Yield per trip (65 cargo): ~W20 C21 Pd2, Pt 0-2. Acubens = Low security: if `mine` prints STOP pirates, leave.
Trip time ~6 min. Refuel when < 30: MCP spacemolt action=refuel (docked).

## PB-2 Cheap buy-mission (Central Nexus)
```
sm call spacemolt accept_mission '{"id":"market_participation_buying"}'
sm call spacemolt buy '{"id":"copper_ore","quantity":10}'    # ~10cr
sm active    # get mission_id
sm call spacemolt complete_mission '{"id":"<mission_id>"}'   # +1000cr
sm dump
```
Done once 2026-10-09; check if repeatable.

## PB-3 Explore a system (record to resources.md)
```
sm route <system>; sm jump <system>; sm sys     # note security line FIRST
sm go <belt_poi>; sm poi                       # record ores, richness, remaining
```
If security is lawless/unknown and not approved: jump back immediately.
