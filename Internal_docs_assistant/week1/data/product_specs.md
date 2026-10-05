# Northwind Robotics — Product Specs: "Warehouse Rover R2"

## Overview
The Warehouse Rover R2 is an autonomous mobile robot (AMR) for indoor logistics.
It navigates warehouses using LiDAR + visual SLAM and transports payloads between
pick stations and packing zones.

## Key Specifications
- **Payload capacity:** 80 kg
- **Max speed:** 1.8 m/s (loaded), 2.2 m/s (unloaded)
- **Battery:** 48V 30Ah LiFePO4; ~8 hours continuous operation
- **Charging:** Auto-docking; 0–80% in 45 minutes
- **Navigation:** 2D LiDAR + stereo cameras, 360° obstacle detection
- **Safety:** Emergency stop, 5 cm minimum obstacle clearance, ISO 3691-4 compliant
- **Connectivity:** Wi-Fi 6, optional 5G module
- **Fleet size:** Up to 50 rovers per Fleet Manager instance

## Software
The R2 is managed by **Fleet Manager 4.2**, which handles task assignment,
traffic control, and battery-aware scheduling. The REST API allows integration
with warehouse management systems (WMS). Firmware updates are delivered
over-the-air and can be staged to a canary group before fleet-wide rollout.

## Support & SLA
Standard support covers business hours (9–5, Mon–Fri) with a 4-hour response SLA.
Premium support adds 24/7 coverage and a 1-hour response SLA. Replacement parts
for critical components ship within 48 hours under the Premium plan.

## Known Limitations
- Not rated for outdoor or wet environments (IP54 only).
- Reflective or glass surfaces can degrade LiDAR accuracy; add visual markers.
- Maximum ramp incline is 5 degrees.
