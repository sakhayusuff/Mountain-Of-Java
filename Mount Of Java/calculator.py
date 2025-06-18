# calculator.py
"""
Referensi algoritma kalkulator berat carrier
Logika ini sudah diimplementasikan di script.js
"""

def calculate_carrier_weight(body_weight, hiking_duration, terrain_difficulty, weather_condition, group_size, experience_level):
    # Base weight calculation (10-20% dari berat badan)
    if experience_level == 1:  # Pemula
        base_percentage = 0.10
    elif experience_level == 2:  # Menengah
        base_percentage = 0.15
    else:  # Ahli
        base_percentage = 0.20
    
    base_weight = body_weight * base_percentage
    
    # Adjustment factors
    duration_factor = 1 + (hiking_duration - 1) * 0.15
    terrain_factor = 1 + (terrain_difficulty - 1) * 0.1
    weather_factor = 1 + (weather_condition - 1) * 0.05
    group_factor = max(0.8, 1 - (group_size - 1) * 0.05)
    
    # Calculate final weight
    recommended_weight = base_weight * duration_factor * terrain_factor * weather_factor * group_factor
    
    # Safety limits
    max_safe_weight = body_weight * 0.25
    min_weight = body_weight * 0.08
    
    final_weight = min(max(recommended_weight, min_weight), max_safe_weight)
    
    return {
        'recommended_weight': round(final_weight, 1),
        'min_weight': round(min_weight, 1),
        'max_weight': round(max_safe_weight, 1)
    }

# Contoh penggunaan
if __name__ == "__main__":
    result = calculate_carrier_weight(70, 2, 2, 1, 4, 2)
    print(f"Berat carrier yang direkomendasikan: {result['recommended_weight']} kg")