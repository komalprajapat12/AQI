def get_aqi_category(aqi):

    if aqi <= 50:
        return "Good"

    elif aqi <= 100:
        return "Moderate"

    elif aqi <= 150:
        return "Unhealthy for Sensitive"

    elif aqi <= 200:
        return "Unhealthy"

    elif aqi <= 300:
        return "Very Unhealthy"

    else:
        return "Hazardous"


def health_advice(aqi):

    if aqi <= 50:
        return "Air quality is good. Enjoy outdoor activities."

    elif aqi <= 100:
        return "Sensitive people should limit prolonged outdoor activity."

    elif aqi <= 150:
        return "Wear mask when going outside."

    elif aqi <= 200:
        return "Avoid outdoor exercise."

    else:
        return "Stay indoors and wear protective mask."