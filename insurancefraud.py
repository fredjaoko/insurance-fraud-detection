from pydantic import BaseModel

class Insurance(BaseModel):
    months_as_customer: int
    policy_csl: object 
    policy_deductable: int  
    policy_annual_premium: float
    umbrella_limit: int 
    insured_sex: object 
    insured_education_level: object 
    insured_occupation: object 
    insured_relationship: object 
    capital-gains: int 
    capital-loss: int
    incident_type: object 
    collision_type: object 
    incident_severity: object 
    authorities_contacted: object 
    incident_hour_of_the_day: int  
    number_of_vehicles_involved: int 
    property_damage: object 
    bodily_injuries: int 
    witnesses: int  
    police_report_available: object 
    injury_claim: int  
    property_claim: int  
    vehicle_claim: int 
    fraud_reported: object 
