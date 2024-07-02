import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Create a figure and an axis with a specific projection
fig = plt.figure(figsize=(10, 5))
ax = plt.axes(projection=ccrs.PlateCarree())

# Set the extent to the European region (min lon, max lon, min lat, max lat)
ax.set_extent([-30, 60, 30, 75], crs=ccrs.PlateCarree())

# Add coastlines and borders
ax.coastlines(resolution='50m')
ax.add_feature(cfeature.BORDERS, linestyle=':')

# Add gridlines
ax.gridlines(draw_labels=True)

# Optionally, add land and ocean features with color
ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='lightgray')
ax.add_feature(cfeature.OCEAN, edgecolor='black', facecolor='lightblue')

# Display the map
plt.title('Map of Europe')
plt.show()

