def predict(features, model, class_labels):
    pred = model.predict(features)[0]
    print(f"Prediction result (pred): {pred}, type: {type(pred)}")  # Debug
    
    # Jika class_labels adalah dict, gunakan sebagai mapping
    if isinstance(class_labels, dict):
        return class_labels.get(pred, pred)  # Gunakan get untuk aman
    # Jika class_labels adalah list, asumsikan pred adalah indeks numerik
    elif isinstance(class_labels, list):
        try:
            idx = int(pred)
            return class_labels[idx]
        except (ValueError, IndexError):
            # Jika pred adalah string label, kembalikan langsung (tidak ada mapping)
            return pred
    else:
        # Fallback: kembalikan pred langsung
        return pred