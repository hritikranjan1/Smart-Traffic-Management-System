import numpy as np

def predict_traffic(data):
    """
    Predicts traffic conditions based on sensor data.
    
    Args:
        data (list): A list of traffic density values.
    
    Returns:
        str: Predicted traffic condition ('Heavy Traffic' or 'Normal Traffic').
    """
    avg_density = np.mean(data)
    
    if avg_density > 70:
        return "Heavy Traffic"
    elif avg_density > 40:
        return "Moderate Traffic"
    else:
        return "Normal Traffic"

if __name__ == "__main__":
    sample_data = [30, 45, 60, 75, 50]
    prediction = predict_traffic(sample_data)
    print(f"Predicted Traffic Condition: {prediction}")
