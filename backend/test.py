# words = [
#                                  "revolution",
#                                  "solstice",
#                                  "meridians",
#                                  "International Dateline",
#                                  "hydrosphere",
#                                  "Prime Meridian",
#                                  "hemispheres",
#                                  "lithosphere",
#                                  "latitude",
#                                  "biosphere",
#                                  "North Pole",
#                                  "parallels",
#                                  "atmosphere",
#                                  "equinox",
#                                  "geographic coordinates",
#                                  "Tropic of Cancer",
#                                  "longitude",
#                                  "axis",
#                                  "Arctic Circle",
#                                  "Ring of Fire",
#                                  "rotation",
#                                  "Tropic of Capricorn",
#                                  "(arc of a) great circle",
#                                  "equator",
#                                  "Antarctic Circle",
#   ]

words = [
    "oceanic",
    "asthenosphere",
    "inner core,,",
    "Mohorovocic Discontinuity",
    "continental",
    "outer core",
    "S-Waves",
    "lithosphere",
    "focus",
    "tectonic",
    "P-Waves",
    "Precambrian",
    "epicenter",
    "gradational",
    "Love ",
    "Uniformitarianism",
    "fault",
    "Exogenic",
    "Rayleigh ",
    "Catastrophism",
    "Holocene",
    "Endogenic",
    "geomorphology",
    "Cenozoic",
]

clues = [
    "the heavier, denser, basaltic crust.",
    "This is where slow, convective currents occur and is  believed to be the engine that drives Plate Tectonics.",
    "The portion of the Earth composed primarily of iron and believed to be in a solid state.",
    "This separates the uppermost mantle from the crust.",
    "The lighter, less dense, granitic crust.",
    "This is believed to be in a liquid/molten state and composed of an iron alloy.",
    "These do not travel through molten rock. [They arrive at the seismic station second].",
    "This is the rigid outer part of the earth, consisting of the crust and upper mantle.",
    "The point within the Earth where original slippage occurs.",
    "These processes result in mountain building & earthquakes.",
    "These transmit through all types of material. [They arrive at the seismic station first].",
    "This Eon accounts for over 88% of Earth’s history.",
    "The place on Earth’s surface directly above the focus.",
    "These processes serve to smooth the landscape by wearing down and filling in.",
    "These move horizontally and perpendicular to the direction of the wave.",
    "The theory that landforms are a result of ongoing processes that have always been at work. ",
    "A crack, fracture or breakage zone in the Earth’s crust.",
    "This system derives its energy from the Sun.",
    "These waves move vertically and give a rolling effect.",
    "The belief that landforms were created by short-term events.",
    "This is the Epoch we currently live in. [last ~11.5 kya]",
    "This system derives its energy from within the Earth.",
    "This is the study of Earth’s landforms.",
    "This is our current Era, which means “new life”.",
]
questions = [
    "revolution",
    "solstice",
    "meridians",
    "International Dateline",
    "hydrosphere",
    "Prime Meridian",
    "hemispheres",
    "lithosphere",
    "latitude",
    "biosphere",
    "North Pole",
    "parallels",
    "atmosphere",
    "equinox",
    "geographic coordinates",
    "Tropic of Cancer",
    "longitude",
    "axis",
    "Arctic Circle",
    "Ring of Fire",
    "rotation",
    "Tropic of Capricorn",
    "(arc of a) great circle",
    "equator",
    "Antarctic Circle",
]


a = []
for i in range(len(words)):
    a.append([words[i], clues[i]])
print(a)
# print(len(words), len(clues))
