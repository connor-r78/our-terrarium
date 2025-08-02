import math

def latlon_to_minecraft(lat_deg, lon_deg):
    R = 6378137
    scale = 70.0

    lat_rad = math.radians(lat_deg)
    lon_rad = math.radians(lon_deg)

    x = R * lon_rad
    z = R * math.log(math.tan(math.pi / 4 + lat_rad / 2))

    mc_x = x / scale
    mc_z = -z / scale
    
    return mc_x, mc_z

lat = 37.23
lon = -77.405

mc_x, mc_z = latlon_to_minecraft(lat, lon)
print(f"Minecraft coordinates: x = {mc_x:.2f}, z = {mc_z:.2f}")