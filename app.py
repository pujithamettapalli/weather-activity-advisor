
import streamlit as st

st.set_page_config(
    page_title="Weather Activity Advisor",
    page_icon="🌦️"
)

st.title("🌦️ Weather Activity Advisor")
st.write("I can suggest activities based on weather conditions!")

temperature = st.slider("Temperature (°C)", -5, 50, 28)
rain = st.slider("Chance of Rain (%)", 0, 100, 10)
wind = st.slider("Wind Speed (km/h)", 0, 100, 5)


def get_advice(temperature, rain, wind):

    # RULE 1: Very heavy rain
    if rain >= 70:
        return (
            "🏠 Recommendation: Stay indoors.\n\n"
            "Activities: Reading, indoor games, or yoga.\n\n"
            "Reason: The chance of rain is very high."
        )

    # RULE 2: Strong wind
    elif wind >= 40:
        return (
            "💨 Recommendation: Avoid outdoor sports.\n\n"
            "Activities: Indoor fitness or board games.\n\n"
            "Reason: Strong winds may make outdoor "
            "activities unsafe."
        )

    # RULE 3: Extreme heat
    elif temperature >= 40:
        return (
            "🥵 Recommendation: Avoid strenuous outdoor activity.\n\n"
            "Activities: Indoor games or a relaxing activity.\n\n"
            "Reason: Extreme heat increases the risk of "
            "heat-related illness."
        )

    # RULE 4: Very cold weather
    elif temperature <= 5:
        return (
            "🧣 Recommendation: Choose warm indoor activities.\n\n"
            "Activities: Reading, indoor games, or stretching.\n\n"
            "Reason: The temperature is very low."
        )

    # RULE 5: Hot weather
    elif temperature >= 33:
        return (
            "☀️ Recommendation: Prefer indoor exercise.\n\n"
            "Activities: Yoga, stretching, or light exercise.\n\n"
            "Reason: High temperatures can cause overheating."
        )

    # RULE 6: High chance of rain
    elif rain >= 50:
        return (
            "🌧️ Recommendation: Plan indoor activities.\n\n"
            "Activities: Board games, reading, or indoor workouts.\n\n"
            "Reason: Rain is reasonably likely."
        )

    # RULE 7: Moderate chance of rain
    elif rain >= 21:
        return (
            "🌦️ Recommendation: Choose a flexible activity.\n\n"
            "Activities: A short walk near shelter or indoor games.\n\n"
            "Reason: Rain may interrupt outdoor plans."
        )

    # RULE 8: Strong but not extreme wind
    elif wind >= 25:
        return (
            "🍃 Recommendation: Prefer sheltered activities.\n\n"
            "Activities: Indoor fitness or yoga.\n\n"
            "Reason: Wind may make cycling and outdoor games "
            "less comfortable."
        )

    # RULE 9: Cold weather
    elif temperature <= 15:
        return (
            "🧥 Recommendation: Take a brisk walk if comfortable.\n\n"
            "Activities: Walking or light exercise with warm clothing.\n\n"
            "Reason: The weather is cool and rain is relatively low."
        )

    # RULE 10: Mild weather
    elif temperature <= 19:
        return (
            "🌳 Recommendation: Enjoy a nature walk.\n\n"
            "Activities: Walking, light jogging, or photography outdoors.\n\n"
            "Reason: Mild temperatures and low rain favor outdoor plans."
        )

    # RULE 11: Ideal cycling conditions
    elif temperature <= 32 and rain <= 10 and wind <= 15:
        return (
            "🚴 Recommendation: Go cycling.\n\n"
            "Activities: Cycling or outdoor recreation.\n\n"
            "Reason: Comfortable temperature, low rain chance, "
            "and light wind."
        )

    # RULE 12: Comfortable outdoor conditions
    elif temperature <= 32 and rain <= 20 and wind <= 20:
        return (
            "🚶 Recommendation: Go for a walk or jog.\n\n"
            "Activities: Walking, jogging, or outdoor games.\n\n"
            "Reason: Weather conditions are generally favorable."
        )

    # RULE 13: Moderate wind
    elif wind >= 16:
        return (
            "🌿 Recommendation: Take a sheltered walk.\n\n"
            "Activities: Walking in a protected area or indoor exercise.\n\n"
            "Reason: Wind may affect comfort during outdoor activities."
        )

    # RULE 14: Remaining mild conditions
    else:
        return (
            "🎯 Recommendation: Choose a light outdoor activity "
            "if conditions are comfortable.\n\n"
            "Activities: A short walk or gentle stretching.\n\n"
            "Reason: No major rule matched, so choose a flexible "
            "activity and monitor local weather."
        )

if st.button("Get Activity Advice"):
    advice = get_advice(temperature, rain, wind)
    st.success(advice)
