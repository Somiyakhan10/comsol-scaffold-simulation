import mph
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

print("=" * 60)
print("COMSOL SCAFFOLD SIMULATION - RESULTS REPORT")
print("=" * 60)
print(f"Run Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

# Step 1: Start COMSOL
print("[1/5] Starting COMSOL...")
client = mph.start()
print("      [OK] COMSOL started successfully")

# Step 2: Load your project
print("[2/5] Loading scaffold model...")
model = client.load(r'c:\Users\SHOP\Downloads\scaffold_project.mph')
print("      [OK] Model loaded")

# Step 3: Run simulation
print("[3/5] Running finite element simulation...")
model.solve()
print("      [OK] Simulation complete")

# Step 4: Extract results
print("[4/5] Extracting stress data...")
stress_data = model.evaluate('solid.mises', 'N/m^2')
print(f"      [OK] Extracted {len(stress_data)} data points")

# Step 5: Calculate statistics
print("[5/5] Calculating statistics...")

# Basic statistics
max_stress = np.max(stress_data)
min_stress = np.min(stress_data)
avg_stress = np.mean(stress_data)
std_stress = np.std(stress_data)
median_stress = np.median(stress_data)

# Percentile analysis
p25 = np.percentile(stress_data, 25)
p75 = np.percentile(stress_data, 75)
p90 = np.percentile(stress_data, 90)

# Biological interpretation (thresholds)
osteogenic_threshold = 500
adipogenic_threshold = 200

bone_regions = sum(1 for s in stress_data if s > osteogenic_threshold)
fat_regions = sum(1 for s in stress_data if s < adipogenic_threshold)
mixed_regions = len(stress_data) - bone_regions - fat_regions

bone_percent = (bone_regions / len(stress_data)) * 100
fat_percent = (fat_regions / len(stress_data)) * 100
mixed_percent = (mixed_regions / len(stress_data)) * 100

# Print results
print("\n" + "=" * 60)
print("SIMULATION RESULTS")
print("=" * 60)

print("\nSTRESS STATISTICS:")
print("-" * 40)
print(f"   Maximum Stress:     {max_stress:,.2f} N/m²")
print(f"   Minimum Stress:     {min_stress:,.2f} N/m²")
print(f"   Average Stress:     {avg_stress:,.2f} N/m²")
print(f"   Median Stress:      {median_stress:,.2f} N/m²")
print(f"   Standard Deviation: {std_stress:,.2f} N/m²")
print(f"   25th Percentile:    {p25:,.2f} N/m²")
print(f"   75th Percentile:    {p75:,.2f} N/m²")
print(f"   90th Percentile:    {p90:,.2f} N/m²")

print("\nBIOLOGICAL INTERPRETATION:")
print("-" * 40)
print(f"   Osteogenic (> {osteogenic_threshold} N/m²): {bone_percent:.1f}% -> BONE FORMATION")
print(f"   Adipogenic (< {adipogenic_threshold} N/m²): {fat_percent:.1f}% -> FAT FORMATION")
print(f"   Mixed Region:       {mixed_percent:.1f}%")

print("\nCONCLUSION:")
print("-" * 40)
if bone_percent > 70:
    print("   [GOOD] Excellent design. High bone formation predicted.")
elif bone_percent > 50:
    print("   [GOOD] Good design. Further optimization possible.")
elif bone_percent > 30:
    print("   [WARNING] Moderate design. Consider reducing pore size.")
else:
    print("   [BAD] Poor design. Increase load or use stiffer material.")

print("\n" + "=" * 60)
print("RESULTS SAVED SUCCESSFULLY")
print("=" * 60)

# Save results to file
with open('simulation_results.txt', 'w') as f:
    f.write("COMSOL SCAFFOLD SIMULATION RESULTS\n")
    f.write("=" * 50 + "\n\n")
    f.write(f"Run Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    f.write("STRESS STATISTICS:\n")
    f.write(f"  Maximum Stress: {max_stress:.2f} N/m²\n")
    f.write(f"  Minimum Stress: {min_stress:.2f} N/m²\n")
    f.write(f"  Average Stress: {avg_stress:.2f} N/m²\n\n")
    f.write("BIOLOGICAL INTERPRETATION:\n")
    f.write(f"  Bone Formation: {bone_percent:.1f}%\n")
    f.write(f"  Fat Formation: {fat_percent:.1f}%\n")

print("\n[FILE] Results saved to: simulation_results.txt")

# Create a simple bar chart
plt.figure(figsize=(10, 6))
categories = ['Bone Formation', 'Mixed Region', 'Fat Formation']
percentages = [bone_percent, mixed_percent, fat_percent]
colors = ['red', 'orange', 'blue']
bars = plt.bar(categories, percentages, color=colors, edgecolor='black')
plt.ylabel('Percentage (%)')
plt.title('Scaffold Differentiation Prediction')
plt.ylim(0, 100)

# Add percentage labels on bars
for bar, pct in zip(bars, percentages):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, 
             f'{pct:.1f}%', ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('results_chart.png', dpi=300)
print("[CHART] Chart saved to: results_chart.png")

plt.show()