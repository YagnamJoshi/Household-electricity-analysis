item=[
    # Heating & Cooling
    {
        "name": "Air Conditioner",
        "type": "1.5 Ton AC",
        "category": "Heating & Cooling",
        "min_power_w": 1200,
        "max_power_w": 1800,
        "power_w": 1500,
        "default_hours": 6,
        "continuous": False
    },
    {
        "name": "Water Heater",
        "type": "Geyser",
        "category": "Heating & Cooling",
        "min_power_w": 2000,
        "max_power_w": 3000,
        "power_w": 2500,
        "default_hours": 0.5,
        "continuous": False
    },
    {
        "name": "Space Heater",
        "type": "Room Heater",
        "category": "Heating & Cooling",
        "min_power_w": 1500,
        "max_power_w": 2000,
        "power_w": 1750,
        "default_hours": 2,
        "continuous": False
    },
    {
        "name": "Electric Iron",
        "type": "Steam Iron",
        "category": "Heating & Cooling",
        "min_power_w": 1000,
        "max_power_w": 2500,
        "power_w": 1750,
        "default_hours": 0.5,
        "continuous": False
    },

    # Kitchen
    {
        "name": "Induction Cooktop",
        "type": "Induction",
        "category": "Kitchen",
        "min_power_w": 1200,
        "max_power_w": 2000,
        "power_w": 1600,
        "default_hours": 1,
        "continuous": False
    },
    {
        "name": "Microwave Oven",
        "type": "Microwave",
        "category": "Kitchen",
        "min_power_w": 1000,
        "max_power_w": 1500,
        "power_w": 1250,
        "default_hours": 0.3,
        "continuous": False
    },
    {
        "name": "Electric Kettle",
        "type": "Kettle",
        "category": "Kitchen",
        "min_power_w": 1200,
        "max_power_w": 1800,
        "power_w": 1500,
        "default_hours": 0.2,
        "continuous": False
    },
    {
        "name": "Mixer Grinder",
        "type": "Mixer/Grinder",
        "category": "Kitchen",
        "min_power_w": 500,
        "max_power_w": 750,
        "power_w": 625,
        "default_hours": 0.2,
        "continuous": False
    },
    {
        "name": "Refrigerator",
        "type": "Double Door",
        "category": "Kitchen",
        "min_power_w": 150,
        "max_power_w": 250,
        "power_w": 200,
        "default_hours": 24,
        "continuous": True
    },

    # Utility & Laundry
    {
        "name": "Washing Machine",
        "type": "Semi/Top Load",
        "category": "Utility & Laundry",
        "min_power_w": 500,
        "max_power_w": 1000,
        "power_w": 750,
        "default_hours": 0.5,
        "continuous": False
    },
    {
        "name": "Washing Machine",
        "type": "Front Load",
        "category": "Utility & Laundry",
        "min_power_w": 1500,
        "max_power_w": 2200,
        "power_w": 1850,
        "default_hours": 0.5,
        "continuous": False
    },
    {
        "name": "Clothes Dryer",
        "type": "Electric Dryer",
        "category": "Utility & Laundry",
        "min_power_w": 2000,
        "max_power_w": 3000,
        "power_w": 2500,
        "default_hours": 1,
        "continuous": False
    },
    {
        "name": "Water Pump",
        "type": "Domestic Pump",
        "category": "Utility & Laundry",
        "min_power_w": 750,
        "max_power_w": 1500,
        "power_w": 1125,
        "default_hours": 1,
        "continuous": False
    },

    # Cooling & Airflow
    {
        "name": "Ceiling Fan",
        "type": "Standard",
        "category": "Cooling & Airflow",
        "min_power_w": 70,
        "max_power_w": 80,
        "power_w": 75,
        "default_hours": 8,
        "continuous": False
    },
    {
        "name": "Ceiling Fan",
        "type": "BLDC",
        "category": "Cooling & Airflow",
        "min_power_w": 28,
        "max_power_w": 35,
        "power_w": 32,
        "default_hours": 8,
        "continuous": False
    },
    {
        "name": "Table Fan",
        "type": "Table/Pedestal",
        "category": "Cooling & Airflow",
        "min_power_w": 50,
        "max_power_w": 70,
        "power_w": 60,
        "default_hours": 6,
        "continuous": False
    },
    {
        "name": "Air Cooler",
        "type": "Desert/Personal",
        "category": "Cooling & Airflow",
        "min_power_w": 150,
        "max_power_w": 250,
        "power_w": 200,
        "default_hours": 6,
        "continuous": False
    },

    # Entertainment & Electronics
    {
        "name": "LED TV",
        "type": "32-50 inch",
        "category": "Entertainment",
        "min_power_w": 30,
        "max_power_w": 100,
        "power_w": 65,
        "default_hours": 5,
        "continuous": False
    },
    {
        "name": "Desktop Computer",
        "type": "Gaming/Performance PC",
        "category": "Electronics",
        "min_power_w": 200,
        "max_power_w": 500,
        "power_w": 350,
        "default_hours": 5,
        "continuous": False
    },
    {
        "name": "Laptop",
        "type": "Laptop",
        "category": "Electronics",
        "min_power_w": 45,
        "max_power_w": 90,
        "power_w": 65,
        "default_hours": 6,
        "continuous": False
    },
    {
        "name": "Wi-Fi Router",
        "type": "Router/Modem",
        "category": "Electronics",
        "min_power_w": 10,
        "max_power_w": 15,
        "power_w": 12,
        "default_hours": 24,
        "continuous": True
    },
    {
        "name": "Smartphone Charger",
        "type": "Phone Charger",
        "category": "Electronics",
        "min_power_w": 5,
        "max_power_w": 12,
        "power_w": 8,
        "default_hours": 2,
        "continuous": False
    },

    # Lighting
    {
        "name": "LED Bulb",
        "type": "LED",
        "category": "Lighting",
        "min_power_w": 7,
        "max_power_w": 12,
        "power_w": 9,
        "default_hours": 6,
        "continuous": False
    },
    {
        "name": "Tube Light",
        "type": "LED Tube",
        "category": "Lighting",
        "min_power_w": 18,
        "max_power_w": 22,
        "power_w": 20,
        "default_hours": 6,
        "continuous": False
    },
    {
        "name": "CFL Bulb",
        "type": "CFL",
        "category": "Lighting",
        "min_power_w": 15,
        "max_power_w": 25,
        "power_w": 20,
        "default_hours": 6,
        "continuous": False
    },
    {
        "name": "Incandescent Bulb",
        "type": "Traditional",
        "category": "Lighting",
        "min_power_w": 60,
        "max_power_w": 100,
        "power_w": 80,
        "default_hours": 6,
        "continuous": False
    }
]