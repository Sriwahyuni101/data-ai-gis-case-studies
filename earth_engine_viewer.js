// OPTIONAL: paste this file into the Google Earth Engine Code Editor.
// Dataset: WRI / Google DeepMind Global Drivers of Forest Loss 2001-2023 v1.1.
// This displays a published global layer; it does not train a new model.
var drivers = ee.Image('projects/landandcarbon/assets/wri_gdm_drivers_forest_loss_1km/v1_1_2001_2023');
var classification = drivers.select('classification');
var palette = ['E39D29', 'E58074', 'E9D700', '51A44E', '895128', 'A354A0', '3A209A'];
var vis = {min: 1, max: 7, palette: palette};
Map.setCenter(102.26, -3.80, 5); // initial view near Bengkulu; not an analysis boundary
Map.addLayer(classification, vis, 'Dominant driver of tree-cover loss (2001–2023)');

// Optional: probability layer for class 1 (permanent agriculture).
// Values are stored on a 0–250 scale with a multiplier of 0.004.
var agricultureProbability = drivers.select('probability_1').multiply(0.004);
Map.addLayer(agricultureProbability, {
  min: 0, max: 1,
  palette: ['440154','481567','482677','453781','3b528b','2c728e','21908d','27ad81','5ec962','aadc32','fde725']
}, 'Probability: permanent agriculture', false);

print('Class legend (classification band):', ee.Dictionary({
  1: 'Permanent agriculture',
  2: 'Hard commodities',
  3: 'Shifting cultivation',
  4: 'Logging',
  5: 'Wildfire',
  6: 'Settlements and infrastructure',
  7: 'Other natural disturbances'
}));
print('Important: the product shows the dominant mapped driver in each ~1 km cell over 2001–2023; review the catalog limitations before interpretation.');
