from cmath import exp
from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
import math
import Evapotranspiration_covered_areas
import Evapotranspiration_noncovered_areas


def et_QDWB(
    Soil_wetness_in_previous_step : float,
    Permanent_wilting_point_wet : float,
    Field_capacity_wet : float,
    soil_depth : float,
    Crop_Coefficient : float,
    Crop_Cover : float,
    Reference_Crop_Evapotranspiration : float,
    Is_in_fisrt_step : bool,
    infiltration : float = None,
    Available_Evaporable_Water_in_previous_step : float = None,
    initial_Available_Evaporable_Water : float = None
) -> float:

    # reference_evapotranspiration
    """
    Description
    -----------
    calculate Available_water With FC and PWP 
    ----------
    Soil_wetness_in_previous_step : float
        Soil_wetness_in_previous_step in percent(volumetric)
    Permanent_wilting_point_wet : float
        Permanent_wilting_point_wet in percent(volumetric)
    Field_capacity_wet : float
        Field_capacity_wet in percent(volumetric)
    soil_depth : float
        soil_depth in mm
    Crop_Coefficient : float
        Crop_Coefficient in No units
    Crop_Cover : float
        Crop_Cover in No units
    Reference_Crop_Evapotranspiration : float
        Reference_Crop_Evapotranspiration in mm
    Is_in_fisrt_step : bool
        Is_in_fisrt_step in No units
    infiltration : float
        infiltration in mm
    Available_Evaporable_Water_in_previous_step : float
        Available_Evaporable_Water_in_previous_step in mm
    initial_Available_Evaporable_Water : float
        initial_Available_Evaporable_Water in mm
   
    Returns
    -------
    et_QDWB : float
        real evapotranspiration with QDWB in mm
    
    """
    ET_covered = Evapotranspiration_covered_areas.et_covered(
        Soil_wetness_in_previous_step = Soil_wetness_in_previous_step,
        Permanent_wilting_point_wet = Permanent_wilting_point_wet,
        Field_capacity_wet = Field_capacity_wet,
        soil_depth = soil_depth,
        Crop_Coefficient = Crop_Coefficient,
        Crop_Cover = Crop_Cover,
        Reference_Crop_Evapotranspiration = Reference_Crop_Evapotranspiration
    )

    E_noncovered = Evapotranspiration_noncovered_areas.e_noncovered(
        Is_in_fisrt_step = Is_in_fisrt_step,
        Permanent_wilting_point_wet = Permanent_wilting_point_wet,
        Field_capacity_wet = Field_capacity_wet,
        soil_depth = soil_depth,
        Crop_Cover = Crop_Cover,
        Reference_Crop_Evapotranspiration = Reference_Crop_Evapotranspiration,
        infiltration = infiltration,
        Available_Evaporable_Water_in_previous_step = Available_Evaporable_Water_in_previous_step,
        initial_Available_Evaporable_Water = initial_Available_Evaporable_Water
    )

    return ET_covered + E_noncovered



# print(et_QDWB(
#     Soil_wetness_in_previous_step = 290,
#     Permanent_wilting_point_wet = 20,
#     Field_capacity_wet = 60,
#     soil_depth = 250,
#     Crop_Coefficient = 0.6,
#     Crop_Cover = 0.4,
#     Reference_Crop_Evapotranspiration = 2,
#     Is_in_fisrt_step = True,
#     initial_Available_Evaporable_Water = 145
# ))






