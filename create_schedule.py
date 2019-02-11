import json

low_morning = [
        {
            "heatSetpoint": 21.0, 
            "TimeOfDay": "07:00:00"
            }, 
        {
            "heatSetpoint": 16.0, 
            "TimeOfDay": "08:20:00"
            }, 
        ]

high_morning = [
        {
            "heatSetpoint": 21.0, 
            "TimeOfDay": "07:00:00"
            }, 
        ]

low_noon = [
        {
            "heatSetpoint": 15.0, 
            "TimeOfDay": "12:20:00"
            }, 
        ]

noon = [
        {
            "heatSetpoint": 21.0, 
            "TimeOfDay": "12:20:00"
            }, 
        ]

low_afternoon = [
        {
            "heatSetpoint": 16.0, 
            "TimeOfDay": "13:30:00"
            }, 
        {
            "heatSetpoint": 21.0, 
            "TimeOfDay": "16:30:00"
            }, 
        {
            "heatSetpoint": 15.0, 
            "TimeOfDay": "23:00:00"
            }, 
        ]

high_afternoon = [
        {
            "heatSetpoint": 21.0, 
            "TimeOfDay": "13:30:00"
            }, 
        {
            "heatSetpoint": 15.0, 
            "TimeOfDay": "23:00:00"
            }, 
        ]

low_afternoon_lossy = [
        {
            "heatSetpoint": 16.0, 
            "TimeOfDay": "13:30:00"
            }, 
        {
            "heatSetpoint": 21.0, 
            "TimeOfDay": "16:30:00"
            }, 
        {
            "heatSetpoint": 15.0, 
            "TimeOfDay": "20:00:00"
            }, 
        ]

high_afternoon_lossy = [
        {
            "heatSetpoint": 21.0, 
            "TimeOfDay": "13:30:00"
            }, 
        {
            "heatSetpoint": 15.0, 
            "TimeOfDay": "20:00:00"
            }, 
        ]

sp_low = [
        {
            "heatSetpoint": 12.0, 
            "TimeOfDay": "07:00:00"
            }, 
        {
            "heatSetpoint": 12.0, 
            "TimeOfDay": "22:30:00"
            }
        ]

sp_room = [
        {
            "heatSetpoint": 16.0, 
            "TimeOfDay": "06:35:00"
            }, 
        {
            "heatSetpoint": 14.0, 
            "TimeOfDay": "07:30:00"
            }, 
        {
            "heatSetpoint": 16.0, 
            "TimeOfDay": "18:00:00"
            }, 
        {
            "heatSetpoint": 14.0, 
            "TimeOfDay": "22:30:00"
            }
        ]

sp_bathroom_weekday_lossy = [
        {
            "heatSetpoint": 22.0, 
            "TimeOfDay": "06:30:00"
            }, 
        {
            "heatSetpoint": 18.0, 
            "TimeOfDay": "07:40:00"
            }, 
        {
            "heatSetpoint": 18.0, 
            "TimeOfDay": "18:00:00"
            }, 
        {
            "heatSetpoint": 14.0, 
            "TimeOfDay": "22:30:00"
            }
        ]

sp_bathroom_weekday = [
        {
            "heatSetpoint": 22.0, 
            "TimeOfDay": "06:30:00"
            }, 
        {
            "heatSetpoint": 18.0, 
            "TimeOfDay": "07:30:00"
            }, 
        {
            "heatSetpoint": 21.0, 
            "TimeOfDay": "18:00:00"
            }, 
        {
            "heatSetpoint": 16.0, 
            "TimeOfDay": "20:30:00"
            }
        ]

sp_bathroom_weekend_lossy = [
        {
            "heatsetpoint": 20.0, 
            "timeofday": "07:10:00"
            }, 
        {
            "heatsetpoint": 18.0, 
            "timeofday": "09:00:00"
            }, 
        {
            "heatsetpoint": 18.0, 
            "timeofday": "18:00:00"
            }, 
        {
            "heatsetpoint": 14.0, 
            "timeofday": "22:30:00"
            }
        ]

sp_bathroom_weekend = [
        {
            "heatSetpoint": 23.0, 
            "TimeOfDay": "08:00:00"
            }, 
        {
            "heatSetpoint": 17.0, 
            "TimeOfDay": "10:00:00"
            }, 
        {
            "heatSetpoint": 21.0, 
            "TimeOfDay": "18:00:00"
            }, 
        {
            "heatSetpoint": 16.0, 
            "TimeOfDay": "20:00:00"
            }
        ]


def create_schedule(schedules):
    json_schedules = []

    for i, schedule in enumerate(schedules):
        json_schedules.append(
                {
                    "DayOfWeek": i, 
                    "Switchpoints": schedule
                    }
                )

    return { "DailySchedules": json_schedules }

schedule = {
    "1463707": {
        "name": "Lio", 
        "schedule": create_schedule([sp_room] * 7)
        },
    "1426070": {
        "name": "Siemen", 
        "schedule": create_schedule([sp_room] * 7)
        },
    "1426064": {
        "name": "Kamer", 
        "schedule": create_schedule([sp_room] * 7)
        },
    "1414656": {
        "name": "Tuur", 
        "schedule": create_schedule([sp_room] * 7)
        },

    "1406768": {
        "name": "Bureau", 
        "schedule": create_schedule([sp_low] * 7)
        },
    "4496910": {
        "name": "Wasruimte", 
        "schedule": create_schedule([sp_low] * 7)
        },

    "2030471": {
        "name": "Badk 2", 
        "schedule": create_schedule(
            [sp_bathroom_weekday_lossy] * 5 +
            [sp_bathroom_weekend_lossy] * 2
            )
        },
    "1406793": {
        "name": "Badkamer", 
        "schedule": create_schedule(
            [sp_bathroom_weekday] * 5 +
            [sp_bathroom_weekend] * 2
            )
        },

    "1426079": {
        "name": "Veranda", 
        "schedule": create_schedule(
            [
                low_morning + noon + low_afternoon_lossy,
                high_morning + noon + high_afternoon_lossy,
                high_morning + noon + high_afternoon_lossy,
                high_morning + low_noon + low_afternoon_lossy,
                low_morning + noon + low_afternoon_lossy,

                high_morning + noon + high_afternoon_lossy,
                high_morning + noon + high_afternoon_lossy
                ]
            )
        },
    "1406794": {
        "name": "Woonkamer", 
        "schedule": create_schedule(
            [
                low_morning + noon + low_afternoon,
                high_morning + noon + high_afternoon,
                high_morning + noon + high_afternoon,
                high_morning + low_noon + low_afternoon,
                low_morning + noon + low_afternoon,

                high_morning + noon + high_afternoon,
                high_morning + noon + high_afternoon
                ]
            )
        },
    }

print("Nieuw bestand schrijven ...")

f = open("new_zone_schedules.json", "w")
f.write(json.dumps(schedule, indent=4))
f.close()

