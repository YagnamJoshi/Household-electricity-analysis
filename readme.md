# Household Electricity Consumption Analyzer

A desktop app (Tkinter + Matplotlib) that estimates monthly/seasonal/yearly electricity consumption and MSEDCL (Pune/PCMC) electricity bills for a household, based on a configurable list of appliances.

## Features

- **House type selection** — pick a preset household (1 RK, 1 BHK, 1.5 BHK, 2 BHK, 2.5 BHK, 3 BHK), each backed by its own appliance CSV.
- **Appliance editor** — view, add, edit, delete, or reset the appliance list for the selected house before running the analysis.
- **Dashboard** with:
  - KPI cards: total units (kWh), total bill (₹), average daily cost, top consuming category.
  - Monthly bill bar chart, with the selected period highlighted.
  - Consumption by category (horizontal bar).
  - Top 5 appliances by consumption for the selected period.
  - Bill component breakdown (donut chart: energy, wheeling, FAC, duty, fixed charge).
- **Filters** — connection type (Single-Phase / Three-Phase), FAC rate, view mode (Month / Season / Full Year), specific month or season, and appliance category.
- **Seasonal adjustment** — appliances like ACs, coolers, heaters, geysers, and fans get month-specific usage multipliers instead of a flat monthly estimate.
- **MSEDCL-accurate billing** — telescopic slab-based energy charges, wheeling charge, FAC, electricity duty, and fixed charge, matching the official residential (LT-1) tariff structure.

## Project Structure

```
project/
├── main.ipynb                  # Notebook containing the full app (all cells below)
└── data/
    ├── appliances_1RK.csv
    ├── appliances_1BHK.csv
    ├── appliances_15BHK.csv
    ├── appliances_2BHK.csv
    ├── appliances_25BHK.csv
    └── appliances_3BHK.csv
```

The `data/` folder must sit alongside the notebook (`DATA_DIR = "data"`), and each CSV must follow the schema below.

## Appliance CSV Schema

Each house-type CSV has one row per appliance/variant:

| Column          | Type    | Description                                              |
|-----------------|---------|------------------------------------------------------------|
| `name`          | string  | Appliance name (also used as the seasonal-factor lookup key) |
| `type`          | string  | Model/variant label (e.g. "1.5 Ton AC")                   |
| `category`      | string  | Grouping used for category charts/filters                 |
| `power_w`       | number  | Rated power per unit, in watts                             |
| `min_power_w`   | number  | Lower bound of typical wattage range (reference only)      |
| `max_power_w`   | number  | Upper bound of typical wattage range (reference only)      |
| `default_hours` | number  | Default hours of use per day, per unit                     |
| `continuous`    | bool    | `True` if the appliance runs 24×7 (e.g. fridge, router)    |
| `count`         | integer | Number of units owned; rows with `count = 0` are excluded on load |
| `total_power_w` | number  | `power_w × count` (reference/display only, not used in cost math) |

> Appliances flagged `continuous = True` are forced to `hours = 24` on load and on manual add/edit, regardless of what's in `default_hours`, so a bad value in that column can't silently undercount an always-on device.

## Cost Calculation Logic

1. **Per-appliance daily energy:**
   `daily_kwh = power_w × count × hours / 1000`
2. **Monthly energy per appliance**, adjusted by a seasonal multiplier for the appliance's `name` (defaults to `1.0` if no seasonal factor is defined for that month):
   `monthly_kwh = daily_kwh × 30 × seasonal_factor(name, month)`
3. **Monthly bill**, using MSEDCL's telescopic slab rates for Pune/PCMC:

   | Units (cumulative) | Rate (₹/unit) |
   |---------------------|---------------|
   | 0–100               | 4.28          |
   | 101–300             | 11.10         |
   | 301–500             | 15.38         |
   | 500+                | 17.68         |

   Then:
   - `wheeling = units × ₹1.60`
   - `fac = units × FAC rate` (default ₹0.35/unit, editable)
   - `duty = 16% × (energy_charge + wheeling + fac)`
   - `fixed = ₹130` (Single-Phase) or `₹435` (Three-Phase)
   - `total = energy_charge + wheeling + fac + duty + fixed`
4. **Period totals** (Month / Season / Full Year) sum the independently-billed months in that period — matching how MSEDCL actually resets slabs each billing month.

### Seasonal Factors

Multipliers are defined per appliance name and month (`1.0` = baseline, no override):

| Appliance        | Peak season                      |
|------------------|-----------------------------------|
| Air Conditioner  | Summer (Apr–Jun, up to 1.9×)      |
| Air Cooler       | Summer (Apr–Jun, up to 1.8×)      |
| Space Heater     | Winter (Dec–Jan, up to 1.9×)      |
| Water Heater     | Winter (Dec–Jan, up to 1.6×)      |
| Ceiling Fan      | Summer (Apr–Jun, up to 1.3×)      |

## Requirements

```
pandas
matplotlib
```

`tkinter` and `calendar` ship with standard CPython on most platforms (on Linux you may need to install `python3-tk` separately).

```bash
pip install pandas matplotlib
```

## Running

Open `main.ipynb` and run all cells — the last cell launches the app:

```python
app = ElectricityApp()
app.mainloop()
```

**Flow:** House selection → review/edit appliance list → dashboard.

## Customizing

- **Add/remove a house type:** update `HOUSE_FILES` and add a matching CSV in `data/`.
- **Change tariff rates:** edit `PUNE_SLABS`, the wheeling rate, duty %, or fixed charges in `calculate_full_bill`.
- **Change seasonal behavior:** edit `SEASONS` (month groupings) and `SEASONAL_FACTORS` (per-appliance multipliers).
- **Change default FAC rate:** edit the FAC field on the dashboard, or the `fac_rate` default in `calculate_full_bill`.

## Known Limitations

- Monthly estimates assume a flat 30-day month (real months are 28–31 days).
- Seasonal factors are only defined for a handful of appliance names; anything else uses a flat `1.0` multiplier year-round.
- Tariff figures are hardcoded for MSEDCL Pune/PCMC residential (LT-1) and will need updating if rates change or for a different DISCOM.