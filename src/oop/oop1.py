# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    """Base class Vehicle"""
    pass


class GroundVehicle(Vehicle):
    """Subclass GroundVehicle"""
    """Inherits from Vehicle"""
    pass


class Car(GroundVehicle):
    """Subclass Car"""
    """Inherits from GroundVehicle"""
    pass


class Motorcycle(GroundVehicle):
    """Subclass Motorcycle"""
    """Inherits from GroundVehicle"""
    pass


class FlightVehicle(Vehicle):
    """Subclass FlightVehicle"""
    """Inherits from Vehicle"""
    pass


class Starship(FlightVehicle):
    """Subclass Starship"""
    """Inherits from FlightVehicle"""
    pass


class Airplane(FlightVehicle):
    """Subclass Airplane"""
    """Inherits from FlightVehicle"""
    pass
